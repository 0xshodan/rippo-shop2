import json

with open("cars.json", "r", encoding="utf8") as rf:
    cars = json.load(rf)

with open("brands5.json", "r", encoding="utf8") as rf:
    brands = json.load(rf)

with open("brands.json", "r", encoding="utf8") as rf:
    brands_db = json.load(rf)

for c, car in enumerate(cars):
    for brand in brands_db:
        if car["fields"]["brand"] == brand["pk"]:
            for br in brands:
                for cr in br["cars"]:
                    if cr["name"] == car["fields"]["name"]:
                        cars[c]["fields"]["photo"] = cr["img_path"]

with open("upd_cars.json", "w", encoding="utf8") as wf:
    json.dump(cars, wf, ensure_ascii=False)

with open("upd_cars2.json", "w") as wf:
    json.dump(cars, wf)