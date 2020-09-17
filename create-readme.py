import csv
from datetime import datetime
devtoCsv=None
with open('devto.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    devtoCsv=list(csv_reader)
tanggal=datetime.now()

tanggalSekarang=str(tanggal.day)+"-"+str(tanggal.month)+"-"+str(tanggal.year)
READMES="""last scraped in %s

---

## List of item scraped from devto shop

|no|image|url|title|price|
|--|-----|---|-----|-----|\n""" % (tanggalSekarang)
number=0
for item in devtoCsv[1:len(devtoCsv)]:
    number+=1
    READMES+="|"+str(number)+"|<img src='"+item[0]+"' width='300px' height='200px' />|"+item[1]+"|"+item[2]+"|$ "+item[3]+"|\n"
f = open("README.md", "w+")
f.write(READMES)
f.close()