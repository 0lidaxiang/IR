import os
import dictionary
import getQuerysList

def createQueryTFFile():
    allDictionary = dictionary.getDictionary()
    fname = './initialResult/queryTF.txt'
    res =  os.path.isfile(fname)

    if res:
        pass
    else:
        tempQueryList = getQuerysList.getIntsFromFile()
        f = open(fname, 'w')
        for sub in allDictionary:
            strWrite = str(sub)
            for v in tempQueryList:
                c_wd = v.count(sub)
                strWrite += " " + str(c_wd)
            f.write(strWrite + "\n")
        f.close()


# def getQueryTF():
#     createQueryTFFile()
#     res = []
#     with open('./initialResult/queryTF.txt') as f:
#         lines = f.read().splitlines()
#     for line in lines:
#         strTemp = ''.join(line.split("\r\n"))
#         res.append(list(map(int, strTemp.split() )) )
#     return res

# res = getQueryTF()
# print("len(res): " , len(res))

# k =0
# for v in res:
#     if k < 1:
#         print(v)
#         k  = k + 1
