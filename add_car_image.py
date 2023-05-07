import json

with open("cars.json", "r", encoding="utf8") as rf:
    cars = json.load(rf)

with open("brands5.json", "r", encoding="utf8") as rf:
    brands = json.load(rf)

with open("brands.json", "r", encoding="utf8") as rf:
    brands_db = json.load(rf)

def test(cars, cr):
    for c, car in enumerate(cars):
        for brand in brands_db:
            if car["fields"]["brand"] == brand["pk"]:
                if cr["name"] == car["fields"]["name"]:
                    cars[c]["fields"]["photo"] = cr["img_path"]
                    return
for br in brands:
    print(br["name"])
    for cr in br["cars"]:
        test(cars, cr)

            

with open("upd_cars.json", "w", encoding="utf8") as wf:
    json.dump(cars, wf, ensure_ascii=False)

with open("upd_cars2.json", "w") as wf:
    json.dump(cars, wf)