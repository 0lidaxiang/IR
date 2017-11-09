#!/usr/bin/python3
# coding: utf-8

import os
import document
import dictionary
from collections import Counter
from collections import OrderedDict

def createWordDocNoCount():
    allFilesContent = document.getAllFilesContent()
    allDictionary = dictionary.getDictionary()
    fname = "./initialResult/wordIndex.txt"
    res =  os.path.isfile(fname)

    if res:
        pass
    else:
        f = open(fname, 'w')
        allFileContentLists = []
        for fileContent in allFilesContent:
            allFileContentLists.append(fileContent.split(" "))

        strWrite = ""
        index = 0
        for fileContentList in allFileContentLists:
            if index < len(allFileContentLists):
                countDic = dict(Counter(allFileContentLists[index]))
                for wordName in OrderedDict(sorted(countDic.items())):
                    wordNum = countDic[wordName]
                    if wordNum > 0 and wordName != "\n":
                        strWrite  += wordName + ":" + str(allDictionary.index(wordName)) + " "
                strWrite += "\r\n"
            index += 1
        f.write(strWrite)
        f.close()

def getWordDocNoCount():
    createWordDocNoCount()
    res = []
    with open('./initialResult/wordIndex.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        aDocWordCountList = strTemp.split(" ")
        del(aDocWordCountList[-1])
        tempList = []
        for value in aDocWordCountList:
            results = value.split(":")
            tempList.append(results)
        res.append(tempList)
    return res

def getOnlyWordDocNoCount():
    createWordDocNoCount()
    res = []
    with open('./initialResult/wordIndex.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        aDocWordCountList = strTemp.split(" ")
        del(aDocWordCountList[-1])
        tempList = []
        for value in aDocWordCountList:
            results = value.split(":")
            tempList.append(results[0])
        res.append(tempList)
    return res



# res = getAllWordDocNoCount()
# res = getOnlyWordDocNoCount()
# print(len(res))
# print(len(res[0]))
# print(res[0][0])
# print(res[0][1])
# print(res[0][2])
# print(res[0][0][0])
# k =0
# for v in res:
#     if k < 3:
#         print(v)
#         k  = k + 1
