# coding: utf-8
import os
from datetime import datetime
import h5py
import numpy as np
import math

import dictionary
import getQuerysList
import getFileList
import idfResult

def getTF_IDF():
    # createQueryTFFile()
    res = []
    with open('./tFIDF_result.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        # strTemp = ''.join(line.split("\r\n"))
        lineL = line.split(",")
        cos_valList = []
        for i in range(1, len(lineL) -1):
            # print(lineL)
            # print(type(lineL[i].split(":")), len(lineL[i].split(":")))
            cos_valList.append(float(lineL[i].split(":")[1]))
        res.append(cos_valList)
    return res

def getWeightFromHd5(weight_file_path):
    f = h5py.File(weight_file_path)
    try:
        if len(f.items())==0:
            print("len(f.items())", len(f.items()))
            return
        embeddings = f["embedding_1"]["embedding_1"]["embeddings:0"]
        return np.array(embeddings)
    finally:
        f.close()

# answer = getWeightFromHd5("./" + "39281-393018_2017-11-25 11:16:36.h5")
# answer = getWeightFromHd5("./" + "1-393018_2017-11-30 18:07:33.h5")
answer = getWeightFromHd5("./" + "1-2500-393018_2017-11-30 18:07:33.h5")

print("start compute querys_weight，docs_weight ------------------ ")
# compute sim by cos_val
queryFilesList = getQuerysList.getIntsFromFile()
docsList = getFileList.getIntsFromFile()
dic = dictionary.getDictionary()
startTime = datetime.now()
docs_weight = []
for doc in docsList:
    doc_length = len(doc)
    doc_weight = np.zeros(shape=(100, ))
    for word in doc:
        c_w_d = doc.count(word)
        now_doc_weight = c_w_d * answer[dic.index(word)] / doc_length
        doc_weight = doc_weight + now_doc_weight
    docs_weight.append(doc_weight)

querys_weight = []
for queryFile in queryFilesList:
    query_length = len(queryFile)
    query_weight = np.zeros(shape=(100, ))
    for word in queryFile:
        c_w_d = queryFile.count(word)
        if word in dic:
            now_query_weight = c_w_d * answer[dic.index(word)]  / query_length
            query_weight = query_weight + now_query_weight
    querys_weight.append(query_weight)
print("finish compute querys_weight，docs_weight , the excution time is : " + str(datetime.now() - startTime).split(".")[0])

# print("\n ------------------ sim start compute and write result ------------------ ")
startTime = datetime.now()
TFIDF = getTF_IDF()
fs = open("submission_TFIDF_MAP100.txt" , 'w')
docsNameList = getFileList.getFileNameList()
fs.write("Query,RetrievedDocuments" + "\n")
query_index = 1
for query_weight in querys_weight:
    oneQueryResult = []
    doc_index = 0
    a = np.array(query_weight)
    aL = np.sqrt(a.dot(a))

    # doc_index = 0
    for doc_weight in docs_weight:
        oneLine = {}
        b = np.array(doc_weight)
        bL = np.sqrt(b.dot(b))
        dem = ( aL * bL)
        cosVal = 1
        if dem != 0:
            cosVal = (np.dot(a,b)) / dem
        oneLine["fileName"] = docsNameList[doc_index]
        oneLine["cosVal"] = cosVal + 5 * TFIDF[query_index - 1][doc_index]
        oneQueryResult.append(oneLine)
        doc_index += 1
    oneQueryResult.sort(key=lambda k: k['cosVal'], reverse=True)

    queryFileName = "50" + str(query_index).zfill(3) + ".query"
    querySortedRes = ""
    for dicc in oneQueryResult[0:100]:
        querySortedRes += dicc["fileName"] +" "
        # querySortedRes += str(dicc["cosVal"]) +" "
    fs.write(queryFileName + "," + querySortedRes + "\n")
    query_index += 1
fs.close()
print("finish compute and write sim-result , the excution time is : " + str(datetime.now() - startTime).split(".")[0] + "\n")
