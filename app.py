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
        #loggıng kısmı 
        logging.info(f"Ziyaret sayısı: {count}")
        return f"<h1>Bu sayfa {count} kez ziyaret edildi.</h1>"
    else:
        logging.info("Test modunda çalışıyor.")
        return "<h1>Test modunda çalışıyor.</h1>"


    #monıtorıng kısmı
def health():
    try:
        if cursor:
            cursor.execute("SELECT 1;")  # basit bir sorgu
            return {"status": "ok", "database": "reachable"}, 200
        else:
            return {"status": "ok", "database": "test-mode"}, 200
    except Exception as e:
        logging.error(f"Health check failed: {e}")
        return {"status": "error", "message": str(e)}, 500

