from datetime import date
from datetime import timedelta
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as pltdate
import fonction


class bilan():
	def __init__(self):
		lien_fichier = fonction.lienfichier(date.today())
		lien_fichier_1 = fonction.lienfichier(date.today() - timedelta(days=1))
		self.l_date = []
		self.l_temp = []
		self.l_v_raff = []
		self.l_v_dir = []
		self.l_pluie = []
		self.l_hygro = []
		with open(lien_fichier, 'r', encoding='utf8') as fichier:
			with open(lien_fichier_1, 'r', encoding='utf8') as fichier_1:
				for line_1 in fichier_1:
					date_veille = datetime.strptime(line_1.split(',')[0], "%Y-%m-%d %X")
					if int(date_veille.strftime("%H")) >= datetime.now().hour - 2:
						self.record_line(line_1)
					else:
						self.a = float(line_1.split(',')[10])
				for line in fichier:
					self.record_line(line)
		self.l_date = [x + timedelta(hours=2) for x in self.l_date]
		self.t_max = max(self.l_temp)
		self.ht_max = self.l_date[self.l_temp.index(self.t_max)].strftime("%Hh")
		self.t_min = min(self.l_temp)
		self.ht_min = self.l_date[self.l_temp.index(self.t_min)].strftime("%Hh")
		self.v_max = max(self.l_v_raff)
		self.hv_max = self.l_date[self.l_v_raff.index(self.v_max)].strftime("%Hh")
		self.v_dir = fonction.comptage(self.l_v_dir)
		self.pluie_c = sum(self.l_pluie)
		self.hygro_max = max(self.l_hygro)
		self.hygro_min = min(self.l_hygro)
	def record_line(self, line):
		try:
			self.l_temp.append(round(float(line.split(',')[5]),1))
			self.l_pluie.append(round(float(line.split(',')[10]) - self.a, 1))
			self.a = round(float(line.split(',')[10]),1)
			self.l_date.append(datetime.strptime(line.split(',')[0], "%Y-%m-%d %X"))
			self.l_v_raff.append(round(float(line.split(',')[8]) * 3.6, 1))
			self.l_hygro.append(int(line.split(',')[4]))
			winddir_text_array = ('NORD', 'NORD-EST', 'NORD-EST', 'NORD-EST', 'EST', 'SUD-EST', 'SUD-EST', 'SUD-EST','SUD', 'SUD-OUEST', 'SUD-OUEST', 'SUD-OUEST', 'OUEST', 'NORD-OUEST', 'NORD-OUEST', 'NORD-OUEST')
			if line.split(',')[9] == '':
				self.l_v_dir.append(0)
			else:
				self.l_v_dir.append(winddir_text_array[int(line.split(',')[9])])
		except:
			self.a = self.a
	def __str__(self):
		retour = f"""Bilan de la journée :
Température maximale : {self.t_max}°C à {self.ht_max}
Vitesse du vent maximale : {self.v_max}km/h à {self.hv_max}
Direction des vents dominants : {self.v_dir}
Cumul des pluies : {self.pluie_c}mm"""
		return retour
	def test(self):
		return fonction.liste_heure(self.l_date)
	def graph(self):
		max_temp = fonction.maxheure(self.l_date, self.l_temp)
		max_vent = fonction.maxheure(self.l_date, self.l_v_raff)
		sum_pluie = fonction.sumheure(self.l_date, self.l_pluie)
		dates = fonction.liste_heure(self.l_date)
		dates = [i.strftime("%d-%H") for i in dates]
		plts =[]
		plts.append(plt.plot(dates, [x[1] for x in max_temp]))
		plts.append(plt.plot(dates, [x[1] for x in max_vent]))
		plts.append(plt.bar(dates, [x[1] for x in sum_pluie]))
		plt.legend([x[0] for x in plts], ['température', 'vent', 'pluie'])
		plt.xticks(rotation=50)
		plt.savefig("out.png")
		

