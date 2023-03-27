import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle

st.write()
'''
### Stat Info
* 차트설명
---
'''
option = st.selectbox(
'원하는 차트를 골라주세요',
('스탯비교 그래프', '승률데이터 그래프', 'Chart'))
st.write(f'고르신 {option} 차트를 출력하겠습니다: ')

if option == '스탯비교 그래프':
    # CSV 파일이 업로드되었는지 확인
    url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/cbb.csv"
    df = pd.read_csv(url)

    # 선택한 컬럼명으로 데이터프레임 필터링
    conf_val = st.selectbox("Select value in CONF column", options=df['CONF'].unique())
    year_val = st.selectbox("Select value in YEAR column", options=df['YEAR'].unique())
    filtered_df = df[(df['CONF'] == conf_val) & (df['YEAR'] == year_val)]

    # TEAM의 컬럼명으로 데이터프레임 필터링하여 radar chart 출력
    team_col = "TEAM"
    team_vals = st.multiselect("Select values in TEAM column for radar chart", options=filtered_df[team_col].unique())
    stats = st.multiselect('Select statistics for radar chart:', filtered_df.columns.tolist())

    # make_subplots로 1x1 subplot 만들기
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'polar'}]])

    # 선택한 각 team별로 trace 추가하기
    for team_val in team_vals:
        team_df = filtered_df[filtered_df[team_col] == team_val]
        theta = stats + [stats[0]]
        fig.add_trace(go.Scatterpolar(
            r=team_df[stats].values.tolist()[0] + [team_df[stats].values.tolist()[0][0]],
            theta=theta,
            fill='toself',
            name=team_val
        ), row=1, col=1)

    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 70])))
    st.plotly_chart(fig)

elif option == '승률데이터 그래프':
    st.write("승률 데이터 계산입니다")
    url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv"
    df = pd.read_csv(url)
    df = df.iloc[:, 1:]
    unique_CONF = df['CONF'].unique()
    
    # 각 고유값에 해당하는 인덱스 추출하여 딕셔너리에 저장
    index_dict = {}
    for CONF in unique_CONF:
        index_dict[CONF] = df[df['CONF'] == CONF].index.tolist()
    
    # 사용자로부터 지역 입력 받기
    user_CONF = st.selectbox("원하시는 지역을 골라주세요:", unique_CONF)
    
    # 선택한 지역에 해당하는 모든 행 출력
    if user_CONF in unique_CONF:
        indices = index_dict[user_CONF]
        sub_df = df.loc[indices]
        st.write(f"### 해당 지역 '{user_CONF}'에 소속된 팀들의 데이터입니다. ")
        st.write(sub_df)
        
        # 사용자로부터 시즌 입력 받기
        user_YEAR = st.selectbox("원하시는 시즌을 골라주세요:", [''] + sub_df['YEAR'].unique().tolist())
        
        # 선택한 시즌에 해당하는 행 출력
        if user_YEAR != "":
            sub_df = sub_df[sub_df['YEAR'] == int(user_YEAR)]
            st.write(f"### 해당 '{user_CONF}' 지역에 소속된 팀 {user_YEAR} 시즌의 데이터입니다. ")
            st.write(sub_df)
            # 승률 계산
            df_winrate = (sub_df['W'] / sub_df['G']) * 100
            # 계산한 승률을 소수점 아래 2자리까지 표현
            df_winrate_round = df_winrate.round(2)
            sub_df_Team = sub_df[['TEAM']]
            result = pd.concat([sub_df_Team, df_winrate_round], axis=1)
            df_result = result.rename(columns={0: 'win_rate'})
            df_result.reset_index(drop=True, inplace=True)
            # st.write(df_result)
            df_long = pd.melt(df_result, id_vars=['TEAM'], value_vars=['win_rate'])
            fig = px.bar(df_long, x='TEAM', y='value', color='TEAM')
            st.write(f"'{user_CONF}' 지역에 소속된 팀들의 {user_YEAR} 시즌의 승률 그래프입니다. ")
            st.plotly_chart(fig)
    else:
        st.warning("다시 골라주세요.")

elif option == 'Chart':
    st.write("승률 데이터 계산입니다")