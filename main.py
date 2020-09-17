from bs4 import BeautifulSoup
import requests
import re
import csv
codelandWebsite=requests.get("https://shop.dev.to/collections/codeland")
soupCodeland = BeautifulSoup(codelandWebsite.text,"html.parser")
listCodelandItem=soupCodeland.select(".grid-view-item")
DevtoItemCsv=[]
for item in listCodelandItem:
    currencyFloat=None
    changeCurrencyToFloat=re.search(r"\d+", item.select_one(".grid-view-item__meta").getText())
    if changeCurrencyToFloat:            
        currencyFloat=changeCurrencyToFloat.group()
    DevtoItemCsv.append({
        "image":"https:"+item.select_one(".grid-view-item__image").get("src") if item.select_one(".grid-view-item__image").get("src") else "",
        "url":"https://shop.dev.to"+item.select_one("a").get("href") if item.select_one("a").get("href") else "",    
        "title":item.select_one(".grid-view-item__title").getText() if item.select_one(".grid-view-item__title") else "",
        "price":float(currencyFloat)
    })
page=0
while True:
    page+=1
    devtoShopWebsite=requests.get("https://shop.dev.to/collections/2018-new-merch?page="+str(page))
    soupDevtoShop=BeautifulSoup(devtoShopWebsite.text,"html.parser")
    ListItemDevtoshop=soupDevtoShop.select(".grid-view-item")
    if len(ListItemDevtoshop) == 0 or not ListItemDevtoshop:
        break
    for item in ListItemDevtoshop:
        currencyFloat=None
        changeCurrencyToFloat=re.search(r"\d+", item.select_one(".grid-view-item__meta").getText())
        if changeCurrencyToFloat:            
            currencyFloat=changeCurrencyToFloat.group()
        DevtoItemCsv.append({
        "image":"https:"+item.select_one(".grid-view-item__image").get("src") if item.select_one(".grid-view-item__image").get("src") else "",
        "url":"https://shop.dev.to"+item.select_one("a").get("href") if item.select_one("a").get("href") else "",    
        "title":item.select_one(".grid-view-item__title").getText() if item.select_one(".grid-view-item__title") else "",
        "price":float(currencyFloat)
        })
def create_csv(dict_data,name):
    csv_columns = ['image','url','title','price']
    csv_file = name
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")
create_csv(DevtoItemCsv,"devto.csv")