import streamlit as st
from PIL import Image

st.sidebar.title("Upload Cover Photo")
cover_photo = st.sidebar.file_uploader("Choose a PNG or JPG image", type=["png", "jpg"])

if cover_photo is not None:
    img = Image.open(cover_photo)
    st.image(img, caption='Uploaded Cover Photo', use_column_width=True)
