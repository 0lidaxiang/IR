# coding: utf-8
import relevantDoc
import answerSet

relevantDoc = relevantDoc.getRelevantDocList("./source/solution.txt")
# homework1 my submission
answerSet = answerSet.getAnswerSetList("./source/mySubmission.txt")
# example submission
# answerSet = answerSet.getAnswerSetList("./source/submission.txt")

sumAP = 0
queryIndex = 0
for rDValue in relevantDoc:
    thisQueryPrecision = [] # for 2265 documents
    thisQueryAnswerSet = answerSet[queryIndex]["answerSet"]  # 2265 documents
    thisQueryRelevantDoc = rDValue["relevantDoc"]  # 13 documents

    # 2265 documents
    for tQRDValue in thisQueryAnswerSet:
        docPre = {"docName" : "", "docPre": 0}
        # 13 relevant documents for this query
        for tQAValue in thisQueryRelevantDoc:
            if tQRDValue == tQAValue:
                docPre["docName"] = tQAValue
                docPre["docPre"] = 1
                break
        thisQueryPrecision.append(docPre)

    # comput Average precision
    allPrecisionofDocs = 0
    precisionDoc = 0
    documentIndex = 1
    countHitDocs = 0
     # for 2265 documents
    for value in thisQueryPrecision:
        if value["docPre"] == 1:
            countHitDocs += 1
            precisionDoc = (countHitDocs * 1.0) / documentIndex
            allPrecisionofDocs = allPrecisionofDocs + precisionDoc
        documentIndex += 1

    AP = allPrecisionofDocs / countHitDocs
    sumAP += AP
    queryIndex += 1

# comput mean Average precision
MAP = sumAP / 16
print("MAP: " , MAP)
