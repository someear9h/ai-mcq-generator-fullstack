// App.jsx
import { Routes, Route, Navigate } from "react-router-dom"
import { SignIn, SignUp } from "@clerk/clerk-react"

import ClerkProviderWithRoutes from "./auth/ClerkProviderWithRoutes.jsx"
import { Layout } from "./layout/Layout.jsx"
import { ChallengeGenerator } from "./challenge/ChallengeGenerator.jsx"
import { HistoryPanel } from "./history/HistoryPanel.jsx"

import "./App.css"

function App() {
  return (
    <ClerkProviderWithRoutes>
      <Routes>
        {/* Clerk Auth Routes */}
        <Route path="/sign-in/*" element={<SignIn routing="path" path="/sign-in" />} />
        <Route path="/sign-up/*" element={<SignUp routing="path" path="/sign-up" />} />

        {/* Protected App Routes */}
        <Route element={<Layout />}>
          <Route path="/" element={<ChallengeGenerator />} />
          <Route path="/history" element={<HistoryPanel />} />
        </Route>

        {/* Catch-all fallback */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </ClerkProviderWithRoutes>
  )
}

export default App
