# streamlit 라이브러리 호출
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from google.colab import files

# 엑셀 파일 불러오기
uploaded_file = st.file_uploader("KDX2021_SSC_ONLINE_DATA", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)

#st.write 내부만 고치기!

st.write(
    """
   
# streamlit에 pie chart 업로드
st.pyplot(fig)

    """
)
# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2020/01/26/21/57/computer-4796017_960_720.jpg"
)