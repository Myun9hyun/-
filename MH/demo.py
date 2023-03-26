import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
from math import pi

# csv 파일 업로드
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 지역 입력
    location = st.text_input('Enter the location')
    filtered_df = df[df['CONF'] == location]

    # 시즌 입력
    season = st.text_input('Enter the season')
    filtered_df = filtered_df[filtered_df['YEAR'] == season]

    # 스탯 선택
    selected_stats = st.multiselect('Select stats', ['TEAM', 'CONF', 'G', 'W', 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D',
       'TOR', 'TORD', 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O',
       '3P_D', 'ADJ_T', 'WAB', 'POSTSEASON', 'SEED', 'YEAR'])

    # 선택된 스탯 리스트
    # selected_stats = st.multiselect('Select stats to compare', list(df.columns[4:]))

    # 선택된 스탯만 포함하는 데이터프레임
    df_selected = df.loc[df['CONF'] == location].reset_index(drop=True)[['TEAM', 'YEAR'] + selected_stats]

    # 스탯 비교 레이더 차트 그리기
    fig, ax = plt.subplots(figsize=(10, 8))
    categories = selected_stats
    N = len(categories)
    angles = [n / float(N) * 2 * math.pi for n in range(N)]
    angles += angles[:1]
    ax.set_rmax(mapi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(0)
    for i in range(len(df_selected)):
        values = df_selected.loc[i, selected_stats].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=df_selected.loc[i, 'TEAM'])
        ax.fill(angles, values, alpha=0.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    st.pyplot(fig)
