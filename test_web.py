import unittest
from monitor_web import app

class TestWebMonitor(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        """التأكد من أن الصفحة الرئيسية تعمل."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_endpoint(self):
        """التأكد من أن الـ API يعيد بيانات JSON صحيحة."""
        response = self.app.get('/api/metrics')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)
        data = response.get_json()
        self.assertIn('cpu_usage_percent', data)

if __name__ == "__main__":
    unittest.main()
