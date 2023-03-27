import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 업로드 및 데이터프레임 생성
uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # CONF 열 입력받아 해당하는 행 출력
    conf_col = st.selectbox("CONF 열 선택", options=list(df.columns))
    selected_conf = st.text_input("CONF 값을 입력하세요.")
    conf_df = df.loc[df[conf_col] == selected_conf]

    # YEAR 열 입력받아 해당하는 행 출력
    year_col = st.selectbox("YEAR 열 선택", options=list(df.columns))
    selected_year = st.text_input("YEAR 값을 입력하세요.")
    year_df = conf_df.loc[conf_df[year_col] == selected_year]

    # 출력할 열 선택받아 출력
    selected_cols = st.multiselect("출력할 열 선택", options=list(df.columns))
    selected_df = year_df[selected_cols]

    # TEAM 열을 기준으로 radar chart 출력
    if 'TEAM' in selected_cols:
        fig = px.line_polar(selected_df, r='VALUE', theta='TEAM', line_close=True)
        st.plotly_chart(fig)
    else:
        st.write(selected_df)
