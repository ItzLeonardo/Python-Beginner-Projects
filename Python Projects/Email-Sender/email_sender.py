import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Daud Ahmed'
email['to'] = 'daudahmed36@gmail.com'
email['subject'] = 'Hello! How\'s the weather today?'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('itzleonardo786@gmail.com', '**********')
	smtp.send_message(email)
	print("All Good!")
