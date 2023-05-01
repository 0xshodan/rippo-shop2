import json

import numpy
import pandas
from pytils.translit import slugify

with open("brands.json", "r") as rf:
    brands = json.load(rf)

alls = []
exl = pandas.read_excel("upper.xlsx")
for i in range(0, len(exl["Модель авто"])):
    if (
        exl["Модель авто"][i] != numpy.nan
        or exl["Модель авто"][i] != " "
        or exl["Модель авто"][i] != "\xa0"
    ):
        for brand in brands:
            if exl["Марка авто"][i].lstrip().rstrip() == brand["fields"]["name"]:
                alls.append(
                    (
                        brand["pk"],
                        str(exl["Модель авто"][i]).lstrip().rstrip(),
                        brand["fields"]["slug"],
                    )
                )
                break
    else:
        print(i, exl["Модель авто"][i])
counter = 1
fixtures = []
alls = sorted(list(set(alls)), key=lambda x: x[1])
for pk, name, brand_slug in alls:
    fixtures.append(
        {
            "model": "cars.Car",
            "pk": counter,
            "fields": {
                "name": name,
                "slug": brand_slug + "-" + slugify(name),
                "brand": pk,
            },
        }
    )
    counter += 1

with open("cars.json", "w") as wf:
    json.dump(fixtures, wf, ensure_ascii=False)
