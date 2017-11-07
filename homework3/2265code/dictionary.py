#!/usr/bin/python3
# coding: utf-8

import os
import document

def createDictionary():
    s = document.getAllFilesContent()
    os.mkdir("../2265initialResult")
    fname = "../2265initialResult/dictionary.txt"
    res =  os.path.isfile(fname)

    if res:
        pass
    else:
        f = open(fname, 'w')
        all_the_text = "".join(str(x) for x in s)
        wordSet = set()
        for word in all_the_text.split():
                wordSet.add(word)
        f.write("\r\n".join(wordSet))
        f.close()

def getDictionary():
    fname = '../2265initialResult/dictionary.txt'
    res1 =  os.path.isfile(fname)
    if res1:
        pass
    else:
        createDictionary()

    res = []
    with open(fname) as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

# res = getDictionary()
# print("len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 10:
#         print(v)
#         k  = k + 1
