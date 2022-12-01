import csv
f = open(r"conso-annuelles_original.csv")
s = open("conso-annuelles_v1.csv",'w')
myReader = csv.reader(f, delimiter=';')
myWriter = csv.writer(s, delimiter=';')

for row in myReader:

    for col in row:
        if col == '':
            break
    if col == '':
        continue  # on continue à lire les colonnes/lignes

    if row[0] != 'Appareil suivi':  # additionner les deux colonnes et les remplacer par la 1
        row[1] = float(row[2].replace(',', '.')) + float(
            row[3].replace(',', '.'))  # on ne peut faire de calculs dans python avec une virgule
    writable = row[0], row[1]
    myWriter.writerow(writable) #on ecris les deux premières colonnes



#csv_file = open('conso-annuelles_original.csv', 'r')
#with open('conso-annuelles_v1.csv', 'a') as writable:
 #   writer = csv.writer(writable)
  #  for row in csv_file:
   #     writer.writerow(str.strip(row[0]))

