pip install twilio
from twilio.rest import Client
ACCOUNT_SID = "ENTER_YOUR_ACCOUNT_SID"
AUTH_TOKEN = "ENTER_YOUR_AUTHENTICATION_TOKEN" 
TWILIO_NUMBER = "ENTER_YOUR_TWILIO_NUMBER"
RECIEVER_NUMBER = "ENTER_YOUR_RECEIVER_NUMBER"
Client = Client(ACCOUNT_SID,AUTH_TOKEN)
message = Client.messages.create(body = "good afternoon beautiful", from_ = TWILIO_NUMBER,to = RECIEVER_NUMBER )
