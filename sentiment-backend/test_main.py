import unittest
from fastapi.testclient import TestClient
from main import app  # Name of backend file to test

client = TestClient(app)

class TestSentimentAnalysis(unittest.TestCase):
    def test_analyze_positive_text(self):
        response = client.post(
            "/analyze/", json={"text": "I love this product!"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("label", response.json())
        self.assertIn("score", response.json())

    def test_analyze_empty_text(self):
        response = client.post("/analyze/", json={"text": ""})
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertIn("label", result)
        self.assertIn("score", result)
        self.assertGreaterEqual(result["score"], 0)

if __name__ == "__main__":
    unittest.main()