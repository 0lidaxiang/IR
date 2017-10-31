import os

def getFilesName():
    fname = "../source/doc_list.txt"
    res = []
    with open(fname) as f:
        for line in f:
            res.append(str(line))
    return res

def getAllFilesContent():
    fname = "../initialResult/allFilesContent.txt"
    res1 =  os.path.isfile(fname)
    if res1:
        pass
    else:
        createFilesContentFile()
    res = []
    with open(fname) as f:
        for line in f:
            res.append(str(line))
    return res

def createFilesContentFile():
    fileNameList= getFilesName()
    # allFilesContent= []

    strTemp = ""
    for fileName in fileNameList:
        print(fileName)
        f = open( "../source/Document" + "/" + fileName.rstrip("\n"));
        iter_f = iter(f);

        lineNumber = 1

        for line in iter_f:
            if lineNumber > 3:
                strTemp = strTemp + line.rstrip("-1\r\n")
            else:
              lineNumber = lineNumber + 1
        strTemp += "\r\n"
        # allFilesContent.append(strTemp)
        f.close()

    f = open( "../initialResult/allFilesContent.txt", "w");
    f.write(strTemp)
    f.close()
    # return allFilesContent
    return "success"

# res = getAllFilesContent()
# print("type " , type(res))
# print("type " , type(res[0]))
# print("len(res): " , len(res))
# print("len(res): " , len(res[0]))
# print("len(res): " , len(res[0][0]))

# k =0
# for v in res:
#     if k < 10:
#         print( v)
#         k  = k + 1


# def getFilesListFromFile():
#     createFilesListFile()
#     new = []
#     with open('./initialResult/filesList.txt') as f:
#         lines = f.read().splitlines()
#     for line in lines:
#         strTemp = ''.join(line.split("\r\n"))
#         new.append(strTemp)
#
#     return new
