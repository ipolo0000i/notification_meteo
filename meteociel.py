import requests
import re
from bs4 import BeautifulSoup
from datetime import date
import fonction

class meteociel():
	def __init__(self, url):	
		jour_demain = date.today().day + 1
		html = requests.get(url).content
		soup = BeautifulSoup(html, features="html5lib")
		table = soup.find("table", {"bordercolor":"#a0a0b0"})
		heure = []
		temp =[]
		v_dir = []
		v_raf = []
		pluie = []
		temps = []
		for row in table.findAll('tr')[2:]:
			col = row.findAll('td')
			if len(col) == 11:
				tableau_jour = re.split("<br/>", str(col[0]))[1]
				if int(tableau_jour) == int(jour_demain):
					heure.append(col[1].string)
					temp.append(col[2].string)
					img_vent = col[4].find('img')['src']
					img_vent = img_vent.split('/')[-1].split('.')[0]
					v_dir.append(img_vent)
					v_raf.append(col[6].string)
					pluie.append(col[7].string)
					temps.append(col[10].find('img')['alt'])
			else:
				if int(tableau_jour) == int(jour_demain):
					heure.append(col[0].string)
					temp.append(col[1].string)
					img_vent = col[3].find('img')['src']
					img_vent = img_vent.split('/')[-1].split('.')[0]
					v_dir.append(img_vent)
					v_raf.append(col[5].string)
					pluie.append(col[6].string)
					temps.append(col[9].find('img')['alt'])

		heure = [f"{x.split(':')[0]}h" for x in heure]
		self.v_max = max(v_raf)
		self.hv_max = heure[v_raf.index(max(v_raf))]
		self.v_dir = fonction.vent(fonction.comptage(v_dir))
		pluie = [float(re.findall(r'\d+[.]?\d?', x)[0]) for x in pluie if x != "--"]
		self.pluie_c = round(sum(pluie), 1)
		self.ambiance = fonction.comptage(temps)
		temp = [int(re.findall(r'\d+', x)[0]) for x in temp]
		self.t_max = max(temp)
		self.ht_max = heure[temp.index(max(temp))]
		self.t_min = min(temp)
		self.ht_min = heure[temp.index(min(temp))]
		
	def __str__(self):
		retour = f"""Ambiance générale : {self.ambiance}
Température maximale : {self.t_max}°C à {self.ht_max}
Vitesse du vent maximale : {self.v_max}km/h à {self.hv_max}
Direction des vents dominants : {self.v_dir}
Cumul des pluies : {self.pluie_c}mm"""
		return retour			