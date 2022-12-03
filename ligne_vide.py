import csv, operator
import unicodedata
data = [] #liste vide
fichier_csv = "conso-annuelles_original.csv"
exitdata = open("conso-clean.csv","w")
with open(fichier_csv,'r') as csvfile:
    myReader = csv.reader(csvfile, delimiter=';')
    x = 0
    v = 0
    p = 0
    for row in myReader:
        x = x + 1
        for col in row:
            if col == '':
                break
        if col == '':
            continue  # on continue à lire les colonnes/lignes
        if row[0] != 'Appareil suivi':
            if row[2] == '-':
                AN2 = row[2].replace('-', '0')
            else:
                AN1 = row[2]

            if row[3] == '-':
                AN2 = row[3].replace('-', '0')
            else:
                AN2 = row[3]
            consototal = float(AN1.replace(',', '.')) + float(AN2.replace(',', '.'))
            data = row[0], consototal, row[4]
            print(data)
#dataclean = sorted(data,key=lambda x: (x[2], x[1]), reverse=True)
#data.insert(0,['Appareil suivi', 'CT Annuelle','Type'])

with open('conso-clean.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(data)
#print(f)

    #print(row[0]) #Lis la colonne 0 

    #print(row) # Lis le tableur ligne par ligne

    #print(str.strip(row[0])) # str.strip retire les espaces
    #print(str.strip(row[2]) + str.strip(row[3])) # additionne les colonnes 2 et 3
    #print(str.strip(row[4])) #
