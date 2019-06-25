import json
import re

enJson = open("en.json", "r")
arr = []

for line in enJson:
    arr.append(line)

jsonList = []

for x in arr:
    jsonList.append(json.loads(x))

def split_sentences(st):
    sentences = re.split(r'[.?!]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]

sentences = []

for data in jsonList:
    sentences.append(split_sentences(data['body']))

normalSentences = []

for arr in sentences:
    for sentence in arr:
        normalSentences.append(sentence.replace('\n', ' '))

sentenceCount = len(normalSentences)

totalSentenceLength = 0
sentenceWithTenLength = []

for sentence in normalSentences:
    length = len(sentence)
    if length == 10:
        sentenceWithTenLength.append(sentence)
    totalSentenceLength += length

averageSentenceLength = totalSentenceLength/sentenceCount

enOutput = open("output/94463165_Assignment2_Part2_EN.en", "w+")

enOutput.write(str(sentenceCount) + '    ' + str(int(averageSentenceLength)) + '\n')
counter = 1
while counter <= 10:
    enOutput.write(str(counter) + ') ' + sentenceWithTenLength[counter] + '\n')
    counter += 1