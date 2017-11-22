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
import h5py
import dictionary
import getFileList
import getDocL

k = 1   # context windows size
wordsNum = 13290
train_data_size = 100000
docsL = getFileList.getIntsFromFile()
dic = dictionary.getDictionary()

def getWeightFromHd5(weight_file_path):
    f = h5py.File(weight_file_path)
    try:
        if len(f.items())==0:
            print("len(f.items())", len(f.items()))
            return
        embeddings = f["embedding_1"]["embedding_1"]["embeddings:0"]
        return np.array(embeddings)
    finally:
        f.close()

def getAllWordsNum():
    all_words_num = 0
    for doc in docsL:
        all_words_num += len(doc)
    return all_words_num

all_words_num = getAllWordsNum()
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
        left_Input[inputIndex] = doc.index(doc[wordI])
        right_Input[inputIndex] = doc.index(doc[wordI+1])
        middle[inputIndex] = doc.index(doc[wordI+2])
        inputIndex += 1
left_Input = left_Input[0:train_data_size]
right_Input = right_Input[0:train_data_size]
middle = middle[0:train_data_size]

#preprocess the label_y
clf = LabelBinarizer()
clf.fit(dic)
LabelBinarizer(neg_label=0, pos_label=1)
label_y = clf.transform(middle)

# final input and label
left_Input = np.array(left_Input)
right_Input = np.array(right_Input)
label_y = np.array(label_y)
print("left_Input : ", left_Input.shape, type(left_Input))
print("right_Input : ", right_Input.shape, type(right_Input))
print("label_y : ", label_y.shape, type(label_y) , "\n")

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

history = model.fit([left_Input,right_Input], label_y.reshape(train_data_size,1,13290), initial_epoch=0, epochs=10, verbose=0, shuffle=False)

# it can be others, like mean_absolute_error , cosine_proximity, mean_absolute_percentage_error
loss_func_name = 'mean_squared_error'

lossFileW_path = "./loss_log-" + str(datetime.now()).split()[0] + ".log"
lossFileW = open(lossFileW_path, 'w')
lossFileW.write(loss_func_name + " loss value : \n")

print("\n" + loss_func_name + " loss value" + " : ")
for value in history.history[loss_func_name]:
    lossFileW.write(str(datetime.now()) + "  " + str(value) + "\n")
    print(value)
lossFileW.close()
pyplot.plot(history.history[loss_func_name])
pyplot.show()

res_weights_file = "my_model_" + str(datetime.now()).split(".")[0] +".h5"
model.save_weights(res_weights_file)

res_embeddings_path = res_weights_file
# res_embeddings_path = "my_model_2017-11-21 18:32:50" + ".h5"

res_embeddings = getWeightFromHd5(res_embeddings_path)
# print(type(res_embeddings[0]), res_embeddings[0])
