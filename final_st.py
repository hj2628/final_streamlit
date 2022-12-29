import streamlit as st 
import pandas as pd
from PIL import Image
import pytesseract
import cv2
import matplotlib.pyplot as plt


pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'


st.set_page_config(
    page_title = "알잘딱8센_돋보귀app",
    page_icon= "🔎",
    layout= "wide"
)
st.title("🔎돋보귀👂🏻")
img = Image.open('/Users/munhojun/Desktop/멋사_ai_7/파이널프로젝트_썸네일.jpeg')
st.image(img)

st.write("사진을 첨부해주세요")
image_file = st.file_uploader("이미지 업로드", type=["jpg", "png", "jpeg"])

if image_file is not None:
    our_image = Image.open(image_file)
    image = st.image(our_image)
    
    if st.button("결과보기"):
        text = pytesseract.image_to_string(our_image, lang='kor+eng')
        st.write(text)


    
    
   
    
    
    
