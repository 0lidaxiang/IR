# coding: utf-8
import os
import math
import numpy as np

import dictionary
import documentTF
import idfResult
import getQuerysList
import getFileList

def getQueryTF():
    # createQueryTFFile()
    res = []
    with open('./initialResult/queryTF.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(list(map(int, strTemp.split() )) )
    return res

allDictionary = dictionary.getDictionary()
wordNumber = len(allDictionary)
idfList = idfResult.getIDF()
numberOfDoc = 2265

docTF = documentTF.getDocumentTF()
querTF = getQueryTF()
fileNameList = getFileList.getFileNameList()
queryFilesList = getQuerysList.getIntsFromFile()
docsList = getFileList.getIntsFromFile()

print(" initialResult -------------- ")
def computeAquery(queryIndex):
    i = 0
    queryResult = []
    qtfL = []

    # lineNum1 = 0
    # while lineNum1 < wordNumber:
    #     qtfL.append(querTF[lineNum1][queryIndex])
    #     lineNum1 += 1

    while i < numberOfDoc:
        documentWeightVec = []
        queryWeightVec = []

        lineNum = 0
        while lineNum < wordNumber:
            tf = docTF[lineNum][i]
            idf = idfList[lineNum]
            qtf = querTF[lineNum][queryIndex]
            idfLogVal = math.log(idf)
            # 3,3
            documentWeight = tf * idfLogVal
            queryWeight = qtf * idfLogVal

            documentWeightVec.append(documentWeight)
            queryWeightVec.append(queryWeight)
            lineNum += 1
        a = np.array(queryWeightVec)
        b = np.array(documentWeightVec)
        aL = np.sqrt(a.dot(a))
        bL = np.sqrt(b.dot(b))

        x = np.dot(a,b)
        y = aL * bL
        cosVal = x / y

        tempStr = {"fileName" : "" , "cosVal" : 0}
        thisFileName = fileNameList[i]
        tempStr["fileName"] = thisFileName
        tempStr["cosVal"] = cosVal
        queryResult.append(tempStr)
        i+=1
    # queryResult.sort(key=lambda k: k['cosVal'], reverse=True)
    return queryResult

resultIndex = 0
queryNames = getQuerysList.getFileNameList()
f = open("tFIDF_result.txt" , 'w')
print(" ----------------- Start compute ------------------ ")
for query in queryNames:
    queryResult = computeAquery(resultIndex)
    print (str(resultIndex+1).ljust(2) , " compute  " + query + " over. ")

    f.write(query + ",")
    for queryRes in queryResult:
        f.write(queryRes["fileName"] + ":" +  str(queryRes["cosVal"]) + ",")
    f.write("\n")
    resultIndex += 1
f.close()
print(" ----------------- Finish compute ------------------ ")
