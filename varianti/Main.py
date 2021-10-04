import random

import pandas as pd
import sources as s


shablon = ['', '', '', '', '', '']

folder = "/varianti/"
table_headers = ['пол', 'имя', 'рост', 'вес', 'город', 'балл 2019', 'балл 2020', 'балл 2021']


def generate():
    sex = s.sex[random.randint(0, 1)]
    if sex == s.sex[0]:
        name = s.names_man[random.randint(0, len(s.names_man) - 1)]
    else:
        name = s.names_woman[random.randint(0, len(s.names_woman) - 1)]

    city = s.city[random.randint(0, len(s.city) - 1)]
    weight = random.randint(50, 80)
    height = random.randint(150, 180)
    point = random.randint(140, 300)
    point2 = random.randint(140, 300)
    point3 = random.randint(140, 300)
    return [sex, name, weight, height, city, point, point2, point3]


for j in range(30):
    all_people = []
    for i in range(random.randint(100, 120)):
        all_people.append(generate())
    df = pd.DataFrame(all_people, columns=table_headers)
    print(df.to_string())
    df.to_excel(f'generated/{j}.xlsx')
