import os
import dictionary
import queryList

def createQueryTFFile():
    allDictionary = dictionary.getDictionary()
    oneQuery = queryList.getQueryFilesList()[0]

    fname = 'queryTFResult.txt'
    res =  os.path.isfile(fname)
    if res:
        print fname + ' file has exists.'
    else:
        f = open(fname, 'w')
        for sub in allDictionary:
            strWrite = sub + " "  + str(oneQuery.count(sub))
            f.write(strWrite + "\n")
        f.close()
        print "Write to file over."

def getQueryTF():
    createQueryTFFile()

    res = []
    with open('./queryTFResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

res = getQueryTF()
print len(res)
k =0
for v in res:
    if k < 10:
        print v
        k  = k + 1
