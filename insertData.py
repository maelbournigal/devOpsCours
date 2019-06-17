#Import des modules nécessaires
import mysql.connector as mariadb
import glob
import os
import json

#Récupération de la liste de fichiers
list_of_files = glob.glob('*') # * means all if need specific format then *.csv

#Récupération du dernier fichier cr��
latest_file = max(list_of_files, key=os.path.getctime)

#Connexion à la base de données
mariadb_connection = mariadb.connect(host='192.168.213.128', port=3306, user='devops', password='bournigal', database='TPDevOps')

#Création du curseur pour exécuter des requetes
cursor = mariadb_connection.cursor()

#Récupération des données du fichier json
with open(latest_file) as json_file:  
	data = json.load(json_file)
	#Pour chaque mesure, insertion des données dans la base
	for p in data['mesure']:
		if (p['numUnite'] >= 1 and p['numUnite'] <= 5 and p['numAutomate'] >= 1 and p['numAutomate'] <= 10 and p['tempCuve'] >= 2.5 and p['tempCuve'] <= 4 and p['tempExterieure'] >= 8 and p['tempExterieure'] <= 14 and p['poidsLaitCuve'] >= 3512 and p['poidsLaitCuve'] <= 4607 and p['pH'] >= 6.8 and p['pH'] <= 7.2 and p['ionPotassium'] >= 35 and p['ionPotassium'] <= 47 and p['chlorureDeSodium'] >= 1 and p['chlorureDeSodium'] <= 1.7 and p['niveauSalmonelle'] >= 17 and p['niveauSalmonelle'] <= 37 and p['niveauEColi'] >= 35 and p['niveauEColi'] <= 49 and p['niveauListeria'] >= 28 and p['niveauListeria'] <= 54):
			insert = "INSERT INTO MesuresAutomates (numUnite, numAutomate, typeAutomate, tempCuve, tempExterieure, poidsLaitCuve, poidsProduitFini, pH, ionPotassium, chlorureDeSodium, niveauSalmonelle, niveauEColi, niveauListeria, dateMesure) VALUES ("+str(p['numUnite'])+", "+str(p['numAutomate'])+", '"+str(p['typeAutomate'])+"', "+str(p['tempCuve'])+", "+str(p['tempExterieure'])+", "+str(p['poidsLaitCuve'])+", "+str(p['poidsProduitFini'])+", "+str(p['pH'])+", "+str(p['ionPotassium'])+", "+str(p['chlorureDeSodium'])+", "+str(p['niveauSalmonelle'])+", "+ str(p['niveauEColi'])+", "+str(p['niveauListeria'])+", '"+str(p['dateMesure'])+"');"
			cursor.execute(insert)

#Commit des données 
mariadb_connection.commit()
