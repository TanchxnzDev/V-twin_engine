import firebase_admin
from firebase_admin import credentials, firestore, auth
import os
import json
from dotenv import load_dotenv

load_dotenv()

def initialize_firebase():
    if not firebase_admin._apps:
        # พยายามดึงค่าจาก Environment Variable (สำหรับ Railway)
        firebase_creds_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")
        
        if firebase_creds_json:
            # ถ้ามีค่าเป็น JSON string ให้โหลดตรงๆ
            creds_dict = json.loads(firebase_creds_json)
            cred = credentials.Certificate(creds_dict)
        else:
            # ถ้าไม่มี ให้พยายามหาไฟล์ local (สำหรับ Dev)
            try:
                cred = credentials.Certificate("tspi-ee68e-firebase-adminsdk-fbsvc-4d7ec1a2d3.json")
            except Exception:
                print("⚠️ Warning: Firebase credentials not found. Firebase features will be disabled.")
                return None

        firebase_admin.initialize_app(cred)
    
    return firestore.client()

# สร้าง instance ของ db ไว้ใช้งาน
db = initialize_firebase()
