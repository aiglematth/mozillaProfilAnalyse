#Auteur --> aiglematth

#Imports
from sqlite3 import *
import json

#Exceptions
class ConnectException(Exception):
	"""
	Exception levée quand on ne peut pas ouvrir un .sqlite avec la méthode connect
	"""
	def __init__(self, name):
		"""
		Constructeur de la classe
		:param name: Le nom du fichier qui génère l'erreur
		"""
		self.name = name
		Exception.__init__(self)

	def __str__(self):
		return f"open({self.name}) --> Fichier innexistant ou innaccessible"

#Classes
class Analyse():
	"""
	Cette classe permet de simplifier la gestion d'un fichier sqlite
	"""
	def __init__(self, filename):
		"""
		Constructeur de la classe
		:param filename: Le nom du fichier avec lequel interagir
		"""
		self.filename = filename
		try:
			with open(self.filename, "r") as f:
				pass
		except:
			raise ConnectException(self.filename)
		self.db = connect(self.filename)
		self.cursor = self.db.cursor()

	"""
	On va implémenter le with 
	"""
	def __enter__(self):
		"""
		with a() as f:
			pass
		--> with a() execute en vrai f = a().__enter__()
		"""
		return self

	def __exit__(self, *params):
		"""
		Destructeur de la classe
		"""
		self.db.close()

	def select(self, req):
		"""
		On simplifie le retour d'un SELECT
		:param req: La requête SQL
		:return:    Une liste de réponses
		"""
		self.cursor.execute(req)
		return self.cursor.fetchall()

	def insert(self, req):
		"""
		On simplifie le retour d'un INSERT
		:param req: La requête SQL
		"""
		self.cursor.execute(req)
		self.db.commit()

class AnalysePlaces(Analyse):
	"""
	Classe fille de Analyse, permet d'analyser un fichier places.sqlite
	"""
	def __init__(self, filename="places.sqlite"):
		"""
		Constructeur de la classe
		:param filename: Le nom du fichier à analyser
		"""
		Analyse.__init__(self, filename)

	def showHistory(self):
		"""
		Permet de retourner l'historique au format json
		"""
		ret = {
			"url"   : [],
			"title" : []
		}
		req = "SELECT url,title FROM moz_places;"
		
		for (url, title) in self.select(req):
			ret["url"].append(url)
			ret["title"].append(title)

		return json.dumps(ret)

	def showPlaces(self):
		"""
		Retourne le contenu de la table moz_places en format json
		:return: String au format json
		"""
		dico = {
			"id"         : [],
			"url"        : [],
			"title"      : [],
			"rev_host"   : [],
			"visit_coun" : [],
			"hidden"     : [],
			"typed"      : [],
			"frecency"   : [],
			"last_visit" : [],
			"guid"       : [],
			"foreign_co" : [],
			"url_hash"   : [],
			"descriptio" : [],
			"previem_im" : [],
			"origin_id"  : []
		}
		req = "SELECT * FROM moz_places;"
		
		for (id, url, title, rev_host, visit_coun, hidden, typed, frecency, last_visit, guid, foreign_co, url_hash, descriptio, previem_im, origin_id) in self.select(req):
			dico["id"].append(id)
			dico["url"].append(url)
			dico["title"].append(title)
			dico["rev_host"].append(rev_host)
			dico["visit_coun"].append(visit_coun)
			dico["hidden"].append(hidden)
			dico["typed"].append(typed)
			dico["frecency"].append(frecency)
			dico["last_visit"].append(last_visit)
			dico["guid"].append(guid)
			dico["foreign_co"].append(foreign_co)
			dico["url_hash"].append(url_hash)
			dico["descriptio"].append(descriptio)
			dico["previem_im"].append(previem_im)
			dico["origin_id"].append(origin_id)
		
		return json.dumps(dico)

class AnalyseCookies(Analyse):
	"""
	Classe fille de Analyse, permet d'analyser un fichier places.sqlite
	"""
	def __init__(self, filename="cookies.sqlite"):
		"""
		Constructeur de la classe
		:param filename: Le nom du fichier à analyser
		"""
		Analyse.__init__(self, filename)

	def showCookies(self):
		"""
		Retourne le contenu de la table moz_cookies en format json
		:return: String au format json
		"""
		dico = {
			"id"               : [],
			"originAttributes" : [],
			"name"             : [],
			"value"            : [],
			"host"             : [],
			"path"             : [],
			"expiry"           : [],
			"lastAccessed"     : [],
			"creationTime"     : [],
			"isSecure"         : [],
			"isHttpOnly"       : [],
			"inBrowserElement" : [],
			"sameSite"         : [],
			"rawSameSite"      : [],
			"schemeMap"        : []
		}
		req = "SELECT * FROM moz_cookies;"
		
		for (id, originAttributes, name, value, host, path, expiry, lastAccessed, creationTime, isSecure, isHttpOnly, inBrowserElement, sameSite, rawSameSite, schemeMap) in self.select(req):
			dico["id"].append(id)
			dico["originAttributes"].append(originAttributes)
			dico["name"].append(name)
			dico["value"].append(value)
			dico["host"].append(host)
			dico["path"].append(path)
			dico["expiry"].append(expiry)
			dico["lastAccessed"].append(lastAccessed)
			dico["creationTime"].append(creationTime)
			dico["isSecure"].append(isSecure)
			dico["isHttpOnly"].append(isHttpOnly)
			dico["inBrowserElement"].append(inBrowserElement)
			dico["sameSite"].append(sameSite)
			dico["rawSameSite"].append(rawSameSite)
			dico["schemeMap"].append(schemeMap)
		
		return json.dumps(dico)

	def showEssentialCookies(self):
		"""
		Retourne le contenu de la table moz_cookies en format json, sans les champs un peu inutiles
		:return: String au format json
		"""
		dico = {
			"name"             : [],
			"value"            : [],
			"host"             : [],
			"path"             : [],
			"expiry"           : [],
			"lastAccessed"     : [],
			"creationTime"     : [],
		}
		req = "SELECT name, value, host, path, expiry, lastAccessed, creationTime FROM moz_cookies;"
		
		for (name, value, host, path, expiry, lastAccessed, creationTime) in self.select(req):
			dico["name"].append(name)
			dico["value"].append(value)
			dico["host"].append(host)
			dico["path"].append(path)
			dico["expiry"].append(expiry)
			dico["lastAccessed"].append(lastAccessed)
			dico["creationTime"].append(creationTime)
		
		return json.dumps(dico)

	