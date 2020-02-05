import os
import plaidml.keras as pk
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.optimizers import RMSprop
from tensorflow.keras.callbacks import TensorBoard
import datetime

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000,784)
x_test = x_test.reshape(10000,784)
x_train = x_train.astype('float32')/255
y_train = y_train.astype('float32')/255



model = Sequential()
model.add(Dense(512,activation= 'relu',input_shape=(28*28,)))
model.add(Dropout(0.2))
model.add(Dense(10,activation='softmax'))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
#%%
log_dir="logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)
#%%
model.fit(x=x_train,
          y=y_train,
          epochs=5,
          validation_data=(x_test, y_test),
          #callbacks=[tensorboard_callback])

#%%
#tensorboard --logdir logs/fit
'''


import  datetime
## 定义学习参数
batch_size = 128
num_classes = 10
epochs = 20
## import data
(x_train,y_train),(x_test,y_test) = mnist.load_data()
## seperate data
x_train = x_train.reshape(60000,784)
x_test = x_test.reshape(10000,784)
x_train = x_train.astype('float32')/255
y_train = y_train.astype('float32')/255

##打印数据
print(x_train.shape[0],'train samples')
print(x_test.shape[0],'test samples')

#%%
## add layer
model = Sequential()
model.add(Dense(512,activation= 'relu',input_shape=(28*28,)))
## dropout
model.add(Dropout(0.2))
model.add(Dense(10,activation='softmax'))
model.summary()
model.compile(loss = 'sparse_categorical_crossentropy',
              optimizer= RMSprop(),
              metrics= ['accuracy'])
#%%
log_dir='logs/fit/'
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)
#%%
history = model.fit(x_train,y_train,
                    batch_size = batch_size,
                    epochs = epochs,
                    validation_data=(x_test, y_test),
                    callbacks=[tensorboard_callback]
                    )

score = model.evaluate(x_test,y_test,verbose=0)
print('Total Loss:',score[0])
print('Test accuracy:',score[1])
'''
