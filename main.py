import bilan
import meteociel
import mail
#configuration
e_mail = 'email@gmail.com'
lien_meteociel = 'https://www.meteociel.fr/previsions/25600/grigny.htm'


#excecution
meteo = meteociel.meteociel(lien_meteociel)
le_bilan = bilan.bilan()
le_bilan.graph()
email = mail.mail(le_bilan, meteo, e_mail)
print('ok')

