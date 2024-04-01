##THIS THING IS NOT WORKING!!
import smtplib

HOST = 'smtp.gmail.com'
SUBJECT = 'Test email from Python'
TO = 'razninja007@gmail.com'
FROM = 'rraz639@gmail.com'
text = 'bla bla bla'
BODY = '\r\n'.join((
    f'From: {FROM}',
    f'To: {TO}',
    f'Subject: {SUBJECT}',
    '',
    text))
server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()