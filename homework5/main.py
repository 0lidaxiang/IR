# coding: utf-8
import os

initialProcess = "./initialResult/"
if not os.path.exists(initialProcess):
    os.mkdir(initialProcess)

import queryList
import computeAqueryForADoc as compute

queryFilesList = queryList.getQueryFilesName()

print "------------------------------ Main Program Start ----------------"

resList = []
resultIndex = 0
for query in queryFilesList:
    queryResult = compute.computeAquery(resultIndex+1)
    print str(resultIndex+1).ljust(2) , " compute  " + query["fileName"] + " over. "

    oneLine = {}
    oneLine["queryName"] = query["fileName"]
    oneLine["content"] = ""
    for queryRes in queryResult:
        oneLine["content"] = oneLine["content"] + str(queryRes["fileName"]) + " "
    resList.append(oneLine)
    resultIndex += 1

resList.sort(key=lambda k: k['queryName'], reverse=False)

f = open("submission.txt" , 'w')
line1 = "Query,RetrievedDocuments"
f.write(line1 + "\r\n")

for value in resList:
    f.write(value["queryName"] + "," + value["content"] + "\r\n")

f.close()
print "------------------------------ Main Program  Over ----------------"
