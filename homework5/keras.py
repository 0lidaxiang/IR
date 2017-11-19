#!/usr/bin/python3
# coding: utf-8
import sys
sys.path.insert(0, "/usr/local/lib/python3.5/dist-packages")
import keras
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.embeddings import Embedding
from keras.models import Model
from keras.layers import Input, Dense
from datetime import datetime
import numpy as np
import dictionary
wordsNum = 13290
k = 1 # context windows size

dic = dictionary.getDictionary()

INPUT = np.zeros(shape=(wordsNum, 2))
left_Input = np.zeros(shape=(wordsNum, 1))
right_Input = np.zeros(shape=(wordsNum, 1))
answer = np.zeros(shape=(100, wordsNum))
print(type(answer))
print(len(answer))
print(len(answer[0]))
max_size_kn = wordsNum - 2*k
for kn in range(0, wordsNum - k -1):
    left_Input[kn][0] = dic[kn]
    right_Input[kn][0] = dic[kn+k]
    INPUT[kn][0] = dic[kn]
    INPUT[kn][1] = dic[kn+2*k]

# print(left_Input[0])
# print(left_Input[1])
# print(right_Input[0])
# print(right_Input[1])
# print(INPUT[13286])
# print(INPUT[13287])
# define the model
Input_Left = Input(shape=(1,))
# print(type(Input))
Input_Right = Input(shape=(1,))
Answer = Input(shape=(wordsNum,))

CBOW = Embedding(output_dim=100, input_dim=wordsNum)
CBOW_L = CBOW(Input_Left)
CBOW_R = CBOW(Input_Right)
Average = keras.layers.Average()([CBOW_L, CBOW_R])
Prediction = Dense(wordsNum, activation='softmax')(Average)

model = Model(inputs=[Input_Left, Input_Right], outputs=Prediction)
model.compile(optimizer='Adam', loss='categorical_crossentropy')
print(model.summary())
# print(Prediction)

model.fit([left_Input,right_Input],answer, initial_epoch=0, epochs=1, verbose=0, shuffle=False)
model.save_weights("my_model_" + str(datetime.now()).split(".")[0] +".h5")
print('Answer: ', Answer[0])



def getAnswers():
    fname = "wordsWeight.txt"
    res = []
    with open(fname) as f:
        lines = f.read().split("\r\n")
    for line in lines:
        res.append(int(line))
    return res

def getAnswer(word):
    answer = []
    return answer[word]
