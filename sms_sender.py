from twilio.rest import Client

def send_sms_alert(body):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    twilio_phone_number = '+1...'  # your Twilio phone number
    recipient_phone_number = '+1...'  # recipient's phone number

    try:
        # Create a Twilio client
        client = Client(account_sid, auth_token)

        # Send the SMS
        message = client.messages.create(
            body=body,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )

        print("SMS sent successfully! SID:", message.sid)
    except Exception as e:
        print("Error sending SMS:", e)

# Example usage: Call this function when an alert occurs
alert_body = "ALERT: Something went wrong! Please take immediate action."

send_sms_alert(alert_body)
