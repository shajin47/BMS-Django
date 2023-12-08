from django.core.mail import send_mail


def sendMail(email, subject, message):

    subject = subject
    message = message
    email_from = 'shajinrj145@gmail.com'
    recipient = [email]
    res = send_mail( subject, message, email_from, recipient)
    return res