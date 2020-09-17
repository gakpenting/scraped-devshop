from bs4 import BeautifulSoup
import requests
import re
codelandWebsite=requests.get("https://shop.dev.to/collections/codeland")
soupCodeland = BeautifulSoup(codelandWebsite.text)
listCodelandItem=soupCodeland.select(".grid-view-item")
DevtoItemCsv=[]
for item in listCodelandItem:
    DevtoItemCsv.append({
        "image":"https:"+item.select_one(".grid-view-item__image").text,
        "url":"https://shop.dev.to"+item.select_one("a").get("href"),    
        "title":item.select_one(".grid-view-item__title").text,
        "price":item.select_one(".product-price__price").text
    })
