import os

def createQueryList():
    fname = 'queryList.txt'
    res =  os.path.isfile(fname)
    if res:
        print fname + " has exists."
        pass
    else:
        dTFs = []
        path = "./data/Query"
        files= os.listdir(path)
        queryFiles = []
        for file in files:
            f = open(path+"/"+file);
            iter_f = iter(f);
            strtemp = ""
            lineNumber = 1

            for line in iter_f:
                strtemp = strtemp + line.rstrip("-1\r\n")
                lineNumber = lineNumber + 1
            query = {}
            query["fileName"] = file
            query["content"] = strtemp
            queryFiles.append(query)
        f.close()

        fname = "./queryList.txt"
        f = open(fname, 'w')
        for query in queryFiles:
            strWrite = query["fileName"] + " " + query["content"]
            f.write(strWrite + "\n")
        f.close()

def getQueryFilesName():
    createQueryList()
    res = []
    with open('./queryList.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        query = {}
        strTemp = ''.join(line.split("\r\n"))
        query["fileName"] = map(str, strTemp.split())[0]
        # query["fileName"] = map(str, strTemp.split())[0]
        res.append(query)
    return res

def getQueryFilesList():
    createQueryList()
    res = []
    with open('./queryList.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        query = {}
        strTemp = ''.join(line.split("\r\n")).split(' ', 1 )
        query["fileName"] = strTemp[0]
        query["content"] = strTemp[1]
        res.append(query)
    return res

# res =  getQueryFilesList()
# print "len(res): " , len(res)
# print "query[0] type: " , type(res[0])
# print "query[0] type: " , res[0]

# k =0
# for v in res:
#     if k < 10:
#         print v
#         k  = k + 1
