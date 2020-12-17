import flask
from flask import Response
from flask_restful import Resource, Api, reqparse
from .utils import get_payment_parser


app = flask.Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)


class CheapPaymentGateway(Resource):
    def post(self):
        parser = get_payment_parser()
        args = parser.parse_args()
        return Response('Payment is processed', status=200)


api.add_resource(CheapPaymentGateway, '/cheap-payment/')


class ExpensivePaymentGateway(Resource):
    def post(self):
        parser = get_payment_parser()
        args = parser.parse_args()
        return Response('Payment is processed', status=200)


api.add_resource(ExpensivePaymentGateway, '/expensive-payment/')


class PremiumPaymentGateway(Resource):
    def post(self):
        parser = get_payment_parser()
        args = parser.parse_args()
        return Response('Payment is processed', status=200)


api.add_resource(PremiumPaymentGateway, '/premium-payment/')


if __name__ == '__main__':
    app.run()
