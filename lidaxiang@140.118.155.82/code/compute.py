#!/usr/bin/python3
# coding: utf-8

import os
import document

wTMatrix = []
TdMatrix = []
def createDictionary():
    s = document.getAllFilesContent()
    fname = "../initialResult/dictionary.txt"
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
