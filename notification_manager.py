from twilio.rest import Client
from consts import ACCOUNT_SID, AUTH_TOKEN, TWILIO_VIRTUAL_NUMBER, TWILIO_VERIFIED_NUMBER

class NotificationManager:
    
    def __init__(self) -> None:
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def sendSMS(self, message):
        message = self.client.messages \
                .create(
                     body=message,
                     from_=TWILIO_VIRTUAL_NUMBER,
                     to=TWILIO_VERIFIED_NUMBER
                 )

        print(message.sid)
