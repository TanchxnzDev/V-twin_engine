from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# เพิ่ม directory หลักเข้าไปใน path เพื่อให้หา module 'app' เจอ
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

app = FastAPI(
    title="dr_pat: V-Twin Engine",
    description="The core AI engine for patient intelligence",
    version="0.1.0"
)

# Set up CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health_check():
    return {
        "status": "online",
        "engine": "V-Twin",
        "message": "Engine is purring like a Harley!"
    }

if __name__ == "__main__":
    import uvicorn
    # รันจาก root directory (backend_engine_v-twin)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
