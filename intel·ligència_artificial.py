# -*- coding: utf-8 -*-
"""Intel·ligència artificial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AfYiA0QBfSkGFcBp8ZgaeVdmxfSdM_3b
"""

from keras.optimizers import Adam
from keras.regularizers import l2

from google.colab import files
uploaded=files.upload()

files.download('archive (9).zip')

from google.colab import drive
drive.mount('/content/drive')

!unzip "/content/archive (9).zip" -d "/content/drive/MyDrive/"

import os 
#s'utilitza per utilitzar directoris
import cv2 
#s'utilitza pel reconeixament d'imatges en Python
from PIL import Image 
#proporciona funcions d'edició d'imatges, per carregar imatges de fitxers i crear imatges noves
import numpy as np 
#ens serveix per treballar amb vectors o matrius
train_images=[]
labels=[]
a=0
train_path= os.listdir("/content/drive/MyDrive/American Sign Language recogntion (ASL)/training_set")
for cdir in train_path:
  img=os.listdir("/content/drive/MyDrive/American Sign Language recogntion (ASL)/training_set/"+cdir)
  for imatge in img: 
    url="/content/drive/MyDrive/American Sign Language recogntion (ASL)/training_set/"+cdir+"/" +imatge
    ig= cv2.imread(url)
    arr= Image.fromarray(ig, 'RGB')
    labels.append(cdir)
    train_images.append(np.array(arr))

from sklearn.preprocessing import LabelEncoder 
# ens ajuda a codificar els nivells de característiques categòriques en valors numèrics
import pandas as pd 
#és especialitzada en anàlisis d'estructures de dades, permet llegir i escriure fitxers en format CSV, Excel i bases de dades SQL 
lb_encod= LabelEncoder()
labels= pd.DataFrame(labels)
labels= lb_encod.fit_transform(labels[0])

train_images= np.array(train_images)
np.save('imatge',train_images)
np.save('labels', labels)

train_images=np.load('imatge.npy')
labels=np.load('labels.npy')

print(train_images)

import matplotlib.pyplot as plt 
#serveix per crear gráfiques i imatges de dues dimensions
print(train_images[2].shape)
plt.figure()
plt.imshow(np.squeeze(train_images[0]))
plt.show()

import tensorflow as tf
train_images = tf.keras.utils.normalize(train_images, axis=1)
print(train_images)

test_images=[]
test_labels=[]
a=0
test_path= os.listdir("/content/drive/MyDrive/American Sign Language recogntion (ASL)/test_set")
for cdir in train_path:
  img=os.listdir("/content/drive/MyDrive/American Sign Language recogntion (ASL)/test_set/"+cdir)
  for imatge in img: 
    url="/content/drive/MyDrive/American Sign Language recogntion (ASL)/test_set/"+cdir+"/" +imatge
    ig= cv2.imread(url)
    arr= Image.fromarray(ig, 'RGB')
    test_labels.append(cdir)
    test_images.append(np.array(arr))

lb_encod= LabelEncoder()
test_labels= pd.DataFrame(test_labels)
test_labels= lb_encod.fit_transform(test_labels[0])
test_labels

test_images= np.array(test_images)
np.save('test_imatge',test_images)
np.save('test_labels', test_labels)

test_images=np.load('test_imatge.npy', allow_pickle=True)
test_labels=np.load('test_labels.npy', allow_pickle= True)

test_images = tf.keras.utils.normalize(test_images, axis=1)
print(test_images)

(train_images).shape

from keras.layers import Activation, Convolution2D,  Conv2D, AveragePooling2D, BatchNormalization, Flatten, GlobalAveragePooling2D
from keras import layers
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, MaxPool2D

model= tf.keras.Sequential([
  tf.keras.layers.Conv2D(64,(3,3), activation=tf.nn.relu, input_shape=(64,64,3)),
  tf.keras.layers.MaxPooling2D((2,2), strides=2),

  tf.keras.layers.Conv2D(64,(3,3), activation=tf.nn.relu),
  tf.keras.layers.MaxPooling2D((2,2), strides=2),

   tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(64,activation=tf.nn.relu),
  tf.keras.layers.Dense(26,activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history= model.fit(
  train_images, labels,
  batch_size= 32,
  epochs= 15)

model.evaluate(test_images, test_labels)

plt.figure()
plt.imshow(np.squeeze(train_images[30000]))
plt.show()

result= model.predict(np.array([train_images[30000]]))
print(result)

predicted_value= np.argmax(result)
print(predicted_value)
new_predicted_value=predicted_value.tolist()
print(type(new_predicted_value))