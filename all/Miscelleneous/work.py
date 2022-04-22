import csv
from pprint import pprint

import requests

fh = open("response.csv", "w", newline="", encoding="utf-8")
headers = (
    "name",
    "last_name",
    "age",
    "blood",
    "born",
    "born_place",
    "cellphone",
    "city",
    "country",
    "eye_color",
    "father_name",
    "gender",
    "height",
    "national_code",
    "religion",
    "system_id",
    "weight",
)
dw = csv.DictWriter(fh, fieldnames=headers)
dw.writeheader()
i = 0
while i < 10:
    response = requests.get("https://pipl.ir/v1/getPerson")
    # pprint(response.json()['person']['personal'].keys())
    dw.writerow(response.json()["person"]["personal"])
    i += 1
