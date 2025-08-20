# Akbank-Library-Management-System_Step_2
## 📚 Python Kütüphane Uygulaması (ISBN ile Open Library API)
## GİRİŞ
Bu repo, Global AI Hub Python 202 Bootcamp sürecinde bitirme projesini sunmak amacıyla oluşturulmuştur. Proje, 3 aşamalı eğitim sürecinin ikinci aşaması kapsamında geliştirilmiştir.
Bu proje, Python kullanarak Nesne Yönelimli Programlama (OOP) prensiplerine uygun bir terminal tabanlı kütüphane sistemi sağlar. Kitap ekleme, silme, arama ve listeleme işlemleri yapılabilir. Tüm veriler library.json dosyasında kalıcı olarak saklanır.


## PROJE DOSYA YAPISI

library.py         # Book ve Library sınıflarının tanımlandığı dosya<br>
main.py            # Konsol uygulamasının çalıştırıldığı ana dosya<br>
test_library.py # Pytest ile testlerin yazıldığı dosya<br>
library.json       # Kitap verilerinin kaydedileceği JSON dosyası (ilk başta boş)<br>
requirements.txt   # Gerekli paketler<br>
README.md          # Projenin amacı, kurulumu ve kullanımı ile ilgili dökümantasyon<br>

## ÖZELLİKLER
📖 Kitap ekleme: Sadece ISBN girilir, başlık ve yazar bilgisi Open Library API üzerinden alınır.<br>
🔢 ISBN doğrulama:<br>
Boş olamaz.<br>
Sadece rakamlardan oluşmalı.<br>
13 haneli olmalı.<br>
⚠️ Duplicate ISBN kontrolü.<br>
❌ Kitap silme (ISBN ile)<br>
🔍 Kitap arama (ISBN ile)<br>
📚 Kitap listeleme (ISBN 978-XXXXXXXXXXXX formatında)<br>
💾 Tüm veriler JSON dosyasında saklanır.<br>
Kullanılacak API: Open Library Books API<br>
JSON dosyasına eklenecek yeni kitap ISBN bilgisine göre eklenir. Yazar adı ve kitap ismi otomatik olarak bu API den alınıp JSON dosyasına yazdırılır.Kullanılacak API: Open Library Books API<br>
Sistem hata mesajları try-except şeklinde kontrol edilmiştir. <br>
🧪 Pytest ile test edilmiş fonksiyonlar(@patch("library.httpx.get") → API çağrılarını mock ediyoruz. Gerçek internet bağlantısı gerekmez. empty_library fixture → geçici bir library.json dosyası kullanıyor, test ortamını kirletmez. Her test bağımsızdır ve pytest ile çalıştırılabilir)<br>

## KURULUM
1. Platform: PyCharm veya herhangi bir terminal<br>
Python sürümü: 3.7+<br>
2. Projeyi dosyalarını indirin:<br>
3. Gerekli paketleri yükleyin:
pip install -r requirements.txt
4.Opsiyonel: Proje için standart Python yeterlidir.
## KULLANIM
Uygulamayı başlatın:
Terminale python main.py yazın. 

Menü üzerinden seçim yapın:
1️⃣ Kitap Ekle (ISBN ile)
2️⃣ Kitap Sil (ISBN ile)
3️⃣ Kitapları Listele
4️⃣ Kitap Ara (ISBN ile)
5️⃣ Çıkış
Bilgileri girerken:
ISBN 13 haneli ve sadece rakamlardan oluşmalı
Zaten eklenmiş ISBN girilirse uyarı mesajı gösterilir
Kitap ekleme sırasında başlık ve yazar bilgisi otomatik çekilir.

## TESTLER

Projede testler pytest ile yazılmıştır.<br>
Çalıştırmak için:<br>
pytest tests/test_library.py -v<br>

## TEST SONUÇLARI

=============================================================================================== test session starts ================================================================================================
platform darwin -- Python 3.12.2, pytest-7.4.4, pluggy-1.0.0 -- /opt/anaconda3/bin/python<br>
cachedir: .pytest_cache<br>
rootdir: /Users/ozden/python_oop_kutuphane<br>
plugins: dash-3.0.0, langsmith-0.3.18, anyio-4.2.0<br>
collected 6 items                                                                                                                                                                                                  

test_library.py::test_add_book_success PASSED                                                                                                                                                                [ 16%]<br>
test_library.py::test_add_book_already_exists PASSED                                                                                                                                                         [ 33%]<br>
test_library.py::test_add_book_api_failure PASSED                                                                                                                                                            [ 50%]<br>
test_library.py::test_remove_book PASSED                                                                                                                                                                     [ 66%]<br>
test_library.py::test_find_book PASSED                                                                                                                                                                       [ 83%]<br>
test_library.py::test_list_books PASSED                                                                                                                                                                      [100%]<br>

================================================================================================ 6 passed in 0.01s =================================================================================================

