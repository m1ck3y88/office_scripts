from datetime import datetime as dt
import email as mail
import app_password
import imaplib
import time

'''
Here we use the built-in imaplib module to check received emails programmatically.
There are many different options for queries that can be written to pull specific 
emails based on some criteria. To see an extensive list of options, check out the 
documentation for the Python imaplib module. In this example, we pull emails for 
the current date and then write part of the data to a text file. I've used the 
built-in time module to time the automation of checking for emails. For the sake
of testing, I've set the script to check for emails every 5 seconds. Of course you
can adjust the script to check at whatever rate is most appropriate for your needs.

Remember that Google requires you to create app password to log into your Gmail 
account programmatically. If you do not already have an app password, you can create 
one by logging into your Google account via the Chrome browser, clicking on your 
profile icon, enabling 2-factor authentication (if you haven't already), then navigate 
to the following URL:

https://myaccount.google.com/apppasswords
'''

while True:

    host = 'imap.gmail.com'
    email = '<YOUR_EMAIL>'
    password = app_password.your_password_here
    # Format date according to the documentation for imapblib module
    formatted_date = dt.now().strftime('%d-%b-%Y')
    # This query will pull emails only for the current date
    query = f'ON {formatted_date}'
    filename = 'todays_emails.txt'
    delay = 5

    M = imaplib.IMAP4_SSL(host)
    M.login(email, password)
    # Select your Inbox
    M.select('inbox')

    typ, data = M.search(None, query)

    todays_emails = len(data[0].split())

    if todays_emails == 1:
        print('\n-----------------------------------\n')
        print(f'You have received {todays_emails} email today.')
        print('-----------------------------------\n')

    else:
        print('\n-----------------------------------')
        print(f'You have received {todays_emails} emails today.')
        print('-----------------------------------\n')

    if len(data[0].split()) > todays_emails:
        remainder = len(data[0].split()) - todays_emails
        todays_emails += remainder

    list_of_emails = []
    email_id = data[0]

    for email in email_id.split():
        result, email_data = M.fetch(email, '(RFC822)')
        raw_email = mail.message_from_bytes(email_data[0][1])

        # Append data to an empty list with each line to write to the text
        # file as an item in a tuple. I've commented out the body of the
        # email to reduce verbosity, but if you want to include that data
        # then simply uncomment the code below.
        list_of_emails.append((
            '-----------------------------\n',          # Line 1 (tup[0])
            'From: ' + raw_email['From'] + '\n',        # Line 2 (tup[1])
            'Subject: ' + raw_email['Subject'] + '\n',  # Line 3 (tup[2])
            'Date: ' + raw_email['Date'] + '\n',        # Line 4 (tup[3])
            # 'Body:\n'                                 # Line 5 (tup[4])
            # str(raw_email.get_payload(decode = True)) # Line 6 (tup[5])
            '-----------------------------\n'
        ))

    with open(f'{dt.now().strftime("%b_%d[%Hh][%Mm][%Ss]_")}' + filename, 'a') as file:
        # Unpack tuple and write each item to text file
        for tup in list_of_emails:
            file.write(tup[0]),  # Line 1
            file.write(tup[1]),  # Line 2
            file.write(tup[2]),  # Line 3
            file.write(tup[3]),  # Line 4
            file.write(tup[4]),  # Line 5

    M.close()
    M.logout()
    time.sleep(delay)





