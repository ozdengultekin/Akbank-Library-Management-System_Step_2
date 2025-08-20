import json
import os
import httpx


class Book:
    """Represents a single book in the library."""

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def format_isbn(self):
        """ISBN'i 978-XXXXXXXXXX formatına dönüştürür."""
        return f"{self.isbn[:3]}-{self.isbn[3:]}"

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.format_isbn()})"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn}

    @staticmethod
    def from_dict(data: dict):
        return Book(data["title"], data["author"], data["isbn"])


class Library:
    """Manages a collection of books and persists data in a JSON file."""

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, isbn: str):
        """Open Library API üzerinden kitap bilgisi alır ve ekler."""
        # ISBN zaten var mı kontrolü (önce bakıyoruz!)
        if any(b.isbn == isbn for b in self.books):
            print("❌ Bu kitap zaten kayıtlı!")
            return None  # Burada return yapıyoruz, aşağıdaki kod çalışmaz

        try:
            url = f"https://openlibrary.org/isbn/{isbn}.json"
            response = httpx.get(url, timeout=10, follow_redirects=True)
            response.raise_for_status()
            data = response.json()

            title = data.get("title", "Bilinmeyen Başlık")

            # Yazar bilgisi almak için ayrı istek
            authors = []
            for author in data.get("authors", []):
                key = author.get("key")
                if key:
                    author_url = f"https://openlibrary.org{key}.json"
                    author_resp = httpx.get(author_url, timeout=10, follow_redirects=True)
                    if author_resp.status_code == 200:
                        author_name = author_resp.json().get("name", "Bilinmeyen Yazar")
                        authors.append(author_name)

            author_str = ", ".join(authors) if authors else "Bilinmeyen Yazar"

            book = Book(title, author_str, isbn)
            self.books.append(book)
            self.save_books()
            return book

        except httpx.HTTPStatusError as e:
            print(f"❌ Kitap bulunamadı. ({isbn}) Hata: {e.response.status_code}")
        except httpx.RequestError as e:
            print(f"❌ API bağlantı hatası: {e}")
        except Exception as e:
            print(f"⚠️ Beklenmeyen hata: {e}")
        return None

    def remove_book(self, isbn: str):
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()

    def list_books(self):
        return self.books

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.books = [Book.from_dict(b) for b in data]
                except json.JSONDecodeError:
                    self.books = []
        else:
            self.books = []

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4, ensure_ascii=False)
