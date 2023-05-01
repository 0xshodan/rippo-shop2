import json

import numpy
import pandas
from pytils.translit import slugify

exl = pandas.read_excel("upper4.xlsx")

with open("cars.json", "r") as rf:
    cars = json.load(rf)
with open("brands.json", "r") as rf:
    brands = json.load(rf)
with open("car_generations.json", "r") as rf:
    generations = json.load(rf)
with open("spacers.json", "r") as rf:
    spacers = json.load(rf)
alls: list[tuple] = []
arts: list[tuple] = []


def find_i(i):
    for brand in brands:
        if brand["fields"]["name"] == exl["Марка авто"][i]:
            for car in cars:
                if (
                    car["fields"]["name"] == str(exl["Модель авто"][i])
                    and car["fields"]["brand"] == brand["pk"]
                ):
                    for generation in generations:
                        if (
                            generation["fields"]["name"]
                            == str(exl["Поколение авто"][i])
                            and generation["fields"]["car"] == car["pk"]
                        ):
                            name = str(exl["Модификация авто"][i]).lstrip().rstrip()
                            slug = generation["fields"]["slug"] + "-" + slugify(name)
                            alls.append(
                                (
                                    generation["pk"],
                                    name,
                                    exl["Год выпуска"][i],
                                    slug,
                                )
                            )
                            if exl["Коментарий по установке"][i] is numpy.nan:
                                comm = ""
                            else:
                                comm = exl["Коментарий по установке"][i]
                            if exl["Крепеж проставки"][i] is numpy.nan:
                                krepj = ""
                            else:
                                krepj = exl["Крепеж проставки"][i]
                            arts.append(
                                (
                                    exl["Артикул проставки"][i],
                                    slug,
                                    comm,
                                    krepj,
                                    exl["Название проставки"][i],
                                )
                            )
                            return


for i in range(0, len(exl["Марка авто"])):
    print(i)
    find_i(i)

alls = sorted(list(set(alls)), key=lambda x: x[1])
arts = list(set(arts))
fixtures = []
counter = 1
for pk, modif, year, slug in alls:
    raw_spacers = []
    for i, x in enumerate(arts):
        if x[1] == slug:
            raw_spacers.append(x)
    spacers_pk = []
    for raw_s in raw_spacers:
        for spacer in spacers:
            if (
                raw_s[0] == spacer["fields"]["article"]
                and raw_s[2] == spacer["fields"]["description"]
                and raw_s[3] == spacer["fields"]["mount"]
                and raw_s[4] == spacer["fields"]["category"]
            ):
                spacers_pk.append(spacer["pk"])
    year_from, year_end = year.split(" по ")
    year_from, year_end = int(year_from.replace("(", "")), int(
        year_end.replace(")", "")
    )
    fixtures.append(
        {
            "model": "cars.CarModification",
            "pk": counter,
            "fields": {
                "name": modif,
                "car": pk,
                "year_from": year_from,
                "year_end": year_end,
                "slug": slug + str(year_from) + "-" + str(year_end),
                "spacers": spacers_pk,
            },
        }
    )
    counter += 1
with open("modif.json", "w") as wf:
    json.dump(fixtures, wf, ensure_ascii=False)
