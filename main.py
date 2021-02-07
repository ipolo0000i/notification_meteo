import bilan
import meteociel
import mail
import signal
import config



#excecution
prev = meteociel.meteociel(config.lien_meteociel)
le_bilan = bilan.bilan()
le_bilan.graph()
#email = mail.mail(le_bilan, meteo, config.e_mail)
signal.envoyer(le_bilan, prev, config.station)
print('ok')

