import os
import dictionary
import queryList

def createQueryTFFile():
    allDictionary = dictionary.getDictionary()
    fname = 'queryTFResult.txt'
    res =  os.path.isfile(fname)

    if res:
        # print fname + ' file has exists.'
        pass
    else:
        tempQueryList = queryList.getQueryFilesList()
        f = open(fname, 'w')
        for sub in allDictionary:
            strWrite = sub
            for v in tempQueryList:
                strWrite = strWrite + " "  + str(v["content"].count(sub))
            f.write(strWrite + "\n")
        f.close()

def getQueryTF():
    createQueryTFFile()

    res = []
    with open('./queryTFResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

# res = getQueryTF()
# print len(res)
# k =0
# for v in res:
#     if k < 10:
#         print v
#         k  = k + 1
#
# print "\n\n"
# print queryList.getQueryFilesList()[0]
