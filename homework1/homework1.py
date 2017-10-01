# coding: utf-8
import os
import hw1_0
import hw1_1

# stpe 0 : get the query list
queryFilesList = hw1_0.getQueryFilesList()
# print queryFilesList[0]

# step1 : get the dictionary
# allDictionary = hw1_1.getDictionary()
# print allDictionary

# for sub in queryFilesList[0]:
#     print sub
# print queryFilesList[0]


# step2 : document term weight
# TF: 每個query的每個單詞在某個文檔裏面出現次數
# [{"word in a query" : countInADocument, "document name": documentName},

# {"another word in a query" : countIn Another Document, "document name": documentName},
# ]
# IDF： 在所有文檔裏面，包含一個query的一個單詞的文檔有多少個，然後每個query的每個單詞


dTFs = []
path = "./data/Document"
files= os.listdir(path)
fileList = []
fileNameList = []
for file in files:
    f = open(path+"/"+file);
    iter_f = iter(f);
    strtemp = ""
    lineNumber = 1

    fileNameList.append(file)
    # print file

    for line in iter_f:
        if lineNumber > 3:
            # print "str.count(sub) : ", str.count(sub)
            strtemp = strtemp + line
        else:
          lineNumber = lineNumber + 1

    fileList.append(strtemp)

for sub in queryFilesList[0]:
    i = 0
    for fv in fileList:
        dTF = {}
        dTF["documentName"] = fileNameList[i]
        i = i + 1

        dTF[sub] = fv.count(sub)
        dTFs.append(dTF)

k =0
for v in dTFs:
    if k < 10:
        print v
        k  = k + 1

# print dTF
# print len(fileList)



#
# print "\n"

# step3 : query term weight
# TF: 每個query的每個單詞在 query 裏面出現次數

# step5 :
# document term weight 向量
# query term weight 向量

# step6 : 向量點乘

# step7 : 計算 cos

# step8 : 排序比較對於這個 query ，最接近的結果，也就是找到的 document 相似度

# step9: 找到所有的 query 的 排序結果
