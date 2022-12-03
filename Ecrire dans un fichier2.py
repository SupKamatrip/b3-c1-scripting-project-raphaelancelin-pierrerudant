import csv, operator

f = open(r"conso-annuelles_v1.csv")
s = open("conso_annuelles_v2.csv",'w')
myReader = csv.reader(f, delimiter=';')
f = ''.join([i for i in f])
f = f.replace('ID logement','CT Annuelle')  # remplacement de la colonne id logement par la consommation totale
f = sorted(f, key=lambda x: [1])
print(f)