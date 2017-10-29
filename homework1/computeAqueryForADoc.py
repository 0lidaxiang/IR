# coding: utf-8
import os
import math
import numpy as np

import queryList
import dictionary
import documentTF
import queryTF
import idfResult
import getFileList

allDictionary = dictionary.getDictionary()
wordNumber = len(allDictionary)
idfList = idfResult.getIDF()
numberOfDoc = 2265

docTF = documentTF.getDocumentTF()
querTF = queryTF.getQueryTF()
fileNameList = getFileList.getFileNameList()

def computeAquery(queryIndex):
    lineNum1 = 0
    qtfL = []
    idfL = []
    while lineNum1 < wordNumber:
        idfL.append(map(float, idfList[lineNum1].split())[1])
        qtfL.append(map(float, querTF[lineNum1].split())[queryIndex])

        lineNum1 += 1

    maxValQTF = max(qtfL)

    i = 0
    queryResult = []

    while i < numberOfDoc:
        documentWeightVec = []
        queryWeightVec = []

        lineNum = 0
        while lineNum < wordNumber:
            tf = docTF[lineNum][i+1]  # the i+1 document tf
            idf = idfL[lineNum]
            qtf = qtfL[lineNum]

            idfLogVal = math.log(idf)

            # 3,3
            documentWeight = (1 + tf) * idfLogVal
            queryWeight = ( (1+qtf) * idfLogVal)

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
    queryResult.sort(key=lambda k: k['cosVal'], reverse=True)
    return queryResult
