import os
import getFileList
import jieba
import math
import idfResult
import numpy as np

def utf8StopDic():
    fw = open("./data/stoplis_utf8.txt", 'w')
    with open('./data/stoplis.txt', encoding="gbk", errors='ignore') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        fw.write(strTemp + "\n")
    fw.close()

def getStopDictionary():
    res = []
    with open('./data/stoplis.txt', encoding="utf8", errors='ignore') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

def utf8Dic():
    stoplis_utf8 = getStopDictionary()
    fw = open("./data/dictionary_1_utf8.txt", 'w')
    with open('./data/dictionary.txt', encoding="gbk", errors='ignore') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        if strTemp not in stoplis_utf8:
            fw.write(strTemp + "\n")
    fw.close()

def getDictionary():
    res = []
    with open('./data/dictionary_utf8.txt', encoding="utf8", errors='ignore') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res



allDictionary = getDictionary()

def computeTFIDF(file1Path , file2Path):
    jieba.load_userdict("./data/dictionary_utf8.txt")
    allDocsL = getFileList.getFilesListFromFile()

    idfResultL = idfResult.getIDF()

    file1 = getFileList.getAFile(file1Path)
    file2 = getFileList.getAFile(file2Path)

    file1_list = list(jieba.cut(file1, cut_all=False))
    file2_list = list(jieba.cut(file2, cut_all=False))
    file1_matrix = []
    file2_matrix = []
    allDocumentsNum = 17901 # 9 * 1989
    dicc_index = 0
    for dicc in allDictionary:
        dIDFsub = int(idfResultL[dicc_index])
        if dIDFsub > 0:
            tf1 = file1_list.count(dicc)
            tf2 = file2_list.count(dicc)
            idfNum = math.log(allDocumentsNum * 1.0 / dIDFsub)
            file1_matrix.append(tf1 * idfNum)
            file2_matrix.append(tf2 * idfNum)
        else:
            file1_matrix.append(0)
            file2_matrix.append(0)

        # print(dicc_index)
        dicc_index += 1

    a = np.array(file1_matrix)
    b = np.array(file2_matrix)
    aL = np.sqrt(a.dot(a))
    bL = np.sqrt(b.dot(b))

    x = np.dot(a,b)
    y = aL * bL
    cosVal = 0
    if y > 0:
        cosVal = x / y
    return cosVal

utf8StopDic()
utf8Dic()


filesNameList = getFileList.getFileNameList()
for file1Name in filesNameList:
    for file2Name in filesNameList:
        if file1Name != file2Name:
            parentPath = "./data/Document/"
            res =  computeTFIDF(parentPath + file1Name, parentPath + file2Name)
            print( file1Name + " and " + file2Name + " files's cos_value is : " , res)
