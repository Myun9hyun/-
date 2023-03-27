import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# CSV 파일 업로드
uploaded_file = st.file_uploader("Choose a file")

# CSV 파일이 업로드되었는지 확인
if uploaded_file is not None:
    # 업로드한 CSV 파일을 데이터프레임으로 변환
    df = pd.read_csv(uploaded_file)

    # 선택한 컬럼명 받기
    conf_col = st.selectbox("Select CONF column", options=df.columns)
    year_col = st.selectbox("Select YEAR column", options=df.columns)

    # 선택한 컬럼명으로 데이터프레임 필터링
    conf_val = st.selectbox("Select value in CONF column", options=df[conf_col].unique())
    year_val = st.selectbox("Select value in YEAR column", options=df[year_col].unique())
    filtered_df = df[(df[conf_col] == conf_val) & (df[year_col] == year_val)]

    # 선택한 컬럼명으로 데이터프레임 필터링하여 multiselect로 출력할 컬럼 선택
    select_cols = st.multiselect("Select columns to display", options=filtered_df.columns)

    # 선택한 컬럼만 출력
    st.write(filtered_df[select_cols])

    # TEAM의 컬럼명으로 데이터프레임 필터링하여 radar chart 출력
    team_col = "TEAM"
    team_val = st.selectbox("Select value in TEAM column for radar chart", options=filtered_df[team_col].unique())
    team_df = filtered_df[filtered_df[team_col] == team_val]
    stats = st.multiselect('Select statistics for radar chart:', filtered_df.columns.tolist())
    theta = stats + [stats[0]]
    fig = go.Figure(data=go.Scatterpolar(
        r=team_df[stats].values.tolist()[0] + [team_df[stats].values.tolist()[0][0]],
        theta=theta,
        fill='toself'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 40])))
    st.plotly_chart(fig)
else:
    st.warning("Please upload a file.")
