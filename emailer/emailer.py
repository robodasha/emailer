"""
For sending emails
"""

import smtplib
from email.mime.text import MIMEText

__author__ = 'robodasha'
__email__ = 'damirah@live.com'


def send_email(from_address, copy_address, to_address, fname, subject, text):

    msg = MIMEText(text.replace('(%FIRST-NAME%)', fname))
    msg['Subject'] = subject
    msg['From'] = from_address
    if copy_address is not None and len(copy_address):
        msg['Cc'] = copy_address
    msg['To'] = to_address
    msg.add_header('reply-to', from_address)

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
