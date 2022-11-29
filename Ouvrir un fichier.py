import csv

f= open(r"conso-annuelles_original.csv")
myReader = csv.reader(f, delimiter=';')

for row in myReader:
    print(row) # Lis le tableur ligne par ligne

    #print(str.strip(row[0])) # str.strip retire les espaces
    #print(str.strip(row[2]) + str.strip(row[3])) # additionne les colonnes 2 et 3
    #print(str.strip(row[4])) #
