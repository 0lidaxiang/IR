# coding: utf-8
import os
import time
from datetime import datetime

import rocchio
import queryList
import computeAqueryForADoc as compute

initialProcess = "./initialResult/"
if not os.path.exists(initialProcess):
    os.mkdir(initialProcess)
queryFilesList = queryList.getQueryFilesName()[0:10]

f = open("submission-" + datetime.now().strftime("%m_%d_%H_%M_%S_%f") + ".txt" , 'w')
line1 = "Query,RetrievedDocuments"
f.write(line1 + "\r\n")

print "------------------------------ Main Program Start ----------------"
start_time = datetime.now()
# resList = []
resultIndex = 0
for query in queryFilesList:
    queryResult = rocchio.rocchio_algorithm(resultIndex+1)
    print str(resultIndex+1).ljust(2) , " compute  " + query["fileName"] + " over. "

    oneLine = {}
    # oneLine["queryName"] = query["fileName"]
    queryRelavantDocs = ""
    for queryRes in queryResult:
        queryRelavantDocs += str(queryRes["fileName"]) + " "
    f.write(queryRes["fileName"] + "," + queryRelavantDocs + "\r\n")
    # resList.append(oneLine)
    resultIndex += 1

# resList.sort(key=lambda k: k['queryName'], reverse=False)

print(str(resultIndex) + " querys excution time is %10s ." % str(datetime.now() -start_time).split(".")[0])

# for value in resList:
#     f.write(value["queryName"] + "," + value["content"] + "\r\n")
f.close()

res = []
with open(fname) as f:
    lines = f.read().split("\r\n")
for line in lines:
    strTemp = ''.join(line)
    res.append(strTemp)
del(res[0])
res.sort(reverse=False)

fs = open("submission_sorted.txt" , 'w')
line1 = "Query,RetrievedDocuments"
fs.write(line1)
for value in res:
    fs.write(value + "\r\n")
fs.close()
print "------------------------------ Main Program  Over ----------------"
