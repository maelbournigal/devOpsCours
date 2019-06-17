#Import des modules nécessaires
import random
import json
import time
from datetime import datetime, timedelta
import os

#Récupération de l'heure actuelle
now = datetime.now() + timedelta(hours=2)
print(now)

#Récupération de l'unixEpoch
unixEpoch  = round(time.time())
unixEpochString = str(unixEpoch)
data = {}
data['mesure'] = []

#Lecture du fichier de configuration des automates
with open('./config.json') as json_file:
    dataJson = json.load(json_file)
    numUnite = dataJson['numUnite']
    numUniteString = str(numUnite)
    #Pour tous les automates génération de données aléatoires 
    for automate in dataJson['automates']:
        data['mesure'].append({  
        'numUnite': numUnite,
        'numAutomate': automate['numAutomate'],
        'typeAutomate': automate['typeAutomate'],
        'tempCuve': round(random.uniform(2.5, 4.5),1),
        'tempExterieure': round(random.uniform(8, 14),1),
        'poidsLaitCuve': random.randrange(3512, 4608, 1),
        'poidsProduitFini': 3,
        'pH': round(random.uniform(6.8, 7.2),1),
        'ionPotassium': random.randrange(35, 48, 1),
        'chlorureDeSodium': round(random.uniform(1, 1.7),1),
        'niveauSalmonelle': random.randrange(17, 38, 1),
        'niveauEColi': random.randrange(35, 50, 1),
        'niveauListeria': random.randrange(28, 55, 1),
        'dateMesure': now.strftime("%Y-%m-%d %H:%M:%S")
    })

#Sauvegarde du fichier au format JSON
with open('paramunite'+numUniteString+'_'+unixEpochString+'.json', 'w') as outfile:  
    json.dump(data, outfile)

#Exécution
os.system("python ./insertData.py 1")

