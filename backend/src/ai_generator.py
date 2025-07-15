import os
import json
import random
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the Gemini 1.5 Flash model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_challenge_with_ai(difficulty="medium"):
    noise_tag = f"{datetime.now().isoformat()}_{random.randint(1000, 9999)}"

    prompt = f"""
Generate a unique python multiple-choice question of {difficulty} difficulty.

Return only a valid JSON object like:
{{
  "title": "Question title",
  "options": ["Option A", "Option B", "Option C", "Option D"],
  "correct_answer_id": 1,
  "explanation": "Explanation of the correct answer"
}}

Strict rules:
- Only one correct option
- Avoid repetition
- Add a uniqueness tag to prevent duplication: {noise_tag}
"""

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()

        print("\n[Raw Gemini Output]:")
        print(raw)

        # Extract and parse the JSON
        json_start = raw.find("{")
        json_end = raw.rfind("}") + 1
        json_string = raw[json_start:json_end]

        challenge = json.loads(json_string)

        # Validate structure
        for key in ["title", "options", "correct_answer_id", "explanation"]:
            if key not in challenge:
                raise ValueError(f"Missing key: {key}")

        return challenge

    except Exception as e:
        print(f"[Error generating challenge]: {e}")
        return {
            "title": "Default Question: List Append Method",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)"
            ],
            "correct_answer_id": 0,
            "explanation": "In Python, append() is the correct method to add an element to the end of a list."
        }

# Example usage
if __name__ == "__main__":
    mcq = generate_challenge_with_ai("hard")
    print("\n[Final MCQ JSON Output]:")
    print(json.dumps(mcq, indent=2))
