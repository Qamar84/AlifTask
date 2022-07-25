import smtplib
from twilio.rest import Client


def send_email(adder_to, msg_subj, msg_text):
    adder_from = "???"  # Отправитель
    password = "???"  # Пароль
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.ehlo()
    try:
        server.login(adder_from, password)
        server.sendmail(adder_from, adder_to, f'Subject:{msg_subj}\n{msg_text}')
        server.quit()
        return 'Sent email'
    except Exception as e:
        return e


def send_sms(num, text):
    try:
        client = Client('???', '???')
        client.messages.create(from_='+18177830127', to=num, body=text)
        return 'Sent sms'
    except Exception as e:
        return e

