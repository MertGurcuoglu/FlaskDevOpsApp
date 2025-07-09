# FlaskDevOpsApp

Bu proje, Flask tabanlı bir web uygulaması için CI/CD sürecini öğrenmek ve adım adım kurmak amacıyla oluşturulmuştur.

## Özellikler

- Flask + PostgreSQL uygulaması  
- Docker ve Docker Compose ile çalışır  
- GitHub Actions ile CI süreci (pytest + coverage)  
- Logging ve Health Monitoring içerir  
- Otomatik test çalıştırma  
- Simülasyon olarak deploy adımı  

## Teknolojiler

| Teknoloji        | Açıklama                         |
|------------------|----------------------------------|
| Flask            | Web framework                    |
| Docker           | Container altyapısı              |
| Docker Compose   | Servis yönetimi                  |
| PostgreSQL       | Veritabanı                       |
| GitHub Actions   | CI süreci                        |
| Pytest           | Test framework’ü                |
| Coverage.py      | Kod kapsamı ölçümü              |
| Logging          | Python `logging` modülü ile log kaydı |

## Yapı

-  app.py # Flask uygulaması
-  test_app.py # Birim test dosyası
-  requirements.txt # Bağımlılıklar
-   Dockerfile # Flask container için yapılandırma
-   docker-compose.yml # Uygulama + DB servisi
-   .env # Ortam değişkenleri (DB config)
-   .gitignore # Git’e eklenmemesi gereken dosyalar
-   .github/workflows/ci.yml # GitHub Actions yapılandırması



## Test

Push işlemlerinde `pytest` ile testler otomatik çalışır.

**GitHub Actions Üzerinde:**  
Her push/pull request işleminde pytest otomatik çalışır. CI süreçleri `.github/workflows/ci.yml` dosyası üzerinden yönetilir.

## Çalıştırma

Lokalde uygulamayı başlatmak için terminalden aşağıdaki komut çalıştırılır:

docker-compose up --build

 
