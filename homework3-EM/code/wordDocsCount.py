#!/usr/bin/python3
# coding: utf-8

import os
import document
import dictionary
from collections import Counter
from collections import OrderedDict

def createWordDocCount():
    allFilesContent = document.getAllFilesContent()
    fname = "../initialResult/wordNumber.txt"
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
                        strWrite  += wordName + ":" + str(wordNum) + " "
                strWrite += "\r\n"
            index += 1
        f.write(strWrite)
        f.close()

def getWordDocCount():
    createWordDocCount()
    res = []
    with open('../initialResult/wordNumber.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        aDocWordCountList = strTemp.split(" ")
        del(aDocWordCountList[-1])
        tempList = []
        for value in aDocWordCountList:
            results = value.split(":")
            tempList.append(list(map(int, results)))
        res.append(tempList)
    return res

def getDict_DocCountWord():
    fname = "../initialResult/dict_DocCountWord.txt"
    res =  os.path.isfile(fname)
    result = []
    if res:
        with open(fname) as f:
            lines = f.read().splitlines()
        for line in lines:
            tempList = []
            ll = line.split(" ")
            # del(ll[-1])
            for item in ll:
                tempList.append( list(map(int, item.split(":"))))
            result.append(tempList)
    else:
        with open('../initialResult/wordNumber.txt') as f:
            lines = f.read().splitlines()
        f = open(fname, 'w')
        createWordDocCount()
        allDictionary = dictionary.getDictionary()

        for word in allDictionary:
            strWrite = ""
            doc_index = 0
            for line in lines:
                strTemp = ''.join(line.split("\r\n"))
                aDocWordCountList = strTemp.split(" ")
                del(aDocWordCountList[-1])

                for value in aDocWordCountList:
                    results = value.split(":")
                    if results[0] == word:
                        strWrite = strWrite + str(doc_index) + ":" + results[1] + " "
                doc_index = doc_index+1
            f.write(strWrite + "\r\n")
        f.close()
    return result

# res = getDict_DocCountWord()
# res = getWordDocCount()
# res = getDict_DocCountWord()
# print("len(res): " , len(res))
# print("len(res)[0]: " , len(res[0]))
# print("len(res)[0][0]: " , len(res[0][0]))
# print(type(res[0]))
# print(type(res[0][0]))
# print(type(res[0][0][0]))
# print(res[0])
# k =0
# for v in res:
#     if k < 3:
#         print(v)
#         k  = k + 1
