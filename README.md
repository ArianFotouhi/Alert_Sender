# Alert Sender app
The repository is created to send an alert (SMS, Email, etc.) in case of an event

Regarding the sent alert using SMS, we are using the Twilio service, which provides an initial credit to start the trial, with paid options available afterward. To use the service, the user needs to obtain credentials, such as the Account SID and Auth Token, from Twilio, as well as a dedicated Twilio phone number. In our app, the event that may trigger an alert is a simple example that prompts the user to send the alert.
To install Twilio:
```bash
pip install twilio 
```



Email sender uses smtplib, which can be configured to apply the SMTP protocol on services like Gmail (smtplib.SMTP('smtp.gmail.com', 587)), Yahoo (smtplib.SMTP('smtp.mail.yahoo.com', 587)), and others. Unlike the previous Twilio SMS sender, this email service is free of charge as it doesn't require a third-party company like Twilio.

It should be noted that, on May 30, 2022, Google restricted access to Gmail using third-party apps like ours. Therefore, users need to create an app password, and 2-step verification should be enabled prior to that. Here is the link to create an app password, along with a video guide:
[Google Link](https://support.google.com/accounts/answer/6010255?hl=en)

Lastly, instead of smtplib, other options like yagmail can be employed as well by:
```bash
pip install yagmail
```
