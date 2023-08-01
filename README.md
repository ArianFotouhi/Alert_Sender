# Alert Sender app
The repository is created to send an alert (SMS, Email, etc.) in case of an event

Regarding the sent alert using SMS, we are using the Twilio service, which provides an initial credit to start the trial, with paid options available afterward. To use the service, the user needs to obtain credentials, such as the Account SID and Auth Token, from Twilio, as well as a dedicated Twilio phone number. In our app, the event that may trigger an alert is a simple example that prompts the user to send the alert.
To install Twilio:
```bash
pip install twilio 
```
Email sender uses smtplib that can be configured to apply SMTP protocol on gmail (smtplib.SMTP('smtp.gmail.com', 587)), yahoo (smtplib.SMTP('smtp.mail.yahoo.com', 587)), etc., and unlike previous Twilio SMS sender, due to no need to a third party company like Twilio, the service is free of charge.

It should be noted, on May 30, 2022 Google has restricted the access to gmail using a third party app like ours ([Link]([https://support.google.com/accounts/answer/6010255?hl=en)). Therefore, the user has to create app password (2 step verification should be enable prior to that). Here is the link to create app password as well as a video:
[Google Link](https://support.google.com/accounts/answer/6010255?hl=en)
Lastly, instead of smtplib, other options like yagmail can be employed as well by:
```bash
pip install yagmail
```
