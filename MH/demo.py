import streamlit as st
import pandas as pd

# 파일 업로드
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # csv 파일을 데이터프레임으로 변환
    df = pd.read_csv(uploaded_file)

    # CONF 열 입력 받기
    conf = st.text_input("Enter a value for CONF column")
    if conf != "":
        # 입력받은 CONF 값과 일치하는 모든 행 추출
        df = df[df["CONF"] == conf]

    # YEAR 열 입력 받기
    year = st.text_input("Enter a value for YEAR column")
    if year != "":
        # 입력받은 YEAR 값과 일치하는 모든 행 추출
        df = df[df["YEAR"] == year]

    # 선택받은 columns 출력
    columns = st.multiselect("Select columns", df.columns)
    if len(columns) > 0:
        df = df[columns]

    # radar chart로 출력
    if len(df) > 0:
        st.write(df)
        st.write("Radar Chart")
        st.line_chart(df)
    else:
        st.write("No data available")
