# IR
This is the homeworks of NTUST CSIE IR course in  2017.

## steps:
+ 1 : get the query list

+ 2 : get the dictionary and document tf,idf and query tf

+ 3 : document term weight，先取得一個 document 作爲豎着向量。再找到 query term weight， 作爲橫着向量

+ 4 : compute the 兩個向量點乘

+ 5 : compute the 兩個向量長度

+ 6 : 計算 cos

+ 7 : 排序比較對於這個 query ，最接近的結果 cosVal 越大

+ 8 : 找到所有的 query 的 排序結果
