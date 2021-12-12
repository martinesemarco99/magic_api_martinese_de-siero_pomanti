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

import numpy as np
import pandas as pd
mtg = pd.read_json('/Users/marcomartinese/Downloads/studioghibliproject/magic.json')
import matplotlib.pyplot as plt

#select only the interesting columns here:
features_to_consider = ['colorIdentity','manaCost','name','types','power','toughness']
df_clean = df[features_to_consider]
df.head()

#drop missing values
df_clean = df.dropna(subset=['colorIdentity','manaCost','name','types','power','toughness'])

# add a "number of color" column:
colorIdentity = {'B': 'Black', 'G': 'Green', 'R': 'Red', 'U': 'Blue', 'W': 'White'}
df_clean["colorNumber"] = df_clean.colorIdentity.apply(len)
# create new columns, one for each color
for color in colorIdentity:
    df_clean[color] = False
# set True/False in each column according to the matching colors
for color in colorIdentity:
    df_clean[color] = df_clean.colorIdentity.apply(lambda x: color in x)

df_clean.head()

#number of color on each card
df_clean['colorNumber'].plot.hist(bins=5)
plt.title("Number of color on each card",pad=10,fontsize=20)

#which words are use frequently on cards
dfText = df_clean[["text","type","name"]]
dfText["text"] = dfText["text"].apply(str)
from wordcloud import WordCloud

features_we_want = [dfText.name,dfText.type,dfText.text]
titles = ["Name of cards","Type of cards","Card text"]

for i,feature in enumerate(features_we_want):
    text = " ".join(txt for txt in feature)
    wordcloud = WordCloud(width=800, height=400,max_font_size=60, max_words=100, background_color="white").generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(titles[i],pad=10,fontsize=20)
    plt.axis("off")
    plt.show()

#relationship between cmc and manaCost
x = df_clean["cmc"]
y = df_clean["manaCost"]
plt.scatter(x, y)
plt.title("Price versus Mana Cost")
plt.xlabel("Current cost of card in €")
plt.ylabel("manacost")
plt.show()







