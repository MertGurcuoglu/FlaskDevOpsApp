from app import app
import unittest
from unittest.mock import patch, MagicMock

class FlaskTestCase(unittest.TestCase):

    def test_test_modu(self):
        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test modunda çalışıyor", response.data.decode("utf-8"))

    @patch("app.cursor")
    @patch("app.conn")
    def test_db_modu(self, mock_conn, mock_cursor):
        # Veritabanı içeriği varmış gibi simüle ediyoruz
        mock_cursor.fetchone.return_value = [5]

        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Bu sayfa 6 kez ziyaret edildi.", response.data.decode("utf-8"))

    @patch("app.cursor")
    @patch("app.conn")
    def test_db_modu_ilk_zaman(self, mock_conn, mock_cursor):
        # İlk çalıştırma: hiç veri yokmuş gibi
        mock_cursor.fetchone.return_value = None

        tester = app.test_client()
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Bu sayfa 1 kez ziyaret edildi.", response.data.decode("utf-8"))

#monıtorıng testı
            def test_health_check(self):
        tester = app.test_client()
        response = tester.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn("ok", response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()
