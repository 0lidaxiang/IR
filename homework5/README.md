# IR Homework1 Introduction
This is the homework5 of NTUST CSIE IR course in  2017 fall.

## steps1 Vector model
+ 1 : get the query list

+ 2 : get the dictionary and document tf,idf and query tf

+ 3 : document term weight，先取得一個 document 作爲豎着向量。再找到 query term weight， 作爲橫着向量

+ 4 : compute the 兩個向量點乘

+ 5 : compute the 兩個向量長度

+ 6 : 計算 cos

+ 7 : 排序比較對於這個 query ，最接近的結果 cosVal 越大

+ 8 : 找到所有的 query 的 cosVal

## step2 Word Embedding(CBOW)
1. get the all files into a file.
2. initial data, three words are a group of input-data.
3. initial left of the first data, third data.
4. initial middle data list, source from the second data in second step.
5. convert middle data to one-hot style.
6. keras uses Word Embedding method - CBOW to train. And save weight.
7. get Embedding result of weight file.
8. compute cosVal by Embedding result.

## step3 Add and get final result
1. get the all documents 's colVal of all querys from step1.'
2. get the all documents 's colVal of all querys from step2.'
3. Add two groups colVal.
4. Sort result.

## Others:
If we use 2500 times train and split input-data to 10 groups for one train, we will get best result for this homework5 when only train three groups input-data.It is amazing but in fact.
