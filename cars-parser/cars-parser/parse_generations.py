import json

import requests
from bs4 import BeautifulSoup

with open("brands2.json", "r") as rf:
    brands = json.load(rf)

for i, brand in enumerate(brands):
    for o, car in enumerate(brand["cars"]):
        response = requests.get(car["url"])
        soup = BeautifulSoup(response.text, "html.parser")
        gens = []
        for generation in soup.find_all("div", class_="car-modification"):
            a_img = generation.contents[0]
            img = a_img.img
            try:
                name = img.attrs["title"].replace(brand["name"], "").lstrip().rstrip()
            except:
                name = (
                    generation.p.a.contents[0]
                    .replace(brand["name"], "")
                    .lstrip()
                    .rstrip()
                )
            gens.append(
                {
                    "name": name,
                    "url": "https://autodvc.ru" + a_img.attrs["href"],
                    "img": img.attrs["src"],
                }
            )
        brands[i]["cars"][o]["generations"] = gens

with open("brands3.json", "w") as wf:
    json.dump(brands, wf, ensure_ascii=False)
