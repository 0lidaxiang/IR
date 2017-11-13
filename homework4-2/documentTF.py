import os
import getFileList

def createDocumentTF():
    fileList = getFileList.getFilesListFromFile()

    fname = './initialResult/documentTFResult.txt'
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        for sub in range(0, 51253):
            strWrite = ""
            for fv in fileList:
                c_w = fv.count(sub)
                if c_w > 0:
                    strWrite = strWrite + " "  + str(c_w)
            f.write(strWrite + "\n")
        f.close()

def getDocumentTF():
    createDocumentTF()

    res = []
    with open('./initialResult/documentTFResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        res.append(list(map(int, line.split())) )
    return res

# res = getDocumentTF()
# print("len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 100:
#         print(v)
#         k  = k + 1
