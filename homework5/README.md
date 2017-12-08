# IR Homework1 Introduction
This is the homework5 of NTUST CSIE IR course in  2017 fall.

Run the main function to get the TOP 100 of final result:
```
python3 main_withTFIDF.py
```
The final result file is submission_TFIDF_MAP100.txt.

If you want to re-generate TF_IDF score, you will need about three hours and you should modify the TF_IDF.py, then run :
```
python3 TF_IDF.py
```

If you want to re-generate CBOW score, you will need about many hours and you should modify the keras_10.py, then run :
```
python3 keras_10.py
```
But the keras train maybe not right.The CBOW result may be better only need 20~50 times train. My 2500 times train's good result is just a **coincidence**.

And maybe we should given the word in query but not in document the socre of the three lowest TF_IDF socre, teacher's advice.

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
