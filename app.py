from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from google import genai

GOOGLE_API_KEY = "AIzaSyC5B_OKl3CcsXTUZygZNLIdioHyzOfAR78"

# Konfigurasi client Gemini
client = genai.Client(api_key=GOOGLE_API_KEY)

app = FastAPI()

class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: List[str]

@app.post("/recommend")
async def recommend_department(info: PatientInfo):
    try:
        symptoms_text = ", ".join(info.symptoms)

        prompt = (
            f"Pasien berjenis kelamin {info.gender}, usia {info.age} tahun, "
            f"dengan gejala: {symptoms_text}. "
            "Berdasarkan informasi ini, rekomendasikan departemen spesialis yang paling tepat."
            " Jawab hanya 1 kata spesialis saja."
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",   # ✅ Model resmi terbaru
            contents=prompt
        )

        result = response.text.strip()

        return {"recommended_department": result}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
