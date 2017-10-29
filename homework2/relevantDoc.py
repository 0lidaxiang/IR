# coding: utf-8

def getRelevantDocList(path):
    bufsize = 65536
    relevantDocList = []
    relevantDocStr = ""
    with open(path) as infile:
        while True:
            lines = infile.readlines(bufsize)
            if not lines:
                break
            for line in lines:
                lineList = line.split(",")
                lineDic = {}
                lineDic["queryName"] = lineList[0]
                lineDic["relevantDoc"] = lineList[1].split(" ")[:-1]
                relevantDocList.append(lineDic)
    del(relevantDocList[0])
    return relevantDocList

# result = getRelevantDocList()
# print(result[1])
