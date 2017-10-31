# IR Homework3 Introduction

# How to run
Use this command :
```
python3 main.py
```

## steps:
+ get the dictionary, allFilesContent,
+ get the wordNumber in one document and this document length, and get the c(w,d),P(w|d)

+ give K=5(topics number). create and give value randomly for P(d) matrix,P(w|T) matrix and P(T|d) matrix but the sum is equal to 1 for every matrixs.

+ E step and M step, train 50 times.

+ get the P(T|d) matrix.

+ maximize the total log-likelihood of a given training collection and record every train.And check.

+ give α β and  α+β = 1. compute the P(q|d) and sort
