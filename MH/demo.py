import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv"

df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv", index_col=0)

conf = st.sidebar.selectbox("Select Conference", df["CONF"].unique())
selected_df = df[df["CONF"] == conf]

# 선택한 YEAR 값에 해당하는 데이터프레임 출력
year = st.sidebar.selectbox("Select Year", selected_df["YEAR"].unique())
selected_df = selected_df[selected_df["YEAR"] == year]

# 선택한 columns에 해당하는 데이터프레임 출력
columns = st.multiselect("Select Columns", selected_df.columns)
selected_df = selected_df[columns]

# 각 팀들의 Radar Chart를 그리기 위해 팀명을 index로 지정
selected_df.set_index(selected_df.index, inplace=True)

# Radar Chart 그리기
fig = px.line_polar(selected_df, r=selected_df.values, theta=selected_df.columns, line_close=True)

# Radar Chart에 팀명 추가
for d in fig.data:
    d.name = d.name.split("_")[0]

st.plotly_chart(fig)
