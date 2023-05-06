import json

import requests
from bs4 import BeautifulSoup

with open("brands.json", "r") as rf:
    brands = json.load(rf)

for i, brand in enumerate(brands):
    response = requests.get(brand["url"])
    soup = BeautifulSoup(response.text, "html.parser")
    cars: list[dict] = []
    for car in soup.find_all("a", class_="car-model"):
        try:
            name = car.p.contents[0]
        except:
            name = car.img.p.contents[0]
        cars.append(
            {
                "name": name,
                "url": "https://autodvc.ru" + car.attrs["href"],
                "img": car.img.attrs["src"],
            }
        )
    brands[i]["cars"] = cars

with open("brands2.json", "w") as wf:
    json.dump(brands, wf, ensure_ascii=False)
