# streamlit 라이브러리 호출
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from google.colab import files

df = pd.read_excel('KDX2021_SSC_ONLINE_DATA.xlsx')
df2 = df.copy()
df2
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