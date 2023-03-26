# Streamlit 패키지 불러오기
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

# CSV 파일 업로드
uploaded_file = st.file_uploader("Choose a file")

# CSV 파일이 업로드된 경우
if uploaded_file is not None:
    # 업로드된 파일을 데이터프레임으로 변환
    df = pd.read_csv(uploaded_file)
    # CONF 열에서 유니크한 값 추출
    confs = df['CONF'].unique().tolist()
    # 사용자가 선택한 CONF 값
    selected_conf = st.selectbox('Select a conference', confs)
    # 선택된 CONF에 해당하는 행 추출
    selected_rows = df[df['CONF'] == selected_conf]
    # YEAR 열에서 유니크한 값 추출
    years = selected_rows['YEAR'].unique().tolist()
    # 사용자가 선택한 YEAR 값
    selected_year = st.selectbox('Select a year', years)
    # 선택된 YEAR에 해당하는 행 추출
    selected_row = selected_rows[selected_rows['YEAR'] == selected_year]
    # 사용자가 선택한 columns
    columns = st.multiselect('Select columns', list(selected_row.columns))
    # 선택된 columns에 해당하는 값 추출
    values = selected_row.loc[:, columns].values.flatten().tolist()
    # radar chart 그리기
    angles = [n / float(len(columns)) * 2 * pi for n in range(len(columns))]
    angles += angles[:1]
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], columns)
    ax.set_rlabel_position(0)
    plt.yticks([], [])
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    st.pyplot()
