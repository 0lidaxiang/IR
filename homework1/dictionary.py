# coding: utf-8

import os
import collections
import getFileList

def createDictionary():
    s = getFileList.getFilesListFromFile()
    fname = "dictionary.txt"
    res =  os.path.isfile(fname)
    if res:
        print fname + ' file has exists.'
    else:
        f = open(fname, 'w')
        all_the_text = "".join(str(x) for x in s)
        result = []
        for word in all_the_text.split():
            if word not in result:
                result.append(word)
                f.write(word + "\r\n")
        f.close()

def getDictionary():
    createDictionary()

    res = []
    with open('./dictionary.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

res = getDictionary()
print "len(res): " , len(res)

k =0
for v in res:
    if k < 10:
        print v
        k  = k + 1
