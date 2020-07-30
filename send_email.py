import config
import smtplib
import password

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()

        server.login(config.FROM, password.PASSWORD)
        message = 'Subject: {}\n\n {}'.format(subject, msg)
        server.sendmail(config.FROM, config.TO, message)
        server.quit()
        print("Message sent succesfully.")
    except:
        print("Failure to send email.")


def send_thread(subject, msg):
    send_email(subject, msg)
