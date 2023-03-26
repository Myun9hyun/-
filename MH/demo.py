import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# CSV 파일을 데이터프레임으로 읽어오기
df = pd.read_csv("https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv")

# 지역(CONF)에 해당하는 행 추출
conf = st.sidebar.selectbox('Select a conference', df['CONF'].unique())
conf_df = df[df['CONF'] == conf]

# 시즌(YEAR)에 해당하는 행 추출
year = st.sidebar.selectbox('Select a season', conf_df['YEAR'].unique())
year_df = conf_df[conf_df['YEAR'] == year]

# 선택한 스탯들을 multiselect로 선택
selected_stats = st.multiselect('Select stats', year_df.columns)

if selected_stats:
    fig = go.Figure()
    for stat in selected_stats:
        fig.add_trace(go.Scatterpolar(
            r=year_df[stat],
            theta=year_df.index,
            fill='toself',
            name=stat
        ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[year_df[selected_stats].min().min(), year_df[selected_stats].max().max()]
            )
        ),
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)
