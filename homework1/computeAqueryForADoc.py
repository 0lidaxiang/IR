# coding: utf-8
import os
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

def computeAquery(queryIndex, resultFileName):
    docTF = documentTF.getDocumentTF()
    querTF = queryTF.getQueryTF()
    fileNameList = getFileList.getFileNameList()

    qtfindex = 0
    qtfL = []
    idfL = []
    while qtfindex < wordNumber:
        qtfL.append(float(querTF[qtfindex].split()[queryIndex]))  # for which query
        idfL.append(float(idfList[qtfindex].split()[1]))
        qtfindex += 1

    i = 0
    query1Result = []
    f = open(resultFileName , 'w')
    while i < numberOfDoc:

        document2WeightVec = []
        query1WeightVec = []

        index = 0
        while index < wordNumber:
            tf = float(docTF[index].split()[i+1])  # the i+1 document tf
            idf = idfL[index]
            document2Weight = ((1 + tf) * idf)
            document2WeightVec.append(document2Weight)

            qtf = qtfL[index]
            query1Weight = ((1 + qtf) * idf)
            query1WeightVec.append(query1Weight)
            index += 1

        a = np.array(query1WeightVec)
        b = np.array(document2WeightVec)
        aL = np.sqrt(a.dot(a))
        bL = np.sqrt(b.dot(b))

        x = np.dot(a,b)
        y = aL * bL
        cosVal = x / y

        tempStr = {"fileName" : "" , "cosVal" : 1}
        thisFileName = fileNameList[i]
        tempStr["fileName"] = thisFileName
        tempStr["cosVal"] = cosVal
        query1Result.append(tempStr)
        f.write(thisFileName + " " + str(cosVal) + "\r\n")
        i+=1

    query1Result.sort(key=lambda k: k['cosVal'], reverse=True)

    queryFilesList1 = queryList.getQueryFilesList()
    # return query1Result

# res = computeAquery(14)
# print "len(res): " , len(res)
# k = 0
# for v in res:
#     if v["cosVal"] < 0.5:
#         if k < 5:
#             k+=1
#             print "query1 and document2 cos_val : " + str(v)
