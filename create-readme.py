import csv
ta=None
with open('papa.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ta=list(csv_reader)
f = open("README.md", "a")
f.write(capin)
f.close()