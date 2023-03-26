import pandas as pd
import streamlit as st

# 데이터프레임을 불러옵니다.
df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv")

# 체크박스로 선택한 columns 받기
selected_columns = st.multiselect('Select columns', df.columns)

# 선택한 columns에 해당하는 index 추출하기
selected_index = df[df[selected_columns].notna().all(axis=1)].index

# 선택한 index들을 출력할 데이터프레임 만들기
selected_df = df.loc[selected_index, selected_columns]

# 선택한 index들을 출력
st.write(selected_df)
