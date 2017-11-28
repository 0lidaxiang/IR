# coding: utf-8
import os

def getTF_IDF():
    # createQueryTFFile()
    res = []
    with open('./tFIDF_result.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        # strTemp = ''.join(line.split("\r\n"))
        lineL = line.split(",")
        cos_valList = []
        for i in range(1, len(lineL) -1):
            # print(lineL)
            # print(type(lineL[i].split(":")), len(lineL[i].split(":")))
            cos_valList.append(float(lineL[i].split(":")[1]))
        res.append(cos_valList)
    return res

# res = getTF_IDF()
# print("len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 1:
#         print(len(v) , type(v))
#         k  = k + 1
