import csv

with open('archivos\\prueba2.csv') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)