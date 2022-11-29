import csv

s = open(r"conso-annuelles_original.csv")
f = open(r"conso-annuelles_v1.csv")
myReader = csv.reader(f, delimiter=';')
myWriter = csv.writer(s, delimiter=';')

for row in myReader:
    print(str.strip(row[0])) # str.strip retire les espaces
    print(str.strip(row[2]) + str.strip(row[3])) # additionne les colonnes 2 et 3
    print(str.strip(row[4])) #


#with open("conso-annuelles_original.csv",'r') as file:
#    data = file
#file_csv = 'Data2.csv'
#csv_file = open('conso-annuelles_original.csv', 'r')
#with open('conso-annuelles_v1.csv', 'a') as writable:
 #   writer = csv.writer(writable)
  #  for row in csv_file:
   #     writer.writerow(str.strip(row[0]))

