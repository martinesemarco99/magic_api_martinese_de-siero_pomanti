import json

import requests
import pprint

r = requests.get('https://api.magicthegathering.io/v1/cards')

r.json()
pprint.pprint(r.json())
pprint.pprint(r.json()['cards'][0])

file = open("./file-" + "cards"+".json", "w+")
print(file.name)
file.writelines(r.text)
file.close()

#import modules
import csv

#now lets open the JSON file and load it
with open('file-cards.json') as json_file:
    cards= json.load(json_file)

cards_data = ['cards']

#now open the file for writing
data_file = open('file-cards.csv', 'w')

#create the csv writer object
csv_writer = csv.writer(data_file)

#counter variables used for writing
#headers to the csv file
count = 0
for data in cards_data:
    if count == 0:
        #writing header to csv
        header = cards.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(cards.values())
data_file.close()

#save and run the code