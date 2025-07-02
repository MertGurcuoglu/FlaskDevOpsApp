import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Merhaba ben Mert Gürcüoğlu ve bu bir DevOps projesidir.</h1>'

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
