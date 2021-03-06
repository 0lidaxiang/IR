#!/usr/bin/python3
# coding: utf-8

import numpy as np
import math
from datetime import datetime

import dictionary
import document
import wordDocsCount
import wordDocsNoCount

startInitial = datetime.now()

docList = document.getFilesName()
wordList = dictionary.getDictionary()
wNumber = len(wordList)
dNumber = len(docList) # 2265
topicNum = 10
P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
P_w_T = np.random.dirichlet(np.ones(topicNum),size= wNumber)
P_T_d = np.random.dirichlet(np.ones(dNumber),size= topicNum)
P_T_wd = np.zeros(shape=(topicNum * dNumber,wNumber))
count_w_d = wordDocsCount.getWordDocCount()
noCount_w_d = wordDocsNoCount.getWordDocNoCount()
dict_DocCountWord = wordDocsCount.getDict_DocCountWord()


def get_BG():
    fname = "./BGLM.txt"
    with open(fname) as f:
        lines = f.read().splitlines()
    res = []
    for line in lines:
        res.append(line.split())
    return res
bgList = get_BG()

def getQuery():
    fname = "./Query.txt"
    with open(fname) as f:
        lines = f.read().splitlines()
    res = []
    for line in lines:
        res.append(line.split())
    return res
bgList = getQuery()
