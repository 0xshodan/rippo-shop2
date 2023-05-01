import json

import numpy
import pandas

exl = pandas.read_excel("upper4.xlsx")
spacers = []
for i in range(0, len(exl["Артикул проставки"])):
    if exl["Коментарий по установке"][i] is numpy.nan:
        desc = ""
    else:
        desc = exl["Коментарий по установке"][i]
    if exl["Крепеж проставки"][i] is numpy.nan:
        comm = ""
    else:
        comm = exl["Крепеж проставки"][i]
    spacers.append(
        (
            exl["Название проставки"][i],
            exl["Артикул проставки"][i],
            exl["20мм Цена проставки"][i],
            exl["30мм Цена проставки"][i],
            exl["40мм Цена проставки"][i],
            exl["50мм Цена проставки"][i],
            desc,
            comm,
        )
    )
print(len(spacers))
spacers = sorted(list(set(spacers)), key=lambda x: x[1])
print(len(spacers))
fixtures = []
counter = 1
for name, art, price20, price30, price40, price50, comment, krepej in spacers:
    fixtures.append(
        {
            "model": "spacers.Spacer",
            "pk": counter,
            "fields": {
                "article": art,
                "category": name,
                "description": comment,
                "mount": krepej,
                "price20mm": int(price20),
                "price30mm": int(price30),
                "price40mm": int(price40),
                "price50mm": int(price50),
            },
        }
    )
    counter += 1

with open("spacers.json", "w") as wf:
    json.dump(fixtures, wf, ensure_ascii=False)
