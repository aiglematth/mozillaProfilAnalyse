#Auteur --> aiglematth

#Imports
from argparse   import *
from analyse    import *
from sys        import exit
from os         import listdir
from getpass    import getuser
from json       import *

#Fonctions
def displayResult(args):
	if args.cookiesAll:
		haveCookies(profil)
		a = AnalyseCookies(f"{profil}/cookies.sqlite")
		if args.humanReadable:
			a = loads(a.showCookies())
			val = list(a.values())

			for key in a.keys():
				print(f"|\t{key}\t|", end="")
			print("")

			for y in range(len(val[0])):
				for x in range(len(val)):
					print(f"|\t{val[x][y]}\t|", end="")
				print("")
		elif args.csv:
			a = loads(a.showCookies())
			val = list(a.values())
			csv = ""

			for key in a.keys():
				csv += f"\"{key}\","
			csv = csv[0:len(csv)-1] + "\n"

			for y in range(len(val[0])):
				for x in range(len(val)):
					csv += f"\"{val[x][y]}\","
				csv = csv[0:len(csv)-1] + "\n"

			print(csv.strip())
		else:
			print(a.showCookies())

	if args.cookiesResume:
		haveCookies(profil)
		a = AnalyseCookies(f"{profil}/cookies.sqlite")
		if args.humanReadable:
			a = loads(a.showEssentialCookies())
			val = list(a.values())

			for key in a.keys():
				print(f"|\t{key}\t|", end="")
			print("")

			for y in range(len(val[0])):
				for x in range(len(val)):
					print(f"|\t{val[x][y]}\t|", end="")
				print("")
		elif args.csv:
			a = loads(a.showEssentialCookies())
			val = list(a.values())
			csv = ""

			for key in a.keys():
				csv += f"\"{key}\","
			csv = csv[0:len(csv)-1] + "\n"

			for y in range(len(val[0])):
				for x in range(len(val)):
					csv += f"\"{val[x][y]}\","
				csv = csv[0:len(csv)-1] + "\n"

			print(csv.strip())
		else:
			print(a.showEssentialCookies())

	if args.historyAll:
		havePlaces(profil)
		a = AnalysePlaces(f"{profil}/places.sqlite")
		if args.humanReadable:
			a = loads(a.showPlaces())
			val = list(a.values())

			for key in a.keys():
				print(f"|\t{key}\t|", end="")
			print("")

			for y in range(len(val[0])):
				for x in range(len(val)):
					print(f"|\t{val[x][y]}\t|", end="")
				print("")
		elif args.csv:
			a = loads(a.showPlaces())
			val = list(a.values())
			csv = ""

			for key in a.keys():
				csv += f"\"{key}\","
			csv = csv[0:len(csv)-1] + "\n"

			for y in range(len(val[0])):
				for x in range(len(val)):
					csv += f"\"{val[x][y]}\","
				csv = csv[0:len(csv)-1] + "\n"

			print(csv.strip())
		else:
			print(a.showPlaces())

	if args.historyResume:
		havePlaces(profil)
		a = AnalysePlaces(f"{profil}/places.sqlite")
		if args.humanReadable:
			a = loads(a.showHistory())
			val = list(a.values())

			for key in a.keys():
				print(f"|\t{key}\t|", end="")
			print("")

			for y in range(len(val[0])):
				for x in range(len(val)):
					print(f"|\t{val[x][y]}\t|", end="")
				print("")
		elif args.csv:
			a = loads(a.showHistory())
			val = list(a.values())
			csv = ""

			for key in a.keys():
				csv += f"\"{key}\","
			csv = csv[0:len(csv)-1] + "\n"

			for y in range(len(val[0])):
				for x in range(len(val)):
					csv += f"\"{val[x][y]}\","
				csv = csv[0:len(csv)-1] + "\n"

			print(csv.strip())			
		else:
			print(a.showHistory())

def chooseProfil():
	path = f"/home/{getuser()}/.mozilla/firefox/"
	dirs = listdir(path)
	good = []

	for d in dirs:
		if "default" in d:
			good.append(d)

	choix = -1
	while choix < 0 or choix >= len(good):
		for i in range(len(good)):
			print(f"[{i}] - [{good[i]}]")
		choix = input("Entrez le profil souhaité : ")
		try:
			choix = int(choix)
		except:
			choix = -1

	return f"{path}{good[choix]}"

def haveCookies(profil):
	try:
		with open(f"{profil}/cookies.sqlite", "r") as f:
			pass
	except:
		print("Pas de fichier cookies.sqlite.")
		exit(-1)

def havePlaces(profil):
	try:
		with open(f"{profil}/places.sqlite", "r") as f:
			pass
	except:
		print("Pas de fichier places.sqlite.")
		exit(-1)

#Main
parser = ArgumentParser(description="Petit outil pour tcheck l'historique/cookies d'un profil mozzila")
parser.add_argument("--profil", type=str, help="Précise le dossier qui contient le profil (souvent de la forme <randomString>.default[-release]")
parser.add_argument("--profilAuto", action="store_true", help="Trouve le dossier qui contient le profil (souvent de la forme <randomString>.default[-release]")
parser.add_argument("--cookiesResume", action="store_true", help="Permet de montrer les données contenues dans les cookies")
parser.add_argument("--cookiesAll", action="store_true", help="Permet de montrer l'intégalité des données contenues dans les cookies")
parser.add_argument("--historyResume", action="store_true", help="Permet de montrer les urls contenues dans l'historique")
parser.add_argument("--historyAll", action="store_true", help="Permet de montrer toutes les données contenues dans l'historique")
parser.add_argument("--humanReadable", action="store_true", help="Permet de montrer le résultat de façon lisible par un humain")
parser.add_argument("--json", action="store_true", help="Permet de montrer le résultat au format json")
parser.add_argument("--csv", action="store_true", help="Permet de montrer le résultat au format csv")

args = parser.parse_args()

profil = ""


if args.profil:
	profil = args.profil
elif args.profilAuto:
	profil = chooseProfil()
else:
	print("Bye...")
	exit(0)

displayResult(args)
