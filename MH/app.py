import streamlit as st
import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# 웹페이지에 데이터프레임 출력
st.dataframe(df, width=500, height=500)
