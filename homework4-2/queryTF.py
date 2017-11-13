import os
import queryList

def createQueryTFFile():
    fname = './initialResult/queryTF.txt'
    res =  os.path.isfile(fname)

    if res:
        pass
    else:
        tempQueryList = queryList.getQueryFilesList()
        print(len(tempQueryList))
        f = open(fname, 'w')
        for sub in range(0, 51253):
            strWrite = ""
            for v in tempQueryList:
                c_w = v.count(sub)
                if c_w > 0:
                    strWrite += str(c_w) + " "
            # print(strWrite)
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

# res = getQueryTF()
# print("len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 10:
#         print(v)
#         k  = k + 1
