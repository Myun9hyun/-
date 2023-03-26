import pandas as pd
import streamlit as st

# 데이터프레임을 불러옵니다.
df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv")

# 멀티셀렉트로 선택한 열을 입력받습니다.
selected_cols = st.multiselect('Select columns', df.columns)

# 선택한 열에 해당하는 인덱스를 추출합니다.
df_selected = df.loc[:, selected_cols]
selected_indices = df_selected.index.tolist()
st.write(selected_indices)
