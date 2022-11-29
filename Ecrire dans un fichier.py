import csv
f = open(r"conso-annuelles_original.csv")
s = open("conso-annuelles_v1.csv",'w')
myReader = csv.reader(f, delimiter=';')
myWriter = csv.writer(s, delimiter=';')

for row in myReader:

    for col in row:
        #print(col)
        if col=='': #
            break
    if col=='':
        continue # on continue à lire les colonnes/lignes
    if row[0] != 'Appareil suivi':   # additionner les deux colonnes et les remplacer par la 1
         row[1]=float(row[2])+float(row[3]) #on ne peut faire de calculs dans python avec une virgule
    print(row)




#with open("conso-annuelles_original.csv",'r') as file:
#    data = file
#file_csv = 'Data2.csv'
#csv_file = open('conso-annuelles_original.csv', 'r')
#with open('conso-annuelles_v1.csv', 'a') as writable:
 #   writer = csv.writer(writable)
  #  for row in csv_file:
   #     writer.writerow(str.strip(row[0]))

