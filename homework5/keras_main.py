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
from sklearn.preprocessing import LabelBinarizer
from matplotlib import pyplot

import dictionary
import getFileList
import getDocL

k = 1   # context windows size
wordsNum = 13290

docsL = getFileList.getIntsFromFile()
dic = dictionary.getDictionary()

def getAllWordsNum():
    all_words_num = 0
    for doc in docsL:
        all_words_num += len(doc)
    return all_words_num

all_words_num = getAllWordsNum() # 393021
input_size =  all_words_num - 2*k -1

# initial input
left_Input = np.zeros(shape=(input_size, 1))
right_Input = np.zeros(shape=(input_size, 1))
middle = np.zeros(shape=(input_size, 1))
inputIndex = 0
for doc in docsL:
    len_doc = len(doc)
    range_word = len_doc - len_doc % 3 - 2
    for wordI in range(0, range_word):
        left_Input[inputIndex] = dic.index(doc[wordI])
        right_Input[inputIndex] = dic.index(doc[wordI+1])
        middle[inputIndex] = dic.index(doc[wordI+2])
        inputIndex += 1

train_data_size = 393018 # 393018
# left_Input = left_Input[0:train_data_size]
# right_Input = right_Input[0:train_data_size]

# define the model
Input_Left = Input(shape=(1,))
Input_Right = Input(shape=(1,))
CBOW = Embedding(output_dim=100, input_dim=wordsNum)
CBOW_L = CBOW(Input_Left)
CBOW_R = CBOW(Input_Right)
Average = keras.layers.Average()([CBOW_L, CBOW_R])
Prediction = Dense(wordsNum, activation='softmax')(Average)
model = Model(inputs=[Input_Left, Input_Right], outputs=Prediction)
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['mse', 'mae', 'mape', 'cosine'])
print(model.summary())

# total data size 393018 , 400 * 982 = 392800, 393200
data_size = 10
for inputs in range(0, 39301):
    input_start = inputs * 10
    input_end = input_start + 10
    if inputs == 39300:
        input_end = input_start + 8
        data_size = 8
    print(inputs)
    # print("inputs, input_start , input_end, data_size : ", inputs, input_start, input_end, data_size)

    #preprocess the label_y
    now_middle = middle[input_start: input_end]
    clf = LabelBinarizer()
    clf.fit(dic)
    LabelBinarizer(neg_label=0, pos_label=1)
    label_y = clf.transform(now_middle)
    # print("label_y : ", label_y.shape, type(label_y) )

    # final input and label
    now_left_Input = np.array(left_Input)[input_start: input_end]
    now_right_Input = np.array(right_Input)[input_start: input_end]
    label_y = np.array(label_y)
    # print("now_left_Input : ", now_left_Input.shape, type(now_left_Input))
    # print("now_right_Input : ", now_right_Input.shape, type(now_right_Input))

    history = model.fit([now_left_Input , now_right_Input], label_y.reshape( data_size,1,13290), initial_epoch=0, epochs=20, verbose=0, shuffle=False)

    if inputs % 5000 == 0 or inputs > 39280:
        # it can be others, like mean_absolute_error , cosine_proximity, mean_absolute_percentage_error
        loss_func_name = 'mean_squared_error'
        lossFileW_path = "./10Train/loss/" + str(inputs) + "-" + str(datetime.now()).split(".")[0] + ".log"
        lossFileW = open(lossFileW_path, 'w')
        lossFileW.write(loss_func_name + " loss value : \n")
        # print("" + loss_func_name + " loss value" + " : ")
        for value in history.history[loss_func_name]:
            lossFileW.write(str(datetime.now()) + "  " + str(value) + "\n")
            # print(value)
        # print("\n")
        lossFileW.close()
        # pyplot.plot(history.history[loss_func_name])
        # pyplot.show()

        res_weights_file = "./10Train/weights/" +  str(inputs) + "-"  + str(train_data_size) + "_" + str(datetime.now()).split(".")[0] +".h5"
        model.save_weights(res_weights_file)

    # res_embeddings_path = res_weights_file
    # res_embeddings_path = "my_model_2017-11-21 18:32:50" + ".h5"

    # res_embeddings = getWeightFromHd5(res_embeddings_path)
# print(type(res_embeddings[0]), res_embeddings[0])
