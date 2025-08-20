from library import Library


def get_valid_isbn():
    """Kullanıcıdan geçerli ISBN alır (13 haneli rakam)."""
    while True:
        isbn = input("ISBN (13 haneli): ").strip()
        if isbn.isdigit() and len(isbn) == 13:
            return isbn
        print("❌ Geçersiz ISBN! 13 haneli rakamlardan oluşmalı.")


def main():
    library = Library()

    while True:
        print("\n=== Kütüphane Menüsü ===")
        print("1. Kitap Ekle (ISBN ile)")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        try:
            if choice == "1":
                isbn = get_valid_isbn()
                book = library.add_book(isbn)
                if book:
                    print("✅ Kitap eklendi:", book)

            elif choice == "2":
                isbn = get_valid_isbn()
                if library.find_book(isbn):
                    library.remove_book(isbn)
                    print("✅ Kitap silindi.")
                else:
                    print("❌ Bu ISBN ile kayıtlı kitap bulunamadı.")

            elif choice == "3":
                print("\n📚 Kütüphanedeki Kitaplar:")
                books = library.list_books()
                if books:
                    for book in books:
                        print("-", book)
                else:
                    print("❌ Kütüphanede hiç kitap yok.")

            elif choice == "4":
                isbn = get_valid_isbn()
                book = library.find_book(isbn)
                if book:
                    print("✅ Kitap bulundu:", book)
                else:
                    print("❌ Kitap bulunamadı.")

            elif choice == "5":
                print("Çıkılıyor...")
                break

            else:
                print("❌ Geçersiz seçim. Tekrar deneyin.")

        except Exception as e:
            print(f"⚠️ İşlem sırasında bir hata oluştu: {e}")


if __name__ == "__main__":
    main()
