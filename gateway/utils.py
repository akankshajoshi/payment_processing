from flask_restful import reqparse
from datetime import datetime


def min_length(m_length):
    def validate(s):
        if len(s) >= m_length:
            return s
        raise RuntimeError("String must be at least %i characters long" % min)
    return validate


def get_payment_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('card_number', type=str, required=True)
    parser.add_argument('card_holder', type=str, required=True)
    parser.add_argument('expiry_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'), required=True)
    parser.add_argument('security_code', type=min_length(3))
    parser.add_argument('amount', type=float, required=True)
    return parser

