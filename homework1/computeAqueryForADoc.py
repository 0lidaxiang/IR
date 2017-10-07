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

def computeAquery(queryIndex, resultFileName):
    lineNum1 = 0
    qtfL = []
    idfL = []
    while lineNum1 < wordNumber:
        # qtfL.append(float(querTF[lineNum].split()[queryIndex]))  # for which query
        # idfL.append(float(idfList[lineNum].split()[1]))
        idfL.append(map(float, idfList[lineNum1].split())[1])
        qtfL.append(map(float, querTF[lineNum1].split())[queryIndex])

        lineNum1 += 1

    maxValQTF = max(qtfL)
    print "get qtfl over."

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

            # my 0.1, 2
            # socre : 55
            # documentWeight = (idfLogVal)
            # queryWeight =  math.log(1 + idf)

            # my 0.2, 2
            # socre : 55
            documentWeight = tf * idfLogVal
            queryWeight =  qtf * idfLogVal

            # my 0.2, 2
            # socre : 52
            # documentWeight = (tf * (1 + idfLogVal))
            # queryWeight =  qtf * idfLogVal

            # 1,1
            # socre : 50
            # documentWeight = (tf * idfLogVal)
            # queryWeight = (0.5 + ( (0.5 * qtf) / maxValQTF)) * idfLogVal

            # 1,2
            # socre : 50
            # documentWeight = (tf * idfLogVal)
            # queryWeight =  math.log(1 + idf)

            # 1,3
            # socre : 50
            # documentWeight = (tf * idfLogVal)
            # queryWeight = ( (1+qtf) * idfLogVal)

            # 2,1
            # socre : 30
            # documentWeight = (1 + tf)
            # queryWeight = (0.5 + ( (0.5 * qtf) / maxValQTF)) * idfLogVal

            # 2,2
            # socre : 30
            # documentWeight = (1 + tf)
            # queryWeight =  math.log(1 + idf)

            # 2,3
            # socre : 30
            # documentWeight = (1 + tf)
            # queryWeight = ( (1+qtf) * idfLogVal)

            # 3,1
            # socre : 40
            # documentWeight = ((1 + tf) * idfLogVal)
            # queryWeight =  (0.5 + ( (0.5 * qtf) / maxValQTF)) * idfLogVal

            # 3,2
            # socre : 40
            # documentWeight = ((1 + tf) * idfLogVal)
            # queryWeight =  math.log(1 + idf)

            # 3,3
            # socre : 45
            # documentWeight = ((1 + tf) * idfLogVal)
            # queryWeight = ( (1+qtf) * idfLogVal)

            documentWeightVec.append(documentWeight)
            queryWeightVec.append(queryWeight)
            lineNum += 1
        # print "get one document over."
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
        # print "get queryResult over."
    queryResult.sort(key=lambda k: k['cosVal'], reverse=True)

    f = open(resultFileName , 'w')
    for queryRes in queryResult:
        f.write(str(queryRes["fileName"]) + " " + str(queryRes["cosVal"]) + "\r\n")
    f.close()

    checkList = [
        "VOM19980225.0700.0585",
        "VOM19980303.0900.0396",
        "VOM19980303.0900.2198",
        "VOM19980304.0700.0737",
        "VOM19980304.0700.1058",
        "VOM19980305.0700.0703",
        "VOM19980305.0900.2093",
        "VOM19980306.0700.0971",
        "VOM19980311.0700.1487",
        "VOM19980326.0700.1793",
        "VOM19980523.0700.0189",
        "VOM19980621.0700.0565",
        "VOM19980630.0900.0230",
        ]
    indexQR = 1
    ansIndex = 1
    for qr in queryResult:
        if qr["fileName"] in checkList:
            print str(ansIndex) + " : " +  qr["fileName"] + "  " + str(indexQR)
            ansIndex+=1
        indexQR += 1


# res = computeAquery(14)
# print "len(res): " , len(res)
# k = 0
# for v in res:
#     if v["cosVal"] < 0.5:
#         if k < 5:
#             k+=1
#             print "query1 and document2 cos_val : " + str(v)
