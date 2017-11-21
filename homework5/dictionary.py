# coding: utf-8

import os
import collections
import getFileList

def createDictionary():
    s = getFileList.getFilesListFromFile()
    fname = "./initialResult/dictionary.txt"
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        all_the_text = "".join(str(x) for x in s)
        result = []
        for word in all_the_text.split():
            if word not in result:
                result.append(word)
        result = list(map(int, result))
        result.sort()
        for word in result:
            f.write(str(word) + "\r\n")
        f.close()

def getDictionary():
    createDictionary()
    res = []
    with open('./initialResult/dictionary.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        # strTemp = ''.join(.split("\r\n"))
        res.append(int(line))
    return res

# res = getDictionary()
# print ("len(res): " , len(res))
# k =0
# for v in res:
#     if k < 10:
#         print (v)
#         k  = k + 1
