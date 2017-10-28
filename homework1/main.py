# coding: utf-8
import os
import numpy as np

initialProcess = "./initialResult/"
if not os.path.exists(initialProcess):
    os.mkdir(initialProcess)

import queryList
import computeAqueryForADoc as compute

queryFilesList = queryList.getQueryFilesName()

print "------------------------------ Main Program Start ----------------"

resultIndex = 5
queryResult = compute.computeAquery(resultIndex+1)
query = queryFilesList[resultIndex+1]
print str(resultIndex+1).ljust(2) , " compute  " + query["fileName"] + " over. "


# f = open("submission.txt" , 'w')
# line1 = "Query,RetrievedDocuments"
# f.write(line1 + "\r\n")
# resultIndex = 0
# for query in queryFilesList:
#     queryResult = compute.computeAquery(resultIndex+1)
#     print str(resultIndex+1).ljust(2) , " compute  " + query["fileName"] + " over. "
#
#     oneLine = query["fileName"] + ","
#     for queryRes in queryResult:
#         oneLine = oneLine + str(queryRes["fileName"]) + " "
#     f.write(oneLine + "\r\n")
#
#     resultIndex += 1
#
# f.close()
print "------------------------------ Main Program  Over ----------------"
