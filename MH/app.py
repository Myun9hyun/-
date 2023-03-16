# streamlit 라이브러리 호출
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from google.colab import files

import streamlit as st
import pandas as pd

# 엑셀 파일 불러오기
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)

)
# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2020/01/26/21/57/computer-4796017_960_720.jpg"
)