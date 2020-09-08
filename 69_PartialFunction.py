import smtplib
import functools


def send_info_email(user, acc_pass, mail_from, mail_to, mail_subject, mail_body):
    message = """From: {}
Subject: {}
{}
""".format(mail_from, mail_subject, mail_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()  # you need to say hello.
        server.login(user, acc_pass)
        server.sendmail(user, mail_to, message)
        server.close()
        print('Mail sent.')
        return True

    except:
        print('Error sending mail')
        return False


with open(r'/home/darek/Projects/send', 'r') as file:
    mail_to = [addresses[:-1] for addresses in file.readlines()]
with open(r'/home/darek/Projects/send_1', 'r') as file:
    acc_pass = file.readline()

mail_from = 'Your automation system'
mail_subject = "Processing finished successfully"
mail_body = '''Hello!!!
This mail confirms that processing has finished without problems.

Have a nice day!!!'''
user = mail_to[0]

send_info_email_gmail = functools.partial(send_info_email, user, acc_pass,
                                          mail_subject="Execution alert")

send_info_email_gmail(mail_from=mail_from, mail_to=mail_to, mail_body=mail_body)

# send_info_email(user, acc_pass, mail_from, mail_to, mail_subject, mail_body)

#  Lab
