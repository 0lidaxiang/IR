#!/usr/bin/python3
# coding: utf-8

import os
import document

def createDocLength():
    fname = "./initialResult/docLength.txt"
    allFilesContent = document.getAllFilesContent()
    res = os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        for doc in allFilesContent:
            docLength = str(len(doc.split(" "))) + "\r\n"
            f.write(docLength)
        f.close()

def getDocLength():
    fname = "./initialResult/docLength.txt"
    res1 =  os.path.isfile(fname)
    if res1:
        pass
    else:
        createDocLength()
    res = []
    with open(fname) as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(int(strTemp))
    return res

# res = getDocLength()
# print("len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 10:
#         print(v)
#         k  = k + 1
