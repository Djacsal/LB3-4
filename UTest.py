import unittest
from main import app

class TestMortgageCalculator(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.loan_amount = 1000000
        self.interest_rate = 7
        self.loan_term = 20

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mortgage Calculator', response.data)

    def test_post(self):
        data = {
            'loan_amount': self.loan_amount,
            'interest_rate': self.interest_rate,
            'loan_term': self.loan_term
        }
        response = self.client.post('/', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ежемесячный плятёж'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
