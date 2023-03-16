import streamlit as st
import pandas as pd
from google.colab import files

df = pd.read_excel('KDX2021_SSC_ONLINE_DATA.xlsx')
df2 = df.copy()
df2
# 데이터프레임 생성


# 웹페이지에 데이터프레임 출력
st.dataframe(df, width=500, height=500)
