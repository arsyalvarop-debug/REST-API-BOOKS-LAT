# REST API Books

REST API sederhana untuk mengelola data buku menggunakan Python, Flask, dan SQLite.

## Fitur

- **GET** — menampilkan semua buku
- **POST** — menambahkan buku baru
- **PUT** — mengubah data buku berdasarkan ID
- **DELETE** — menghapus buku berdasarkan ID

## Teknologi

- Python
- Flask
- SQLite
- Thunder Client untuk pengujian API

## Cara Menjalankan

1. Clone repository ini.
2. Buat dan aktifkan virtual environment.
3. Instal dependensi:

   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi:

   ```bash
   python app.py
   ```

5. Buka `http://127.0.0.1:5000/`.

## Endpoint API

| Method | Endpoint          | Fungsi             |
| ------ | ----------------- | ------------------ |
| GET    | `/api/books`      | Melihat semua buku |
| POST   | `/api/books`      | Menambahkan buku   |
| PUT    | `/api/books/<id>` | Mengubah buku      |
| DELETE | `/api/books/<id>` | Menghapus buku     |

## Format Data Buku

```json
{
  "title": "Laskar Pelangi",
  "author": "Andrea Hirata",
  "year": 2005,
  "stock": 10
}
```

## Catatan

Proyek ini dibuat sebagai latihan pengembangan REST API dan pengelolaan database sederhana.
