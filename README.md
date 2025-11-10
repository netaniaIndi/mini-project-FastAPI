### 🏥 Mini Project – FastAPI APP

### 🎯 Deskripsi
Project ini adalah layanan FastAPI sederhana yang merekomendasikan departemen spesialis berdasarkan informasi pasien (gender, usia, dan gejala). Service ini menggunakan Google Gemini (Generative AI) untuk membaca input dan mengembalikan rekomendasi.

### 📌 Cara Install & Menjalankan
1. Buka folder project
    cd mini project
2. Buat virtual environment
   ```bash
    python -m venv venv
4. Aktifkan virtual environment
   ```bash
    Windows: venv\Scripts\activate
    Mac/Linux: source venv/bin/activate
6. Install dependency
   ```bash
    pip install fastapi uvicorn google-generativeai pydantic
7. Tambahkan API Key Gemini
   Edit file app.py dan isi:
   GOOGLE_API_KEY = "ISI_API_KEY_ANDA"
9. Jalankan server
   ```bash
    uvicorn app:app --reload
10. Test API
    Buka browser: http://127.0.0.1:8000/docs
    Klik tombol POST /recommend → Try it out → isi body request, contoh:
        "gender": "female",
        "age": 62,
        "symptoms": ["pusing", "mual", "sulit berjalan"]
    Jika berhasil akan menampilkan response, contoh:
    {
        "recommended_department": "Neurologi"
    }

### 📂 Struktur File






