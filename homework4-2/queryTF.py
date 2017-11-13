import os
import dictionary
import queryList

def createQueryTFFile():
    allDictionary = dictionary.getDictionary()
    fname = './initialResult/queryTF.txt'
    res =  os.path.isfile(fname)

    if res:
        pass
    else:
        tempQueryList = queryList.getQueryFilesList()
        f = open(fname, 'w')
        for sub in range(0, 51253):
            strWrite = sub
            for v in tempQueryList:
                c_w = v.count(sub)
                if c_w > 0:
                    strWrite = strWrite + " "  + str(c_w)
            f.write(strWrite + "\n")
        f.close()

def getQueryTF():
    createQueryTFFile()

    res = []
    with open('./initialResult/queryTF.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res
