import csv
data = [] #liste vide
inputdata = "conso-annuelles_original.csv"
exitdata = open("conso-clean.csv","w")
with open(inputdata,'r') as csvfile:
    myReader = csv.reader(csvfile, delimiter=';')
    for row in myReader:
        if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '':
            data.append([row[0],row[1],row[2],row[3],row[4]])

for row in data:
    del row[1]

data.pop(0) # permet de convertir sans l'en tete

for row in data:
    row[1] = row[1].replace(',', '.') # on remplace
    row[2] = row[2].replace(',', '.')

for row in data:
    if row != '-':
        row.replace('-','0')

for row in data:
    row[2] = float(row[2]) + float (row[1])
    del row[1]
for row in data:
    row[1] = round(float(row[1]), 2)

data.sort(key=lambda x: (x[2], x[1]), reverse=True)
data.insert(0, ['Appareil suivi', 'CT Annuelle', 'Type'])

with open('conso-clean.csv', 'w', newline='') as csvfile: # ouverture du fichier de sortie en mode write
    myWriter = csv.writer(csvfile, delimiter=';') # création d'un objet writer pour écrire dans le fichier de sortie
    myWriter.writerows(data) # écriture des lignes dans le fichier de sortie
print(data)