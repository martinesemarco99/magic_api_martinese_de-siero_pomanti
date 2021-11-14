import json
import csv
import requests
import pprint
import pandas
import pandas as pd
#using Python Requests to interact with a REST API
r = requests.get('https://api.magicthegathering.io/v1/cards').json()

df =pd.DataFrame(r["cards"])
from pandas.io.json import json_normalize
pd.json_normalize(r["cards"])

dict =[r]
with open('magic.json', 'w') as outfile:
    json.dump(dict, outfile)

print(df)
df.to_csv("/Users/marcomartinese/Downloads/studioghibliproject/magic.csv")









