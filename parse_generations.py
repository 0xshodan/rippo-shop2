import json

import pandas as pd
from pytils.translit import slugify

exl = pd.read_excel("upper2.xlsx")
alls: list[tuple] = []
with open("cars.json", "r") as rf:
    cars = json.load(rf)
with open("brands.json", "r") as rf:
    brands = json.load(rf)
for i in range(0, len(exl["Поколение авто"])):
    print(i)
    for brand in brands:
        if exl["Марка авто"][i] == brand["fields"]["name"]:
            for car in cars:
                if (
                    exl["Модель авто"][i] == car["fields"]["name"]
                    and car["fields"]["brand"] == brand["pk"]
                ):
                    print("parsed")
                    alls.append(
                        (car["pk"], exl["Поколение авто"][i], car["fields"]["slug"])
                    )
                    break
            break
alls = sorted(list(set(alls)), key=lambda x: x[1])
fixtures = []
counter = 1
for pk, gen, slug in alls:
    if "+" in gen:
        fixtures.append(
            {
                "model": "cars.CarGeneration",
                "pk": counter,
                "fields": {
                    "name": gen,
                    "slug": slug + "-" + slugify(gen) + "-plus",
                    "car": pk,
                },
            }
        )
    else:
        fixtures.append(
            {
                "model": "cars.CarGeneration",
                "pk": counter,
                "fields": {"name": gen, "slug": slug + "-" + slugify(gen), "car": pk},
            }
        )
    counter += 1
with open("car_generations.json", "w") as wf:
    json.dump(fixtures, wf, ensure_ascii=False)
#     for car in cars:
#         if car["fields"]["name"] == str(exl["Поколение авто"][i]):
#             for brand in brands:
#                 if brand["fields"]["name"] == exl["Марка авто"][i]:
#                     if str(exl["Модель авто"][i]) in str(
#                         exl["Поколение авто"][i]
#                     ) and str(exl["Модель авто"][i]) != str(exl["Поколение авто"][i]):
#                         pokol = exl["Поколение авто"][i].replace(
#                             str(exl["Модель авто"][i]), ""
#                         )
#                     else:
#                         pokol = str(exl["Поколение авто"][i]).lstrip().rstrip()
#                     year_from, year_end = exl["Год выпуска"][i].split(" по ")
#                     year_from, year_end = (
#                         int(year_from.replace("(", "")),
#                         int(year_end.replace(")", "")),
#                     )
#                     data = (car["pk"], pokol, car["fields"]["slug"])
#                     for d in alls:
#                         if d[0] == data:
#                             break

#                     alls.append(
#                         (
#                             data,
#                             year_from,
#                             year_end,
#                         )
#                     )
#                     break
#             break

# with open("dddata_normal.json", "w") as wf:
#     json.dump(alls, wf, ensure_ascii=False)


# import json

# from pytils.translit import slugify

# with open("dddata.json", "r") as rf:
#     data = json.load(rf)
# print(len(data))
# x = []
# for i in data:
#     x.append(((i[0][0], i[0][1], i[0][2]), i[1], i[2]))
# x = sorted(list(set(x)), key=lambda x: x[0][1])
# fixtures = []

# for i, car_year in enumerate(x):
#     fixtures.append(
#         {
#             "model": "cars.CarYear",
#             "pk": i + 1,
#             "fields": {
#                 "name": car_year[0][1].lstrip().rstrip(),
#                 "slug": car_year[0][2]
#                 + "-"
#                 + slugify(car_year[0][1].lstrip().rstrip()),
#                 "year_from": car_year[1],
#                 "year_end": car_year[2],
#                 "car": car_year[0][0],
#             },
#         }
#     )
# with open("caryears.json", "w") as wf:
#     json.dump(fixtures, wf, ensure_ascii=False)
