import streamlit as st
from PIL import Image

image = Image.open('MH/image/newjeans.jpg')
st.image(image, caption='뉴진스.')
