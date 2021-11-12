import json

import pandas
import pandas as pd
import requests
import pprint
import json_normalize
r = requests.get('https://api.magicthegathering.io/v1/cards')


file = open("./file-" + "cards"+".json", "w+")
print(file.name)
file.writelines(r.text)
file.close()

dict =[]
json_data = json.load(open("./file-" + "cards" + ".json"))
for i in json_data['cards']:
    k = list(i.values())
    dict.append(k)

csv_file_path = 'cards.csv'
df = pandas.DataFrame(dict)
df = df.rename(columns=({'1':'name'}))
df.to_csv(csv_file_path, sep=',', index=None)



