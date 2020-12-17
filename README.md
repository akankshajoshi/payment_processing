# payment_processing

ProcessPayment that receives a request with the data set

- CreditCardNumber (mandatory, string, it should be a valid credit card number)
- CardHolder: (mandatory, string)
- ExpirationDate (mandatory, DateTime, it cannot be in the past)
- SecurityCode (optional, string, 3 digits)
- Amount (mandatoy decimal, positive amount)

The Apis 

- PremiumPaymentGateway 
- ExpensivePaymentGateway 
- CheapPaymentGateway


The payment gateway that should be used to process each payment follows the next set of
business rules:
a) If the amount to be paid is less than £20, use CheapPaymentGateway.

b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
Otherwise, retry only once with CheapPaymentGateway.

c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
in case payment does not get processed.

