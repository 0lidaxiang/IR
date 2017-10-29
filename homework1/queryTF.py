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
        for sub in allDictionary:
            strWrite = sub
            for v in tempQueryList:
                strWrite = strWrite + " "  + str(v["content"].split().count(sub))
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
