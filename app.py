
from flask import Flask, request
from database import get_connection, create_table

app = Flask(__name__)

create_table()


@app.route("/")
def home():
    return {"message": "REST API Buku berhasil berjalan"}


@app.route("/api/books", methods=["GET"])
def get_books():
    connection = get_connection()
    books = connection.execute("SELECT * FROM books").fetchall()
    connection.close()

    return {"data": [dict(book) for book in books]}


@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("author"):
        return {"error": "Judul dan penulis wajib diisi"}, 400

    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO books (title, author, year, stock) VALUES (?, ?, ?, ?)",
        (
            data["title"],
            data["author"],
            data.get("year"),
            data.get("stock", 0)
        )
    )

    connection.commit()
    book_id = cursor.lastrowid
    connection.close()

    return {
        "message": "Buku berhasil ditambahkan",
        "id": book_id
    }, 201


@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()

    if not data:
        return {"error": "Data JSON wajib diisi"}, 400

    connection = get_connection()

    book = connection.execute(
        "SELECT * FROM books WHERE id = ?", (book_id,)
    ).fetchone()

    if book is None:
        connection.close()
        return {"error": "Buku tidak ditemukan"}, 404

    title = data.get("title", book["title"])
    author = data.get("author", book["author"])
    year = data.get("year", book["year"])
    stock = data.get("stock", book["stock"])

    connection.execute(
        """UPDATE books
        SET title = ?, author = ?, year = ?, stock = ?
        WHERE id = ?""",
        (title, author, year, stock, book_id)
    )

    connection.commit()
    connection.close()

    return {"message": "Buku berhasil diperbarui"}


@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    connection = get_connection()

    book = connection.execute(
        "SELECT * FROM books WHERE id = ?", (book_id,)
    ).fetchone()

    if book is None:
        connection.close()
        return {"error": "Buku tidak ditemukan"}, 404

    connection.execute(
        "DELETE FROM books WHERE id = ?", (book_id,)
    )

    connection.commit()
    connection.close()

    return {"message": "Buku berhasil dihapus"}



if __name__ == "__main__":
    app.run(debug=True)
