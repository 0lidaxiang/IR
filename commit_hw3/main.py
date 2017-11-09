#!/usr/bin/python3
# coding: utf-8

import numpy as np
import math
from datetime import datetime

import dictionary
import document
import wordDocsCount
import wordDocsNoCount
import docLength
import queryList

def get_BG():
    fname = "./BGLM.txt"
    with open(fname) as f:
        lines = f.read().splitlines()
    res = []
    for line in lines:
        res.append(float(line.split()[1]))
    return res

docList = document.getFilesName()
docLengthList = docLength.getDocLength()
count_w_d = wordDocsCount.getWordDocCount()
bgList = get_BG()
queryL = queryList.getQueryFilesList()

allQueryRes = []
for q in range(len(queryL)):
    nowQuery = queryL[q]["content"]
    alpha = 0.4
    beta = 0.1
    queryOfDoc = 0
    queryDocsList = []
    for j in range(len(docLengthList)):
        aDoc = []
        for i in range(len(nowQuery)):
            cwd = 0
            para1 = -1E10
            for ww in count_w_d[j]:
                if ww[0] == int(nowQuery[i]):
                    cwd = ww[1]
                    para1 = math.log((alpha * cwd) / docLengthList[j])
            para2 = math.log((1-alpha - beta)) + bgList[int(nowQuery[i])]
            aDoc.append(para1)
            aDoc.append(para2)
        ss = {"name" : docList[j], "value" : float(np.logaddexp.reduce(aDoc))}
        queryDocsList.append(ss)
    queryDocsList.sort(key=lambda k: k['value'], reverse=True)
    strTemp = ""
    for value in queryDocsList:
        strTemp += value["name"] + " "
    oneQuery = {"queryName" : queryL[q]["fileName"], "content": strTemp}
    print(queryL[q]["fileName"])
    allQueryRes.append(oneQuery)

f = open("./submission.txt" , 'w')
line1 = "Query,RetrievedDocuments"
f.write(line1 + "\r\n")

for value in allQueryRes:
    f.write(value["queryName"] + "," + value["content"] + "\r\n")
f.close()
