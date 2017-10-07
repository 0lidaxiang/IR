import os
import dictionary
import getFileList

def createDocumentTF():
    allDictionary = dictionary.getDictionary()
    fileList = getFileList.getFilesListFromFile()

    fname = 'documentTFResult.txt'
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        for sub in allDictionary:
            strWrite = sub + " "
            for fv in fileList:
                strWrite = strWrite + " "  + str(fv.count(sub))
            f.write(strWrite + "\n")
        f.close()
        # print " Write to " +fname + " file over."

def getDocumentTF():
    createDocumentTF()

    res = []
    with open('./documentTFResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(map(int, strTemp.split()) )
    return res

# res = getDocumentTF()
# print "len(res): " , len(res)
#
# k =0
# for v in res:
#     if k < 10:
#         print v
#         k  = k + 1
