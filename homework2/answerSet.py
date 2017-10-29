# coding: utf-8

def getAnswerSetList(path):
    bufsize = 65536
    answerSetList = []
    answerSetStr = ""
    with open(path) as infile:
        while True:
            lines = infile.readlines(bufsize)
            if not lines:
                break
            for line in lines:
                lineList = line.split(",")
                lineDic = {}
                lineDic["queryName"] = lineList[0]
                lineDic["answerSet"] = lineList[1].split(" ")[:-1]
                answerSetList.append(lineDic)
    del(answerSetList[0])
    return answerSetList

# result = getAnswerSetList()
# print(len(result))
# # print(result[1])
# print(type(result[1]))
# print(result[0]["answerSet"][0])
# print(result[0]["answerSet"][1])
# print(result[0]["answerSet"][2])
