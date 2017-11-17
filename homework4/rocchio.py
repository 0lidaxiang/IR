# coding: utf-8
import os
import math
import numpy as np
import time

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

def rocchio_algorithm(queryIndex):
    lineNum1 = 0
    qtfL = []
    idfL = []
    while lineNum1 < wordNumber:
        idfL.append(map(float, idfList[lineNum1].split())[1])
        qtfL.append(map(float, querTF[lineNum1].split())[queryIndex])
        lineNum1 += 1

    Alpha = 1.0
    Beta = 0.75
    secondTerms = np.zeros(shape=(wordNumber))
    relavantDocs = getRelavantDocs(queryIndex)
    for docName in relavantDocs[1:15]:
        fileL = getAFileList(docName)
        irelavantDocIDF = 0
        for sub in allDictionary:
            secondTerms[irelavantDocIDF] += (1+ fileL.count(sub)) * math.log(idfL[irelavantDocIDF])
            irelavantDocIDF+=1
    secondTerms = secondTerms / 14.0

    queryResult = []
    i = 0
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
        a = np.array(queryWeightVec)*Alpha + Beta * secondTerms
        b = np.array(documentWeightVec)
        aL = np.sqrt(a.dot(a))
        bL = np.sqrt(b.dot(b))
        x = np.dot(a,b)
        y = aL * bL
        # cosVal = x / y
        cosVal = math.log(x) - math.log(y)

        tempStr = {"fileName" : "" , "cosVal" : 0}
        thisFileName = fileNameList[i]
        tempStr["fileName"] = thisFileName
        tempStr["cosVal"] = cosVal
        queryResult.append(tempStr)
        i+=1
    queryResult.sort(key=lambda k: k['cosVal'], reverse=True)
    return queryResult[0:102]

def getAFileList(fileName):
    path = "./data/Document"
    files= os.listdir(path)
    fileList = []
    f = open(path+"/"+fileName);
    iter_f = iter(f);
    strtemp = ""
    lineNumber = 1

    for line in iter_f:
        if lineNumber > 3:
            strtemp = strtemp + line.rstrip("-1\r\n")
        else:
          lineNumber = lineNumber + 1
    fileList.append(strtemp)
    return strtemp.split()

def getRelavantDocs(queryIndex):
    with open('./submission_1.txt') as f:
        lines = f.read().splitlines()
    Docs = []
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        Docs.append(strTemp.split()[0:15])
    return Docs[queryIndex-1]

# res = getRelavantDocs(1-1)
# print "len(res): " , len(res)
# print(res)
# k =0
# for v in res:
#     if k < 3:
#         print v
#         k  = k + 1
