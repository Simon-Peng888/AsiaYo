from flask import Flask, request, jsonify
from decimal import Decimal, ROUND_HALF_UP
from app.services.currency_exchange_service import CurrencyExchangeService
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

exchange_service = CurrencyExchangeService(app.config['RATES'])

@app.route('/convert', methods=['GET'])
def convert():
    source = request.args.get('source')
    target = request.args.get('target')
    amount = request.args.get('amount')
    result = exchange_service.convert(source, target, amount)
    if "error" not in result:
        return jsonify({"msg": "success", "amount": result["amount"]})
    else:
        return jsonify({"msg": "error", "error": result["error"]}), 400

if __name__ == '__main__':
    app.run(debug=True)
