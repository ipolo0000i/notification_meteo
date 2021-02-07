import requests as rq

def envoyer(bilan, prev, station):
	message = f"""Bilan météo {station}
		• Température maxi :{bilan.t_max}°C à {bilan.ht_max}
		• Température mini : {bilan.t_min}°C à {bilan.ht_min}
		• Hygrométrie maxi/mini : {bilan.hygro_max}%/{bilan.hygro_min}%
		• Vitesse vent maxi : {bilan.v_max} km/h à {bilan.hv_max}
		• Direction du vent : {bilan.v_dir}
		• Cumul pluviométrie : {bilan.pluie_c}mm

	Prévision pour {station}
		• Ambiance générale : {prev.ambiance}
		• Température maxi :{prev.t_max}°C à {prev.ht_max}
		• Température mini : {prev.t_min}°C à {prev.ht_min}
		• Vitesse vent maxi : {prev.v_max} km/h à {prev.hv_max}
		• Direction du vent : {prev.v_dir}
		• Cumul pluviométrie : {prev.pluie_c} mm
	"""
	file = {'file': open('out.png','rb')}
	r = rq.post("http://chezpolo.eu:8080/send/", data={"data" : message}, files = file)
