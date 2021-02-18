import smtplib

mail_from = 'Your automation system'

with open(r'/home/darek/Projects/send', 'r') as file:
    mail_to = [addresses[:-1] for addresses in file.readlines()]
with open(r'/home/darek/Projects/send_1', 'r') as file:
    acc_pas = file.readline()

mail_subject = 'Processing finished successfully'

mail_body = '''Hello
This mail confirms that processing has finished without problems.

Have a nice day!!!'''

message = f"""From: {mail_from}
Subject: {mail_subject}
{mail_body}"""

user = mail_to[0]

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()  # you need to say hello.
    server.login(user, acc_pas)
    server.sendmail(user, mail_to, message)
    server.close()
    print('Mail sent.')
except:
    print('Error sending mail')
