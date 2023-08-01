import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body):
    sender_email = 'your_sender_email@gmail.com'  #your email address
    sender_password = 'your_sender_password'      #your email password

    recipient_email = 'recipient@example.com'  #recipient's email address

    # Create a message object
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server and port
        server.starttls()

        # Log in to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the connection
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

# Example 
alert_subject = "ALERT: Something went wrong!"
alert_body = "There was an issue detected. Please take immediate action."

send_email_alert(alert_subject, alert_body)
