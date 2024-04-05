import unittest
from app.services.currency_exchange_service import CurrencyExchangeService

class TestCurrencyExchangeService(unittest.TestCase):
    def setUp(self):
        self.service = CurrencyExchangeService({
            "USD": {"USD": 1, "JPY": 110},
            "JPY": {"JPY": 1, "USD": 0.0091}
        })

    def test_invalid_currency(self):
        result = self.service.convert("EUR", "USD", "100")
        self.assertEqual(result, {"error": "Currency not supported"})

    def test_invalid_amount(self):
        result = self.service.convert("USD", "JPY", "abc")
        self.assertEqual(result, {"error": "Invalid amount"})

    def test_rounding(self):
        result = self.service.convert("USD", "JPY", "1.005")
        self.assertEqual(result, {"amount": "110.55"})

if __name__ == "__main__":
    unittest.main()
