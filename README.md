<h1 align="center">
🏥 Mini Project – FastAPI APP
</h1>

### 🎯 Deskripsi
Project ini adalah layanan FastAPI sederhana yang merekomendasikan departemen spesialis berdasarkan informasi pasien (gender, usia, dan gejala). Service ini menggunakan Google Gemini (Generative AI) untuk membaca input dan mengembalikan rekomendasi.

### 📌 Cara Install & Menjalankan
1. Buka folder project
   ```bash
    cd mini-project-FastAPI
3. Buat virtual environment
   ```bash
    python -m venv venv
4. Aktifkan virtual environment

   Windows:
   ```bash
    venv\Scripts\activate
   ```
   Mac/Linux:
   ```bash
   source venv/bin/activate
5. Install dependency
   ```bash
    pip install fastapi uvicorn google-generativeai pydantic
6. Jalankan server
   ```bash
    uvicorn app:app --reload
7. Test API
   
    - Buka browser:
      ```bash
      http://127.0.0.1:8000/docs
    - Klik tombol POST /recommend → Try it out → isi body request, contoh:
      ```bash
      {
       "gender": "female",
        "age": 62,
        "symptoms": ["pusing", "mual", "sulit berjalan"]
      }
    - Jika berhasil akan menampilkan response, contoh:
      ```bash
      {
        "recommended_department": "Neurologi"
      }

