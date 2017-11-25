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

# answer = getWeightFromHd5("./" + "my_model-948-393018_2017-11-23 22:08:23.h5")
answer = getWeightFromHd5("./" + "39299-393018_2017-11-24 14:22:03.h5")

print("answer type and shape: ", type(answer), answer.shape, "\n")

# compute sim by cos_val
queryFilesList = getQuerysList.getIntsFromFile()
docsList = getFileList.getIntsFromFile()
dic = dictionary.getDictionary()
idf =  idfResult.getIDF()

print("docs_weight start compute ------------------ ")
startTime = datetime.now()
docs_weight = []

for doc in docsList:
    doc_length = len(doc)
    doc_weight = np.zeros(shape=(100, ))
    for word in doc:
        c_w_d = doc.count(word)
        now_doc_weight = c_w_d * answer[dic.index(word)] / doc_length
        # if c_w_d == 0:
            # print(c_w_d, answer[dic.index(word)], now_doc_weight, "\n")
        doc_weight = doc_weight + 1.0* now_doc_weight +  math.log(idf[dic.index(word)])
    # doc_weight = doc_weight / doc_length
    docs_weight.append(doc_weight)
print("docs_weight: ", type(docs_weight) , len(docs_weight))
print("docs_weight finish compute , the excution time is : " + str(datetime.now() - startTime).split(".")[0])

print("querys_weight start compute ------------------ ")
start_query_Time = datetime.now()
querys_weight = []
for queryFile in queryFilesList:
    query_length = len(queryFile)
    query_weight = np.zeros(shape=(100, ))
    # wordIndex = 0
    for word in queryFile:
        c_w_d = queryFile.count(word)
        if word in dic:
            now_query_weight = c_w_d * answer[dic.index(word)]  / query_length
            # if c_w_d == 0:
                # print(c_w_d, answer[dic.index(word)], now_query_weight, "\n")
            query_weight = query_weight +  1. *now_query_weight +  math.log(idf[dic.index(word)])
    # query_weight = query_weight / query_length
    querys_weight.append(query_weight)
print("querys_weight: ", type(querys_weight) , len(querys_weight))
print("querys_weight finish compute , the excution time is : " + str(datetime.now() - start_query_Time).split(".")[0])

# print(docs_weight[0], docs_weight[0].shape)
# print(querys_weight[0], querys_weight[0].shape)
# print(answer[0], answer[0].shape)

print("\n ------------------ sim start compute and write result ------------------ ")
startTime = datetime.now()
fs = open("submission_TFIDF_MAP100.txt" , 'w')
docsNameList = getFileList.getFileNameList()

fs.write("Query,RetrievedDocuments" + "\n")
query_index = 1
for query_weight in querys_weight:
    oneQueryResult = []
    res_index = 0
    a = np.array(query_weight)
    aL = np.sqrt(a.dot(a))

    for doc_weight in docs_weight:
        oneLine = {}
        b = np.array(doc_weight)
        bL = np.sqrt(b.dot(b))
        mem = np.dot(a,b)
        dem = aL * bL
        cosVal = 0
        if dem != 0:
            cosVal = mem / dem
        oneLine["fileName"] = docsNameList[res_index]
        oneLine["cosVal"] = cosVal
        oneQueryResult.append(oneLine)
        res_index += 1
    oneQueryResult.sort(key=lambda k: k['cosVal'], reverse=True)

    queryFileName = "50" + str(query_index).zfill(3) + ".query"
    querySortedRes = ""
    for dicc in oneQueryResult[0:100]:
        querySortedRes += dicc["fileName"] +" "
        # querySortedRes += str(dicc["cosVal"]) +" "
    fs.write(queryFileName + "," + querySortedRes + "\n")
    query_index += 1
fs.close()
print("------------------ sim start compute and write result over , the excution time is : " + str(datetime.now() - startTime).split(".")[0] + "\n")