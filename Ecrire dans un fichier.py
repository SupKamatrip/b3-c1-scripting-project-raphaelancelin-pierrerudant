import csv
x=[]
y=[]
t=[]
with open('conso-annuelles_original.csv', newline='') as f:
    reader = csv.reader(f, delimiter=';')
    for col in reader:
        t.append(str(col[0].replace(",", ".")))
        x.append(str(col[2].replace(",", "."))) #n°1 = 2eme colonne
        y.append(str(col[3].replace(",", "."))) #n°2 = 3eme colonne

print(t)
print(x)
print(y)