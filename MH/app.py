import streamlit as st
import pandas as pd
import numpy as np
# 엑셀 파일 불러오기
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write(df)
