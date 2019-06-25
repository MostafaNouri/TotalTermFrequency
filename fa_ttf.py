import json
import re
import operator

faJson = open("fa.json", "r", encoding='utf-8')
arr = []

for line in faJson:
    arr.append(line)

jsonList = []

for x in arr:
    jsonList.append(json.loads(x))

jsonParsedList = []
for jsonData in jsonList:
    jsonParsedList.append({'id': jsonData['id'],
                           'title': re.findall(r"[\u0620-\u065F\u0670-\u06ff]+", jsonData['title']),
                           'body': re.findall(r"[\u0620-\u065F\u0670-\u06ff]+", jsonData['body'])})

# print(jsonParsedList[0]['body'])

def replaceFaWord(word):
    data = word.replace('\u064a', '\u06cc').replace('\u0622', '\u0627').replace('\u0643', '\u06a9')
    return data

faWords = {}

def updateFarsiWord(list ,word):
    data = replaceFaWord(word)

    if list.get(data) != None:
        list.update({data: list[data] + 1})
    else:
        list.update({data: 1})

for data in jsonParsedList:
    for titleData in data['title']:
        updateFarsiWord(faWords, titleData)
    for bodyData in data['body']:
        updateFarsiWord(faWords, bodyData)

faOutput = open("output/94463165_Assignment2_Part1_FA.fa", "w+", encoding='utf-8')

counter = 1
while counter <= 1000:
    key = max(faWords.items(), key=operator.itemgetter(1))[0]
    token = faWords.pop(key)
    faOutput.write(str(counter) + ')' + key + ': ' + str(token) + '\n')
    counter += 1