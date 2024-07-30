import app_password
import smtplib

"""
This script uses Python's built-in smtplib module to send emails programmatically.
In this example, we use Google's Gmail SMTP server as it is the most widely used email service.
Google has its own free Gmail API, which provides more intuitive interaction and a better overall user
experience, however, it is always best to first learn how to use Python's built-in modules just in case 
third-party modules/APIs are down or unavailable. Keep in mind that Google requires you to create an 
app password to log into your Gmail account programmatically. If you do not already have an app password, 
you can create one by logging into your Google account via the Chrome browser, clicking on your profile 
icon, enabling 2-factor authentication (if you haven't already), then navigate to the following URL:

https://myaccount.google.com/apppasswords

The functionality of this code may not necessarily be useful in a real-world scenario, but the 
concepts are applicable to any real-world office environment, as well as everyday life. I would advise 
sending emails to yourself when testing this code. This script generates five emails and sends them to 
the email address of your choosing.
"""
host = 'smtp.gmail.com'
email = '<SEND_ADDRESS>'
password = app_password.your_password_here
to_address = '<TO_ADDRESS>'
subject = ''
body = ''

# Define function for generating and sending emails
def main(host, email, password, to_address, body, subject=''):
    """
    Connects to SMTP server and sends email.
    :param host:  A string representing the SMTP server host.
    :param email: A string representing the sender's email address.
    :param password: A string representing the sender's password.
    :param to_address: A string representing the receiver's email address.
    :param subject: A string representing the subject line. Default is an empty string.
    :param body: A string representing the body of the email.
    """
    smtp_object = smtplib.SMTP(host, 587)
    smtp_object.ehlo()
    smtp_object.starttls()
    smtp_object.login(email, password)
    msg = "Subject: " + subject + "\n" + body
    smtp_object.sendmail(email, to_address, msg)
    smtp_object.quit()


# Generate five email subject and body lines for testing
for i in range(5):

    if i == 0:
        subject = f'This Is The {str(i + 1)}st Test Message'
        body = f'This is the {str(i + 1)}st test message sent using Python'
    elif i == 1:
        subject = f'This Is The {str(i + 1)}nd Test Message'
        body = f'This is the {str(i + 1)}nd test message sent using Python'
    elif i == 2:
        subject = f'This Is The {str(i + 1)}rd Test Message'
        body = f'This is the {str(i + 1)}rd test message sent using Python'
    else:
        subject = f'This Is The {str(i + 1)}th Test Message'
        body = f'This is the {str(i + 1)}th test message sent using Python'

    # Generate and send the email
    main(host, email, password, to_address, body, subject)
