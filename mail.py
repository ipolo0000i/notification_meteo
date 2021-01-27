import json
import smtplib
from email.message import EmailMessage
from datetime import date
from email.utils import make_msgid

class mail():
	def __init__(self, bilan, previ, e_mail):
		msg = EmailMessage()
		msg['Subject'] = 'Bilan météo'
		msg['From'] = 'adresse@gmail.com'
		msg['To'] = e_mail
		msg.set_content('bulletin météo')
		asparagus_cid = make_msgid()
		cid = 'cid:{asparagus_cid}'
		with open('/home/pi/meteo_mail/meteo.html', 'r', encoding='utf8') as fichier:
			messagehtml = fichier.read()
		compiled_fstring = compile(messagehtml, '<messagehtml>', 'eval')
		messagehtml = eval(compiled_fstring)
		msg.add_alternative(messagehtml.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
		with open("out.png", 'rb') as img:
			msg.get_payload()[1].add_related(img.read(), 'image', 'png', cid=asparagus_cid)
		mailserver = smtplib.SMTP('smtp.gmail.com', 587)
		mailserver.ehlo()
		mailserver.starttls()
		mailserver.ehlo()
		mailserver.login('adresse@gmail.com', 'motdepasse')
		mailserver.send_message(msg)
		mailserver.quit()
	