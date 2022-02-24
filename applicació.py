# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 21:28:58 2022

@author: Núria
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import imutils
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import imageio
import matplotlib.pyplot as plt 
from keras_preprocessing.image import img_to_array



image=None

def escollir_imatge():
  #especificar el tipus d'arxiu que podem seleccionar
  path_image = filedialog.askopenfilename(filetypes=[
   ('image', '.jpg'),
  ('image','.jpeg'),
  ('image','.png')])  


  if len(path_image) >0: 
    img= Image.open(path_image)
    image= img.resize((250,210))
    render= ImageTk.PhotoImage(image)
    img1= tk.Label(root, image=render)
    img1.image=render
    img1.place(x=74, y=80)

    #preparar imatge per aplicar IA:
    img=plt.imread(path_image)
    img=cv2.resize(img,(64,64), interpolation=cv2.INTER_CUBIC)
    img= img_to_array(img)
    img=np.expand_dims(img, axis=0)
    img_prep= tf.keras.utils.normalize(img, axis=1)
      

    model= keras.models.load_model('MFVII.h5')
    model.load_weights('MFWVII.h5')
    
    
    predictions = model.predict(img_prep)
    print(predictions)
    predicted_value= np.argmax(predictions)
    new_predicted_value=predicted_value.tolist()
    print(new_predicted_value)
    
    lletres={0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",
             6:"G",7:"H",8:"I",9:"J", 10:"K",
             11:"L",12:"M",13:"N",14:"O",15:"P",
             16:"Q",17:"R",18:"S",19:"T",20:"U",
             21:"V",22:"W",23:"X",24:"Y",25:"Z"}
    
    lletra= lletres[new_predicted_value]
       
    labelI=tk.Label(root, text="Pertany a la lletra:")
    labelI.place(x=120,y=305,width=160,height=35)
    labelI.config(font=("Verdana",12))
    
    solucio=tk.Label(root, text=lletra)
    solucio.place(x=135,y=345,width=130,height=35)
    solucio.config(font=("Verdana",12))


root=tk.Tk()
root.title('Abecedari ASL')
root.geometry('400x500')

lblInputImage = tk.Label(root)
lblInputImage.place(x=155,y=220,width=50,height=35)


#crear el botó per escollir la imatge d'entrada
btnImatge= tk.Button(root, text='Escollir imatge' , command=escollir_imatge)
btnImatge.config(fg="white", bg="blue",font=("Arial",10))
btnImatge.place(x=116,y=400,width=170,height=45)


lbl=tk.Label(root, text="Abecedari ASL")
lbl.place(x=115,y=32,width=170,height=50)
lbl.config(font=("Book Antiqua",18))


root.mainloop()
