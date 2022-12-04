import csv
data = [] # liste vide afin de faciliter les nettoyages
inputdata = "conso-annuelles_original.csv" # fichier source (depuis lequel on va effectuer notre traitement)
with open(inputdata,'r') as csvfile:
    myReader = csv.reader(csvfile, delimiter=';') # le delimiter va permettre de parcourir correctement les lignes et les colonnes
    for row in myReader:  # pour chaque ligne dans mon reader (le fichier original donc)
        if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '': # j'enlève les lignes contenant une case vide
            data.append([row[0],row[1],row[2],row[3],row[4]]) # j'insére les lignes souhaités dans ma liste data

for row in data: # pour chaque ligne dans ma liste data
    del row[1]  # je supprime la colonne ID logement

data.pop(0) # permet de convertir sans l'en tete

for row in data:
    row[1] = row[1].replace(',', '.') # on remplace les virgules par des points afin de pouvoir additionner
    row[2] = row[2].replace(',', '.')

for row in data: # pour chaque ligne dans ma liste data
    row[0] = row[0].replace('-', '0') # remplace le tiret par un 0 pour pouvoir additionner
    row[1] = row[1].replace('-', '0')
    row[2] = row[2].replace('-', '0')
    row[3] = row[3].replace('-', '0')

for row in data:
    row[2] = float(row[2]) + float (row[1]) # on additionne no colonnes Conso Année 1 et Année 2
    del row[1]
for row in data:
    row[1] = round(float(row[1]), 2) # on arrondis les valeurs pour que ca soit plus propre (éviter les 10.0000009)

data.sort(key=lambda x: (x[2], x[1]), reverse=True) # on tri par odre décroissant selon le type(x2) et la conso(x1)
data.insert(0, ['Appareil suivi', 'CT Annuelle', 'Type']) # on réinsère l'en tëte

with open('conso-clean.csv', 'w', newline='') as csvfile: # on ouvre notre fichier dans lequel on va écrire nos nettoyages
    myWriter = csv.writer(csvfile, delimiter=';') # création d'un writer, celui-ci va nous permettre d'écrire dans le fichier
    myWriter.writerows(data) # écriture des lignes dans le fichier de sortie (writerow)
