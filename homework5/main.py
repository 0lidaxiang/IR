# coding: utf-8
import os
from datetime import datetime

answer = np.ones(shape=(wordsNum, 100))
# answer = keras.getAnswers()
# compute sim by cos_val
queryFilesList = getQueryFiles()
docsList = getFilesList.getFilesListFromFile()

print("docs_weight start compute ------------------ ")
startTime = datetime.now()
docs_weight = []
for doc in docsList:
    doc_weight = 0
    doc_length = len(doc)
    for word in doc_length:
        doc_weight += c_w_d * keras.getAnswer(word) / doc_length
        pass
    docs_weight.append(doc_weight)
print("docs_weight finish compute , the excution time is : " + str(datetime.now() - startTime).split(".")[0])

print("querys_weight start compute ------------------ ")
startTime = datetime.now()
querys_weight = []
for queryFile in queryFilesList:
    query_weight = 0
    query_length = len(queryFile)
    for word in query_length:
        query_weight += c_w_d * keras.getAnswer(word) / query_length
        pass
    querys_weight.append(query_weight)
print("querys_weight finish compute , the excution time is : " + str(datetime.now() - startTime).split(".")[0])

print(" ------------------ sim start compute and write result ------------------ ")
startTime = datetime.now()
fs = open("submission_sorted.txt" , 'w')
queryNamesList = getQueryNamesList()
for queryName in queryNamesList:
    oneQueryResult = []
    for doc_weight in docs_weight:
        oneLine = {}
        a = np.array(querys_weight)
        b = np.array()
        aL = np.sqrt(a.dot(a))
        bL = np.sqrt(b.dot(b))
        cosVal = (np.dot(a,b)) / (aL * bL)
        oneLine["fileName"] = thisFileName
        oneLine["cosVal"] = cosVal
        oneQueryResult.append(oneLine)

        # oneQueryResult += str(cosVal)
    oneQueryResult.sort(key=lambda k: k['cosVal'], reverse=True)
    fs.write(query["fileName"].join(oneQueryResult))
fs.close()
print("------------------ sim start compute and write result over , the excution time is : " + str(datetime.now() - startTime).split(".")[0] + "\n")
