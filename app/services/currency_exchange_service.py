from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

class CurrencyExchangeService:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, source, target, amount):
        # Check if source or target currency is not provided
        if source not in self.rates or target not in self.rates[source]:
            return {"error": "Currency not supported"}

        try:
            # Check if amount is a valid number
            amount = Decimal(amount.replace(',', ''))
        except InvalidOperation:
            return {"error": "Invalid amount"}

        # Perform the conversion
        rate = Decimal(str(self.rates[source][target]))
        converted = (amount * rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        return {"amount": f'{converted:,.2f}'}
