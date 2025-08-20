# Akbank-Library-Management-System_Step_2
## 📚 Python Kütüphane Uygulaması (ISBN ile Open Library API)
GİRİŞ
Bu repo, Global AI Hub Python 202 Bootcamp sürecinde bitirme projesini sunmak amacıyla oluşturulmuştur. Proje, 3 aşamalı eğitim sürecinin ikinci aşaması kapsamında geliştirilmiştir.
Bu proje, Python kullanarak Nesne Yönelimli Programlama (OOP) prensiplerine uygun bir terminal tabanlı kütüphane sistemi sağlar. Kitap ekleme, silme, arama ve listeleme işlemleri yapılabilir. Tüm veriler library.json dosyasında kalıcı olarak saklanır.
ÖZELLİKLER
📖 Kitap ekleme: Sadece ISBN girilir, başlık ve yazar bilgisi Open Library API üzerinden alınır
🔢 ISBN doğrulama:
Boş olamaz
Sadece rakamlardan oluşmalı
13 haneli olmalı
⚠️ Duplicate ISBN kontrolü
❌ Kitap silme (ISBN ile)
🔍 Kitap arama (ISBN ile)
📚 Kitap listeleme (ISBN 978-XXXXXXXXXXXX formatında)
💾 Tüm veriler JSON dosyasında saklanır.
Kullanılacak API: Open Library Books API
JSON dosyasına eklenecek yeni kitap ISBN bilgisine göre eklenir. Yazar adı ve kitap ismi otomatik olarak bu API den alınıp JSON dosyasına yazdırılır.Kullanılacak API: Open Library Books API
🧪 Pytest ile test edilmiş fonksiyonlar
