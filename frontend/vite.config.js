import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
// define config
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");

  const isDev = env.VITE_DEBUG === "true";

  return {
    plugins: [react()],
    server: {
      ...(isDev && {
        proxy: {
          "/api": {
            target: "http://localhost:8000", // FastAPI backend
            changeOrigin: true,
            secure: false
          }
        }
      })
    },
    define: {
      __APP_VERSION__: JSON.stringify(process.env.npm_package_version)
    }
  };
});
