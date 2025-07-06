import os
import time
import psycopg2
from flask import Flask
import logging


app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)


# Test ortamı değilse veritabanına bağlan
if os.getenv("FLASK_ENV") != "testing":
    while True:
        try:
            conn = psycopg2.connect(
                dbname="devdb",
                user="devuser",
                password="devpass",
                host="postgres",
                port="5432"
            )
            cursor = conn.cursor()
            break
        except psycopg2.OperationalError:
            print("PostgreSQL henüz hazır değil. 2 saniye sonra tekrar denenecek...")
            time.sleep(2)
else:
    conn = None
    cursor = None

@app.route('/')
def index():
    if cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS visits (count INT);")
        cursor.execute("SELECT count FROM visits;")
        result = cursor.fetchone()
        if result:
            count = result[0] + 1
            cursor.execute("UPDATE visits SET count = %s;", (count,))
        else:
            count = 1
            cursor.execute("INSERT INTO visits (count) VALUES (1);")
        conn.commit()
        return f"<h1>Bu sayfa {count} kez ziyaret edildi.</h1>"
    else:
        return "<h1>Test modunda çalışıyor.</h1>"

if __name__ == '__main__':
    if os.getenv("FLASK_ENV") != "testing":
        app.run(host='0.0.0.0', port=5000)

@app.route('/')
def index():
    logging.info("Ana sayfa endpoint'ine istek geldi.")
    if cursor:
        logging.info("Veritabanı bağlantısı aktif.")
        ...
        logging.info(f"Ziyaret sayısı: {count}")
        ...
    else:
        logging.info("Test modunda çalışıyor.")
        return "<h1>Test modunda çalışıyor.</h1>"
