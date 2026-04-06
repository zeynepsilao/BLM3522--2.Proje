# SOC Log Bridge: Gerçek Zamanlı Güvenlik Olay Akışı ve Bulut İşleme Sistemi

Bu proje, BLM3522 kodlu Bulut Bilişim Dersi (Proje 2) kapsamında geliştirilmiş gerçek zamanlı bir veri akışı ve işleme mimarisidir. Bir ağda gerçekleşen siber güvenlik olaylarını (Brute Force, SQL Injection, Malware Sync vb.) simüle ederek, bulut platformu üzerinde asenkron olarak işler ve depolar.

## Proje Mimarisinin Özeti

Sistem "Event-Driven" bir mimariyle kurgulanmış olup tamamen Google Cloud servisleri üzerine inşa edilmiştir.

* **Veri Üretimi (Simulation):** Python tabanlı `publisher.py` betiği, IoT/Ağ cihazlarından geliyormuş gibi rastgele güvenlik logları üretir.
* **Mesajlaşma Kuyruğu (Pub/Sub):** Üretilen JSON formatındaki loglar, GCP Pub/Sub üzerindeki `security-logs` konusuna anlık olarak fırlatılır.
* **Tetikleyici:** Pub/Sub'a düşen her yeni log, Cloud Function'ı otomatik olarak uyandırır.
* **Veri İşleme (Cloud Functions/Run):** `main.py` içerisinde çalışan asenkron fonksiyon, Base64 formatındaki veriyi çözer ve analiz eder.
* **Kalıcı Depolama (Firestore):** İşlenen loglar, analiz edilmek üzere isimlendirilmiş bir NoSQL veritabanına (`soc-logs`) benzersiz ID'lerle kaydedilir.

## Kullanılan Teknolojiler

* **Backend:** Python 3.12
* **Bulut Platformu:** Google Cloud Platform
* **Veri Akışı:** Cloud Pub/Sub
* **Serverless İşleme:** Cloud Functions/Run
* **Veritabanı:** Cloud Firestore
* **Güvenlik:** Google IAM

## Kurulum ve Çalıştırma

1.  Proje dosyalarını klonlayın.
2.  Gerekli bağımlılıkları yükleyin: `pip install -r requirements.txt`
3.  Google Cloud kimlik doğrulamasını (Authentication) tamamlayın.
4.  Log simülasyonunu başlatmak için terminalde şu komutu çalıştırın:
    `python3 publisher.py`
5.  Gelen loglar, gerçek zamanlı olarak GCP Firestore üzerindeki `logs` koleksiyonuna düşmeye başlayacaktır.

---
*Bu proje, siber güvenlik operasyon merkezlerinde (SOC) kullanılan gerçek zamanlı log toplama ve analiz altyapılarının bulut tabanlı bir prototipidir.*
