import json

import requests
from bs4 import BeautifulSoup

response = requests.get("https://autodvc.ru/catalog")
soup = BeautifulSoup(response.text, "html.parser")

brands = []
for el in soup.find_all("div", class_="car-vendor"):
    try:
        name = el.a.contents[1]
    except:
        try:
            name = el.a.img.contents[0]
        except:
            name = el.a.contents[0]
    print(name)
    brands.append({"name": name, "url": "https://autodvc.ru" + el.a.attrs["href"]})

with open("brands.json", "w") as wf:
    json.dump(brands, wf, ensure_ascii=False)
