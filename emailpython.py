import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Latesh Kakrai'
email['to'] = 'enter the email id'
email['subject'] = 'write your subject here'

email.set_content('enter your content')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('enter your email id ', 'enter your password')
  smtp.send_message(email)

  