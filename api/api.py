import flask
from flask import request, jsonify
from flask import Response
from datetime import datetime
from .valid_credit_card import is_valid
import requests
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Test</h1>"

data = {
    "CreditCardNumber":"4916477106223428",
    "CardHolder":"akanksha",
    "ExpirationDate":"2021-09-01T21:03:05",
    "SecurityCode":"123",
    "Amount":"10"
}


@app.route('/process-payment/', methods=['GET'])
def ProcessPayment():
    card_number = data.get('CreditCardNumber')
    card_holder = data.get('CardHolder')
    expiry_date = data.get('ExpirationDate')
    security_code = data.get('SecurityCode')
    amount = float(data.get('Amount')) if data.get('Amount') else None
    if card_number and card_holder and expiry_date and amount:
        try:
            expiry_date = datetime.strptime(expiry_date, '%Y-%m-%dT%H:%M:%S')
            if expiry_date < datetime.now():
                return Response("The request is invalid", status=400, )
            if not is_valid(card_number):
                return Response("The request is invalid", status=400, )
            if security_code and not len(str(security_code)) == 3:
                return Response("The request is invalid", status=400, )
            if float(amount) < 0:
                return Response("The request is invalid", status=400, )
            post_data = {'card_number': card_number, 'card_holder': card_holder,
                         'expiry_date': datetime.strftime(expiry_date, '%Y-%m-%dT%H:%M:%S'),
                         'security_code': security_code, 'amount': amount}
        except:
            return Response("Any error", status=500, )

        return payment_switch(post_data)
    else:
        return Response("The request is invalid", status=400, )


def payment_switch(post_data):
    header = {'content_type': "application/json"}
    if 0 <= post_data['amount'] <= 20:
        response = requests.post('http://127.0.0.1:5050/cheap-payment/' ,
                                 headers=header, data=json.dumps(post_data))
    elif 20 < post_data['amount'] <= 500:
        try:
            response = requests.post('http://127.0.0.1:5050/expensive-payment/',
                                 headers=header, data=json.dumps(post_data))
        except:
            requests.adapters.DEFAULT_RETRIES = 1
            response = requests.post('http://127.0.0.1:5050/cheap-payment/',
                                     headers=header, data=json.dumps(post_data))

    else:
        requests.adapters.DEFAULT_RETRIES = 3
        response = requests.post('http://127.0.0.1:5050/premium-payment/',
                                 headers=header, data=json.dumps(post_data))
    return Response(response)


if __name__ == "__main__":
    app.run()