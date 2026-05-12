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

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # อนุญาตให้ทุกที่เข้าถึงได้ (เหมาะสำหรับช่วงพัฒนาระบบ)
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

@app.post("/api/v1/analyze")
async def analyze_lab(payload: dict):
    # ในอนาคตเราจะเอา AI จริงๆ มาใส่ตรงนี้ครับ
    # ตอนนี้จำลอง Logic การสกัดข้อมูลเบื้องต้น
    raw_text = payload.get("text", "")
    return {
        "markers": [
            { "name": "Glucose", "value": 165, "unit": "mg/dL", "flag": "HIGH" },
            { "name": "HbA1c", "value": 7.8, "unit": "%", "flag": "HIGH" },
            { "name": "LDL", "value": 210, "unit": "mg/dL", "flag": "HIGH" }
        ],
        "axes": [
            { "id": "D3", "name": "Insulin & Glucose", "domain": "Metabolic" },
            { "id": "D1", "name": "Systemic Inflammation", "domain": "Immune" }
        ],
        "summary": "AI พบความผิดปกติในแกน Metabolic และ Immune แนะนำให้ติดตามผลอย่างใกล้ชิด"
    }

if __name__ == "__main__":
    import uvicorn
    # รันจาก root directory (backend_engine_v-twin)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
