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
    fname = "../initialResult/wordCount.txt"
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
                        strWrite  += wordName + " "
                strWrite += "\r\n"
            index += 1
        f.write(strWrite)
        f.close()

def getWordDocNoCount():
    createWordDocNoCount()
    res = []
    with open('../initialResult/wordCount.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        # aDocWordCountList = strTemp.split(" ")
        # del(aDocWordCountList[-1])
        # tempList = []
        # for value in aDocWordCountList:
            # results = value.split(":")
            # tempList.append(value)
        res.append(strTemp)
    return res

def getAllWordDocNoCount():
    createWordDocNoCount()
    res = []
    with open('../initialResult/wordCount.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        aDocWordCountList = strTemp.split(" ")
        del(aDocWordCountList[-1])
        tempList = []
        for value in aDocWordCountList:
            # results = value.split(":")
            res.append(value)
    return res

# res = getAllWordDocNoCount()
# print(len(res))
# res = getWordDocNoCount()
# k =0
# for v in res:
#     if k < 3:
#         print(v)
#         k  = k + 1
