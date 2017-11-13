#!/usr/bin/python3
# coding: utf-8
import os

initialProcess = "../initialResult/"
if not os.path.exists(initialProcess):
    os.mkdir(initialProcess)
    
# import numpy as np
# import math
# from datetime import datetime
#
# import dictionary
# import document
# import wordDocsCount
# import wordDocsNoCount
# import docLength
# import queryList

# def get_BG():
#     fname = "./BGLM.txt"
#     with open(fname) as f:
#         lines = f.read().splitlines()
#     res = []
#     for line in lines:
#         res.append(float(line.split()[1]))
#     return res
#
# docList = document.getFilesName()
# docLengthList = docLength.getDocLength()
# count_w_d = wordDocsCount.getWordDocCount()
# bgList = get_BG()
# queryL = queryList.getQueryFilesList()
