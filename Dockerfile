#python sürümünü belirtiyoruz
FROM python:3.12-slim

# çalışma dizini
WORKDIR /app

# requirements.txt dosyasını containera kopyalıyoruz
COPY requirements.txt .

# gerekli Python kütüphanelerini yüklüyoruz 
RUN pip install --no-cache-dir -r requirements.txt

# kalan tüm proje dosyalarını konteynıra kopyalıyoruz
COPY . .

# flask uygulamasını dış dünyaya açacağımız port
EXPOSE 5000

# konteyner çalışınca bu komutu çalıştırıyoruz
CMD ["python", "app.py"]

#her kod değişikliginden sonra konteynırı durdurup tekrar image build edip çalıstırmamız gerekır 
#şu an bunu elle yapıyorum manuel olarak ama
#projenin ilerleyen aşamasında CI/CD tarafında bunları otomatik hale getireceğim 