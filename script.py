with open('conso-annuelles_v1.csv') as file:
    content = file.readlines()
    header = content[:1]
    rows = content[1:]

# print(header)
# print(rows[5])
# print("\n")
print(rows[1])


for x in range (len(rows)):
    print (rows[x:])

