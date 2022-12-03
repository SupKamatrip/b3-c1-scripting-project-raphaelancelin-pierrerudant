import csv, operator
f = open(r"conso-annuelles_original.csv")
s = open("conso-annuelles_v2.csv", "w")
myReader = csv.reader(f, delimiter=';')
myWriter = csv.writer(s, delimiter=';')
x = 0
v = 0
p = 0

for row in myReader:
    x = x + 1
    if not all(row):
        v = v + 1 #ligne vide
        print(x, v, "vide")
    else:
        p = p + 1 #ligne bonne
        print(x, p, "non")

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
            writable = row[0], consototal, row[4]
            myWriter.writerow(writable)
g = open("conso-annuelles_v2.csv", "r") # on reouvre le fichier qu'on  a modifié
t = open("conso-annuelles_v3.csv", "w") #
consoclean = sorted(g, key=lambda x: (x[2],x[1]), reverse=True)
print(g)
#print(f)

    #print(row[0]) #Lis la colonne 0 

    #print(row) # Lis le tableur ligne par ligne

    #print(str.strip(row[0])) # str.strip retire les espaces
    #print(str.strip(row[2]) + str.strip(row[3])) # additionne les colonnes 2 et 3
    #print(str.strip(row[4])) #
