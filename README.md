<h1 align="center">
  🏥 Mini Project – FastAPI APP
</h1>

<div style="display:flex; justify-content:center;">
  <a href="https://github.com/netaniaIndi/mini-project-FastAPI" target="_blank" style="font-size:14px;">
    GitHub Repository
  </a>
</div>



### 🎯 Deskripsi
Project ini adalah layanan FastAPI sederhana yang merekomendasikan departemen spesialis berdasarkan informasi gender, usia, dan gejala pasien.

### 🚀 Cara Install & Menjalankan Aplikasi
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
6. Jalankan server FastAPI
   ```bash
    uvicorn app:app --reload

### 📌 Cara Pengujian API
1. Test via browser
   
   - Buka browser:
      ```bash
      http://127.0.0.1:8000/docs
   - Klik tombol POST /recommend → Try it out → isi body request → execute
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
2. Test via Postman
   - Buka Postman → Workspace → New → HTTP
   - Method → POST
   - URL:
     ```bash
     http://127.0.0.1:8000/recommend
   - Tab Body → pilih raw → pilih JSON, masukkan contoh body ini:
     ```bash
     {
        "gender": "female",
        "age": 62,
        "symptoms": ["pusing", "mual", "sulit berjalan"]
     }
   - Klik Send
   - Jika berhasil akan menampilkan response, contoh:
     ```bash
      {
        "recommended_department": "Neurologi"
      }
    <img width="892" height="772" alt="image" src="https://github.com/user-attachments/assets/a437b67a-aacd-4d62-81c7-426d8ed3d759" />













