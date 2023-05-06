import requests
import json

with open("brands4.json", "r", encoding="utf8") as rf:
    brands = json.load(rf)

for i, brand in enumerate(brands):
    print(i)
    for x, car in enumerate(brand["cars"]):
        for m, gen in enumerate(car["generations"]):
            print(gen)
            img_name = gen["img"].split("?")[0].replace("https://autodvc.ru/sites/default/files/styles/carimage/public/images/cars/", "").replace("/", "_")
            with open(f"media/generations/{img_name}", "wb") as wf:
                resp = requests.get(gen["img"])
                wf.write(resp.content)
            brands[i]["cars"][x]["generations"][m]["img_path"] = f"media/generations/{img_name}"

with open("brands5.json", "w") as wf:
    json.dump(brands, wf)