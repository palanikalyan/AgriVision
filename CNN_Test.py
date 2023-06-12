import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json
from tkinter import *
import tensorflow as tf
from PIL import Image
win=tk.Tk()
win.configure(bg='#FFBF00')
def b1_click():
    global path2
    try:
        json_file = open('model1.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("model1.h5")
        print("Loaded model from disk")
        label=["Apple___Apple_scab","Apple___Black_rot","Apple___Cedar_apple_rust","Apple___Healthy",
               "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot","Corn_(maize)___Common_rust_",
               "Corn_(maize)___Healthy","Corn_(maize)___Northern_Leaf_Blight","Grape___Black_rot",
               "Grape___Esca_(Black_Measles)","Grape___Healthy","Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
               "Potato___Early_blight","Potato___Healthy","Potato___Late_blight","Tomato___Bacterial_spot",
               "Tomato___Early_blight","Tomato___Healthy","Tomato___Late_blight","Tomato___Leaf_Mold",
               "Tomato___Septoria_leaf_spot","Tomato___Spider_mites Two-spotted_spider_mite","Tomato___Target_Spot",
               "Tomato___Tomato_Yellow_Leaf_Curl_Virus","Tomato___Tomato_mosaic_virus"]
        
        path2=filedialog.askopenfilename()
        print(path2)

        test_image = tf.keras.utils.load_img(path2, target_size = (128, 128))        
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image)
        print(result)
        label2=label[result.argmax()]
        print(label2)
        lbl.configure(text=label2)
        img = Image.open(path2)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 20)
        label = label[result.argmax()]
        for i in range(0,2000): 
            draw.rectangle((10, 10, 100, 100), outline="white",width=5)
            draw.rectangle((10, 10, 100, 100), outline="red",width=5)
            draw.rectangle((10, 10, 100, 100), outline="green",width=5)
            draw.text((10, 120), label, font=font, fill="white")
        img = img.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel.configure(image=img,border=8,bg='green')
        panel.image = img

    except IOError:
        pass

    draw.rectangle((10, 10, 100, 100), outline="red",width=5)

label1 = Label(win,width=16, text="Green vision", fg ='lightgreen',bg='black',font=("Qdbettercomicsansboldalternates",16))
label1.pack()

panel = Label(win)
panel.pack()

b1=tk.Button(win, text= 'Pick leaf',width=16, height=1,fg ='White', font=("Qdbettercomicsansboldalternates", 25), command=b1_click,border=10,bg='green')
b1.pack()

lbl = tk.Button(win, text="Result",width=25, fg ='white',bg='#007FFF', font=("Qdbettercomicsansboldalternates",16),border=10)
lbl.pack()

win.geometry("800x500")
win.title("Green Vision AI")
win.bind("<Return>", b1_click)
win.mainloop() 
