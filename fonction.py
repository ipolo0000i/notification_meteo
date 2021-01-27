from datetime import datetime

def lienfichier(ladate):	
	jour = str(ladate.day).rjust(2, "0")
	mois = str(ladate.month).rjust(2, "0")
	annee = str(ladate.year)
	return f"/apps/weather/weather_data/raw/{annee}/{annee}-{mois}/{annee}-{mois}-{jour}.txt"
		
def comptage(liste):
	#a changer de place
	setliste = set(liste)
	liste_pond = []
	for x in setliste:
		a = liste.count(x)
		liste_pond.append((x,a))
	liste_pond = sorted(liste_pond, key=lambda tup: tup[1], reverse=True)
	return liste_pond[0][0]
def vent(var):
	dico = {'s' : 'SUD',
			'sse' : 'SUD-EST',
			'se' : 'SUD-EST',
			'ese' : 'SUD-EST',
			'so' : 'SUD-OUEST',
			'sso' : 'SUD-OUEST',
			'oso' : 'SUD-OUEST',
			'n' : 'NORD',
			'ne' : 'NORD-EST',
			'ene' : 'NORD-EST',
			'nne' : 'NORD-EST',
			'no' : 'NORD-OUEST',
			'ono' : 'NORD-OUEST',
			'nno' : 'NORD-OUEST',
			'o' : 'OUEST',
			'e' : 'EST',
	}
	return dico[var]

def maxheure(temps, donnee):
	a = ""
	result = []
	liste = []
	for i in range(len(temps)):
		if a != temps[i].hour:
			if i:
				result.append((a, max(liste)))
			a = temps[i].hour
			liste = [donnee[i]]
		else:
			liste.append(donnee[i])
	result.append((a, max(liste)))
	return result
def sumheure(temps, donnee):
	a = ""
	result = []
	liste = []
	for i in range(len(temps)):
		if a != temps[i].hour:
			if i:
				result.append((a, sum(liste)))
			a = temps[i].hour
			liste = [donnee[i]]
		else:
			liste.append(donnee[i])
	result.append((a, sum(liste)))
	return result
def liste_heure(temps):
	l = []
	lh = []
	l.append(datetime.strptime(temps[0].strftime("%d/%m/%y %H"), "%d/%m/%y %H"))
	lh.append(temps[0].hour)
	for i in temps:
		if i.hour != l[-1].hour:
			l.append(datetime.strptime(i.strftime("%d/%m/%y %H"), "%d/%m/%y %H"))
	return l