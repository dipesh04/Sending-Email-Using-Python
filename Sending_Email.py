import smtplib    
import getpass    
from email.mime.text import MIMEText

def send_email():

    sender_address = 'sender email address '
    password = getpass.getpass()
    subject = 'Test Mail'
    msg = '''
        Hello!!
        This is a Test mail

        Thank you!
    '''

    # Server Initialisation

    # For Gmail host = 'smtp.gmail.com', port = 587
    # For Yahoo host = 'smtp.mail.yahoo.com', port = 465 or port = 587
    # For Outlook host = 'smtp-mail.outlook.com', port = 587

    #create smtp object for connection with the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()          
    server.login(sender_address, password)

    # Write here all the receivers email address like
    recipients = ['xyz@gmail.com', 'abc@gmail.com',...]


    # Draft my message body
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = ", ".join(recipients)
    

    server.sendmail(sender_address, recipients, msg.as_string())

send_email()
