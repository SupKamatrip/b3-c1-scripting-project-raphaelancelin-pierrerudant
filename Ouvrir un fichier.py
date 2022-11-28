import csv;

f= open(r"conso-annuelles_original.csv")
myReader = csv.reader(f)
for row in myReader:
    print(row)