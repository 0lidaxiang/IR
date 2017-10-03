import os

def getQueryFilesString():
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

    return queryFiles
def getQueryFilesList():
    queryFiles = getQueryFilesString()
    queryFilesList = []
    for value in queryFiles:
        queryFilesList.append(value)
    return queryFilesList

# res =  getQueryFilesList()
# print "len(res): " , len(res)
# print "query[0] type: " , type(res[0])
#
# k =0
# for v in res:
#     if k < 10:
#         print v
#         k  = k + 1
