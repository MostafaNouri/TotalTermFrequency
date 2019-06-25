import json
import re
import operator

enJson = open("en.json", "r")
arr = []

for line in enJson:
    arr.append(line)

jsonList = []

for x in arr:
    jsonList.append(json.loads(x))

jsonParsedList = []
for jsonData in jsonList:
    jsonParsedList.append({'id': jsonData['id'],
                           'title': re.findall(r"[\w']+", jsonData['title']),
                           'body': re.findall(r"[\w']+", jsonData['body'])})

enWords = {}

def updateEnglishWord(list ,word):
    data = word.lower()

    if list.get(data) != None:
        list.update({data: list[data] + 1})
    else:
        list.update({data: 1})

for data in jsonParsedList:
    for titleData in data['title']:
        updateEnglishWord(enWords, titleData)
    for bodyData in data['body']:
        updateEnglishWord(enWords, bodyData)

enOutput = open("output/94463165_Assignment2_Part1_EN.en", "w+")

counter = 1
while counter <= 1000:
    key = max(enWords.items(), key=operator.itemgetter(1))[0]
    token = enWords.pop(key)

    enOutput.write(str(counter) + ')' + key + ': ' + str(token) + '\n')
    counter += 1