import random

import pandas as pd
import sources as s
import os

shablon = ['', '', '', '', '', '']

folder = "/varianti/"
table_headers = ['пол', 'имя', 'рост', 'вес', 'город', 'балл']


def generate():
    sex = s.sex[random.randint(0, 1)]
    if sex == s.sex[0]:
        name = s.names_man[random.randint(0, len(s.names_man)-1)]
    if sex == s.sex[1]:
        name = s.names_woman[random.randint(0, len(s.names_woman)-1)]
    city = s.city[random.randint(0, len(s.city)-1)]
    weight = random.randint(50, 80)
    height = random.randint(50, 80)
    point = random.randint(140, 300)
    print(sex, name, weight, height, city, point)


for i in range(10):
    generate()
# spisok = []
# df1 = pd.DataFrame(spisok,
#                    columns=table_headers)
# df1.to_excel(folder + "output_ee.xlsx")
