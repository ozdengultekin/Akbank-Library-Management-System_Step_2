import pytest
from unittest.mock import patch, MagicMock
from library import Library, Book

# ----------------------
# Fixtures
# ----------------------
@pytest.fixture
def empty_library(tmp_path):
    # Geçici dosya kullanıyoruz
    file = tmp_path / "library.json"
    return Library(filename=str(file))


# ----------------------
# add_book testleri
# ----------------------
@patch("library.httpx.get")
def test_add_book_success(mock_get, empty_library):
    # Mock API cevabı
    mock_response_book = MagicMock()
    mock_response_book.raise_for_status.return_value = None
    mock_response_book.json.return_value = {
        "title": "Matilda",
        "authors": [{"key": "/authors/OL34184A"}]
    }

    mock_response_author = MagicMock()
    mock_response_author.status_code = 200
    mock_response_author.json.return_value = {"name": "Roald Dahl"}

    # httpx.get çağrısı farklı URL için farklı response dönecek
    mock_get.side_effect = [mock_response_book, mock_response_author]

    isbn = "9780140328721"
    book = empty_library.add_book(isbn)

    assert book is not None
    assert book.title == "Matilda"
    assert book.author == "Roald Dahl"
    assert book.isbn == isbn
    assert len(empty_library.list_books()) == 1


@patch("library.httpx.get")
def test_add_book_already_exists(mock_get, empty_library):
    # Aynı ISBN’i iki kez eklemeye çalışalım
    isbn = "9780140328721"
    empty_library.books.append(Book("Matilda", "Roald Dahl", isbn))

    book = empty_library.add_book(isbn)
    assert book is None
    assert len(empty_library.list_books()) == 1  # Yeni ekleme yok


@patch("library.httpx.get")
def test_add_book_api_failure(mock_get, empty_library):
    # API hata veriyor (404)
    mock_get.side_effect = Exception("API Hatası")
    isbn = "9780000000000"
    book = empty_library.add_book(isbn)
    assert book is None
    assert len(empty_library.list_books()) == 0


# ----------------------
# remove_book testleri
# ----------------------
def test_remove_book(empty_library):
    book = Book("Matilda", "Roald Dahl", "9780140328721")
    empty_library.books.append(book)

    empty_library.remove_book(book.isbn)
    assert len(empty_library.list_books()) == 0


# ----------------------
# find_book testleri
# ----------------------
def test_find_book(empty_library):
    book = Book("Matilda", "Roald Dahl", "9780140328721")
    empty_library.books.append(book)

    found = empty_library.find_book("9780140328721")
    assert found == book

    not_found = empty_library.find_book("9780000000000")
    assert not_found is None


# ----------------------
# list_books testleri
# ----------------------
def test_list_books(empty_library):
    b1 = Book("Matilda", "Roald Dahl", "9780140328721")
    b2 = Book("Harry Potter", "J.K. Rowling", "9780439554930")
    empty_library.books.extend([b1, b2])

    books = empty_library.list_books()
    assert len(books) == 2
    assert b1 in books and b2 in books
