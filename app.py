import time
import psycopg2
from flask import Flask

app = Flask(__name__)

# Retry ile veritabanı bağlantısı
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
        break  # bağlantı başarılıysa döngüden çık
    except psycopg2.OperationalError:
        print("PostgreSQL henüz hazır değil. 2 saniye sonra tekrar denenecek...")
        time.sleep(2)

@app.route('/')
def index():
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

if __name__ == '__main__':
    # Test sırasında bu kısım çalışmasın
    import os
    if os.getenv("FLASK_ENV") != "testing":
        app.run(host='0.0.0.0', port=5000)
