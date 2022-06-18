import json
import re
import requests
import json

f = open("D:\\Programming stuff\\Python\\Python Bootcamp\\RiderAPIGather\\UAE Team Emirates", 'r')

data = f.read()

# Parsing data from text file
results = re.search("'(.*)'", data)
ridersNoQuotes = results.group().replace("'", "")
ridersNoWhiteSpace = ridersNoQuotes.replace(" ", "")
riders = ridersNoWhiteSpace




rider_list = riders.split(",")


for rider in rider_list:
    url = "https://pro-cycling-stats.p.rapidapi.com/riders/" + rider
    print(url)

    headers = {
        #mykey
        #host
    }

    response = requests.request("GET", url, headers=headers)
    jsonresponse = response.json();
    with open('UAE.json', "a+") as f:
        f.seek(0)
        file_data = f.read(100)
        if len(file_data) > 0:
            f.write('\n')
        f.write(json.dumps(jsonresponse))




