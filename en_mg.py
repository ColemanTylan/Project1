from twilio.rest import Client

#Account SID and Auth Token from twilio.com/console
account_sid = '***'
auth_token = '***'
client = Client(account_sid, auth_token)

# Sending the message
message = client.messages \
                .create(
                     body="Hello from Python",
                     from_='your_twilio_number',
                     to='recipient_number'
                 )

print(message.sid)