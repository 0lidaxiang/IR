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

def getWeightFromHd5(weight_file_path):
    f = h5py.File(weight_file_path)
    try:
        if len(f.items())==0:
            print("len(f.items())", len(f.items()))
            return
        embeddings = f["embedding_1"]["embedding_1"]["embeddings:0"]
        # print(type(embeddings[0]), embeddings[0])
        return np.array(embeddings)
    finally:
        f.close()

k = 1   # context windows size
wordsNum = 13290
dic = dictionary.getDictionary()
input_size =  wordsNum - 2*k -1
INPUT = np.zeros(shape=(input_size, 2))
left_Input = np.zeros(shape=(input_size, 1))
right_Input = np.zeros(shape=(input_size, 1))
middle = np.zeros(shape=(input_size, 1))

# max_size_kn = wordsNum - 2*k
for kn in range(0, input_size):
    left_Input[kn] = kn
    right_Input[kn] = kn+2*k
    middle[kn] = kn+k

#preprocess the label_y
# print("middle : ", len(middle))
clf = LabelBinarizer()
clf.fit(dic)
LabelBinarizer(neg_label=0, pos_label=1)
label_y = clf.transform(middle)
#
#
left_Input = np.array(left_Input[0:100])
right_Input = np.array(right_Input[0:100])
label_y = np.array(label_y[0:100])
print("left_Input : ", left_Input.shape, type(left_Input))
print("right_Input : ", right_Input.shape, type(right_Input))
print("label_y : ", label_y.shape, type(label_y))
print("\n")

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

history = model.fit([left_Input,right_Input], label_y.reshape(100,1,13290), initial_epoch=0, epochs=10, verbose=0, shuffle=False)

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
