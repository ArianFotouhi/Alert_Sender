import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from credentials import sender_email_add, sender_email_pass, recipient_email_add

def send_email_alert(subject, body):
    sender_email = sender_email_add  #your email address eg 'foo@example.com'
    sender_password = sender_email_pass      #your email password eg '123'

    recipient_email = recipient_email_add  #recipient's email address eg 'foo2@example.com'

    # Create a message object
    msg = MIMEMultipart('alternative')
    html = """\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        Don't Worry<br>
        It is just a test alert using the code <a href="https://github.com/ArianFotouhi/Alert_Sender/blob/master/email_sender.py">link</a>.
        </p>
    </body>
    </html>
    """

    part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')


    msg.attach(part1)
    msg.attach(part2)

    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:

        #gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server and port
        #yahoo
        # server = smtplib.SMTP('smtp.mail.yahoo.com', 587)  # Yahoo SMTP server and port

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
alert_subject = "ALERT: just a test though!"
alert_body = "This is a test alert"

send_email_alert(alert_subject, alert_body)
