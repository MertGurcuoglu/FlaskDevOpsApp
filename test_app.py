from app import app

def test_index():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert "Test modunda çalışıyor" in response.data.decode("utf-8")
