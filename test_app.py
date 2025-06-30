from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Merhaba ben Mert Gürcüoğlu" in response.data
