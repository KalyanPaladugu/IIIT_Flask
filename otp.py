from twilio.rest import Client
from flask import Flask
from flask import session
import random

app=Flask(__name__)
def send_confirmation_code(to_number):
    verification_code = generate_code()
    send_sms("mobile number", verification_code)
    session['verification_code'] = verification_code
    return verification_code


def generate_code():
    return str(random.randrange(100000, 999999))


def send_sms(to_number, body):
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token = app.config['TWILIO_AUTH_TOKEN']
    twilio_number = app.config['TWILIO_NUMBER']
    client = Client(account_sid, auth_token)
    client.api.messages.create(to_number,
                           from_=twilio_number,
                           body=body)
 
if __name__=='__main__':
    app.run(debug=True)
