import csv
f = open(r"conso-annuelles_v1.csv")
s = open("conso_annuelles_v2.csv",'w')
myReader = csv.reader(f, delimiter=';')
f = ''.join([i for i in f])
f = f.replace('ID logement','CT Annuelle')
for row in f:
    print(row)
#s = sorted(f, reverse=True)
#print(f)