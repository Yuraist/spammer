# library for working with SMTP (Simple Mail Transport Protocol)
import smtplib

# imports for add text and images to the message
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# import header to make utf-8 headers available
from email.header import Header
from datetime import datetime

# to join the recipients
COMMASPACE = ', '


# create a message
def create_message(recipient):
    message = MIMEMultipart()

    # create a subject and from
    message['Subject'] = Header('INSERT_YOUR_HEADER_HERE', 'utf-8')
    message['From'] = 'SENDER_NAME'
    message['To'] = recipient

    # open an image
    with open('YOUR_FILE_ADDRESS', 'rb') as image_file:
        image = MIMEImage(image_file.read())

    # create an html text
    html = """
    <html>
      <head></head>
      <body>
                INSERT_HTML_CODE_HERE
      </body>
    </html>
    """

    # create an html instance for email message
    html_attachment = MIMEText(html, 'html')

    # attach the image and html
    message.attach(html_attachment)
    message.attach(image)

    # return the message ready for sending
    return message


def send_message(message, need_alert):
    # connect to email server
    # THIS SETTINGS IS FOR GMAIL
    my_smtp = smtplib.SMTP('smtp.gmail.com', 587)

    # encryption with TSL (Transport Layer Security)
    my_smtp.starttls()

    # auth
    sender_email_address = 'YOUR_ADDRESS@gmail.com'
    sender_password = 'YOUR_PASSWORD_FROM_EMAIL_ABOVE'
    my_smtp.login(sender_email_address, sender_password)

    # send a message
    my_smtp.send_message(message)

    # alert when the message was sent if needed
    if need_alert:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second

        time = '%s: %s: %s .' % (hour, minute, second)
        user = message["To"]
        print("The message has sent to %s \nAt %s" % (user, time))

    # quit the email server
    my_smtp.quit()


# open database from source (address of file with db) and get users from it
# return a list of users
def get_users(source):
    with open(source, 'r') as db:
        users = []
        for user in db:
            users.append(user)

        # alert about successful appending
        print('%s users were appended.' % (len(users)))

        # return list of users
        return users
