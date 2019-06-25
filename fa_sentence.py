import json
import re

enJson = open("fa.json", "r", encoding="utf-8")
arr = []

for line in enJson:
    arr.append(line)

jsonList = []

for x in arr:
    jsonList.append(json.loads(x))

def split_sentences(st):
    sentences = re.split(r'[.\u061f?!]\s*', st)
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

faOutput = open("output/94463165_Assignment2_Part2_FA.fa", "w+", encoding='utf-8')

faOutput.write(str(sentenceCount) + '    ' + str(int(averageSentenceLength)) + '\n')
counter = 1
while counter <= 10:
    faOutput.write(str(counter) + ') ' + sentenceWithTenLength[counter] + '\n')
    counter += 1