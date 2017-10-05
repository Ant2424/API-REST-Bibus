#!/usr/bin/env python3
# coding: utf-8
__author__ = "Antoine Auffret"
__version__ = "1.3"
__source__ = "https://geo.pays-de-brest.fr/donnees/Documents/Public/DocWebServicesTransport.pdf"

import requests
import urllib
import json

class Bibus():
	# Initialisation de l'url de base et du format de données retour
	def __init__(self, base_url, output_format):
		self.base_url = base_url
		self.output_format = output_format

	# Appel du module requests et renvoie les données en json
	def __request(self, url):
		r = requests.get(url)
		return json.dumps(r.json(), indent=4, sort_keys=True, ensure_ascii=False)

	# Obtenir la version de l'application
	def getVersion(self):
		url = "%s%s?format=%s" % (base_url, "getVersion", output_format)
		return self.__request(url)

	# Obtenir le nom de tous les arrêts
	def getStopsNames(self):
		url = "%s%s?format=%s" % (base_url, "getStopsNames", output_format)
		return self.__request(url)

	# Obtenir toutes les lignes
	def getRoutes(self):
		url = "%s%s?format=%s" % (base_url, "getRoutes", output_format)
		return self.__request(url)

	# Obtenir les arrêts d'une ligne
	def getStops_route(self, route_id, trip_headsign):
		param = "route_id=%s&trip_headsign=%s" % (route_id, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getStops_route", output_format, param)
		return self.__request(url)

	# Obtenir un arrêt
	def getStop(self, stop_name):
		param = "stop_name=%s" % (stop_name)
		url = "%s%s?format=%s&%s" % (base_url, "getStop", output_format, param)
		return self.__request(url)

	# Obtenir un arrêt
	def getStop2(self, stop_id):
		param = "stop_id=%s" % (stop_id)
		url = "%s%s?format=%s&%s" % (base_url, "getStop2", output_format, param)
		return self.__request(url)

	# Obtenir toutes les lignes desservant un arrêt
	def getRoutes_stop(self, stop_name):
		param = "stop_name=%s" % (stop_name)
		url = "%s%s?format=%s&%s" % (base_url, "getRoutes_stop", output_format, param)
		return self.__request(url)

	# Obtenir toutes les lignes desservant un arrêt
	def getRoutes_stop2(self, stop_id):
		param = "stop_id=%s" % (stop_id)
		url = "%s%s?format=%s&%s" % (base_url, "getRoutes_stop2", output_format, param)
		return self.__request(url)

	# Obtenir les noms des destinations
	def getDestinations(self, route_id):
		param = "route_id=%s" % (route_id)
		url = "%s%s?format=%s&%s" % (base_url, "getDestinations", output_format, param)
		return self.__request(url)

	# Obtenir les arrêts les plus proches
	def getStopsNear(self, latitude, longitude):
		param = "latitude=%s&longitude=%s" % (latitude, longitude)
		url = "%s%s?format=%s&%s" % (base_url, "getStopsNear", output_format, param)
		return self.__request(url)

	# Obtenir l'arrêt le plus proche pour une ligne
	def getStopNear_route(self, route_id, latitude, longitude):
		param = "route_id=%s&latitude=%s&longitude=%s" % (route_id, latitude, longitude)
		url = "%s%s?format=%s&%s" % (base_url, "getStopNear_route", output_format, param)
		return self.__request(url)

	# Obtenir la position (arrêt) des véhicules (bus ou tramway)
	def getStopVehiclesPosition(self, route_id, trip_headsign):
		param = "route_id=%s&trip_headsign=%s" % (route_id, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getStopVehiclesPosition", output_format, param)
		return self.__request(url)

	# Obtenir la position (géographique) des véhicules
	def getGeolocatedVehiclesPosition(self, route_id, trip_headsign):
		param = "route_id=%s&trip_headsign=%s" % (route_id, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getGeolocatedVehiclesPosition", output_format, param)
		return self.__request(url)

	# Obtenir les horaires des prochains départs
	def getNextDepartures(self, route_id, stop_name, trip_headsign):
		param = "route_id=%s&stop_name=%s&trip_headsign=%s" % (route_id, stop_name, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getNextDepartures", output_format, param)
		return self.__request(url)

	# Obtenir les horaires des prochains départs
	def getNextDepartures2(self, route_id, stop_id, trip_headsign):
		param = "route_id=%s&stop_id=%s&trip_headsign=%s" % (route_id, stop_id, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getNextDepartures2", output_format, param)
		return self.__request(url)

	# Obtenir les temps d'attente avant les prochains passages
	def getRemainingTimes(self, route_id, stop_name, trip_headsign):
		param = "route_id=%s&stop_name=%s&trip_headsign=%s" % (route_id, stop_name, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getRemainingTimes", output_format, param)
		return self.__request(url)

	# Obtenir les temps d'attente avant les prochains passages
	def getRemainingTimes2(self, route_id, stop_id, trip_headsign):
		param = "route_id=%s&stop_id=%s&trip_headsign=%s" % (route_id, stop_id, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getRemainingTimes2", output_format, param)
		return self.__request(url)

	# Obtenir les déviations
	def getDeviations(self, route_id, trip_headsign):
		param = "route_id=%s&trip_headsign=%s" % (route_id, trip_headsign)
		url = "%s%s?format=%s&%s" % (base_url, "getDeviations", output_format, param)
		return self.__request(url)

	# Obtenir les perturbations
	def getPerturbations(self):
		url = "%s%s?format=%s" % (base_url, "getPerturbations", output_format)
		return self.__request(url)

if __name__ == '__main__':
	# Initialisation
	base_url = "https://applications002.brest-metropole.fr/WIPOD01/Transport/REST/"
	output_format = "json"
	api = Bibus(base_url, output_format)

	stop_name = "ISEN"
	stop_id = "ISEN_2"
	route_id = "6"
	latitude = "48.407011"
	longitude = "-4.495557"
	trip_headsign = urllib.parse.quote("Clin Keraudren")

	##### Données statiques #####
	#print(api.getVersion())
	#print(api.getStopsNames())
	#print(api.getRoutes())
	#print(api.getStops_route(route_id, trip_headsign))
	#print(api.getStop(stop_name))
	#print(api.getStop2(stop_id))
	#print(api.getRoutes_stop(stop_name))
	#print(api.getRoutes_stop2(stop_id))
	#print(api.getDestinations(route_id))

	##### Données dynamiques et temps réel #####
	#print(api.getStopsNear(latitude, longitude))
	#print(api.getStopNear_route(route_id, latitude, longitude))
	#print(api.getStopVehiclesPosition(route_id, trip_headsign))
	#print(api.getGeolocatedVehiclesPosition(route_id, trip_headsign))
	#print(api.getNextDepartures(route_id, stop_name, trip_headsign))
	#print(api.getNextDepartures2(route_id, stop_id, trip_headsign))
	#print(api.getRemainingTimes(route_id, stop_name, trip_headsign))
	#print(api.getRemainingTimes2(route_id, stop_id, trip_headsign))
	#print(api.getDeviations(route_id, trip_headsign))
	#print(api.getPerturbations())
