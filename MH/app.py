import streamlit as st
from PIL import Image

header_image = Image.open("MH/image/newjeans.jpg")
st.beta_set_page_config(page_title='My Streamlit App', page_icon=header_image, layout='wide')