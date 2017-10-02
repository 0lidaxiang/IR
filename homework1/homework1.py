# coding: utf-8
import os
import hw1_0
import hw1_1

# stpe 0 : get the query list
queryFilesList = hw1_0.getQueryFilesList()
# print queryFilesList[0]

# step1 : get the dictionary
allDictionary = hw1_1.getDictionary()
# print allDictionary


# step2 : document term weight
# TF: 字典裏 的每個單詞在某個文檔裏面出現次數
# [{"word name " :  documentName - list[{documentName : wordOccursTimes}]},
# ]
# IDF： 在所有文檔裏面，包含字典裏 的一個單詞的文檔有多少個，然後每個query的每個單詞
# [{"word in a query" : document number that contains this word},
# ]

print "---------- get allDictionary ----------------"


path = "./data/Document"
files= os.listdir(path)
fileList = []
fileNameList = []
for fileName in files:
    f = open(path+"/"+fileName);
    iter_f = iter(f);
    strtemp = ""
    lineNumber = 1

    fileNameList.append(fileName)

    for line in iter_f:
        if lineNumber > 3:
            strtemp = strtemp + line
        else:
          lineNumber = lineNumber + 1
    fileList.append(strtemp)

print "---------- get fileList ----------------"


dTFs = []
dIDFs = []
for sub in allDictionary:
    dIDF = {}
    dIDF[sub] = 0

    dTF = {}
    dTFLists = []

    i = 0
    for fv in fileList:
        dTFList = {}
        # dTF[sub] = fv.count(sub)
        # dTF["documentName"] = fileNameList[i]
        dTFList[fileNameList[i]] = fv.count(sub)
        i = i + 1
        dTFLists.append(dTFList)
        # print type(dTFLists) , dTFLists
        # print "\n"

        if sub in fv:
            dIDF[sub] = dIDF[sub] + 1
    dIDFs.append(dIDF)

    dTF[sub] = dTFLists
    # print "---------- get dTF" + str(y)  , dTF,  "----------------"
    # y= y + 1

    # dTF[sub] = len(dTFLists)
    dTFs.append(dTF)

print "----------start print result1 ----------------"
k =0
for v in dTFs:
    if k < 10:
        print v
        k  = k + 1

print "----------start print result2 ----------------"

k =0
for v in dIDFs:
    if k < 10:
        print v
        k  = k + 1

print len(dTFs)
print len(dIDFs)
# print "\n"



# step3 : query term weight
# TF: 字典的每個單詞在 query 裏面出現次數

# step5 :
# document term weight 向量
# query term weight 向量

# step6 : 向量點乘

# step7 : 計算 cos

# step8 : 排序比較對於這個 query ，最接近的結果，也就是找到的 document 相似度

# step9: 找到所有的 query 的 排序結果
