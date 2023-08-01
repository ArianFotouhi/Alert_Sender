from twilio.rest import Client

def send_sms_alert(body):
    account_sid = ''
    auth_token = ''
    twilio_phone_number = '+1...'  # your Twilio phone number
    recipient_phone_number = '+1438...'  # recipient's phone number

    try:
        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Send the SMS
        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )

        print("SMS sent successfully! SID:", message.sid) #message.sid is like unqiue id of an SMS
    except Exception as e:
        print("Error sending SMS:", e)

# Example usage: Call this function when an alert occurs
alert_body = "Hi, this is a test alert!"

user_demand = input('Do you want to send a alert? (y/n):')
if user_demand == 'y':
    send_sms_alert(alert_body)
else:
    print('Ok so alert is sent')