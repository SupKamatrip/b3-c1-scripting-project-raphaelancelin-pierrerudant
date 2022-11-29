import csv
f = open(r"conso-annuelles_original.csv")
myReader = csv.reader(f, delimiter=';')
x = 0

for row in myReader:
    x = x + 1
    if not all(row):
        print(x, "vide")
    else:
        print(x, "non")

    #print(row[0]) #Lis la colonne 0

    #print(row) # Lis le tableur ligne par ligne

    #print(str.strip(row[0])) # str.strip retire les espaces
    #print(str.strip(row[2]) + str.strip(row[3])) # additionne les colonnes 2 et 3
    #print(str.strip(row[4])) #
