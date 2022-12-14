import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import tensorflow.keras.models


def classify(score, threshold,class_dict):
    if score >= threshold:
        result = 1
    if score < threshold:
        result = 0
    return list(class_dict.keys())[list(class_dict.values()).index(result)]

st.header('Upload Images')
image_uploaded = st.file_uploader('Upload Your Images', type='jpg')
if image_uploaded:
    image = Image.open(image_uploaded)
    image = image.convert('RGB')
    img = np.array(ImageOps.fit(image, (224,224)))
    #img = img.reshape(224,224,3)
    img = img/255

    fig = px.imshow(img)
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)
    st.plotly_chart(fig)


    model = tensorflow.keras.models.load_model('saved_model/cnn_model.h5')
    score = model.predict(img.reshape(1,224,224,3))[0][0]  
    cls_result = classify(score, 0.5, {'Monkeypox': 1, 'Others': 0})

    if cls_result == 'Monkeypox':
        st.write('Monkeypox Detected')
    elif cls_result == 'Others':
        st.write('Monkey Not Detected')
    
    st.write(score)
    
    