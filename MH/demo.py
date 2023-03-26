import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

    # 추출된 데이터 내에서 선택된 스탯만 추출
    stats_df = filtered_df[['TEAM'] + selected_stats]

    # Radar chart 그리기
    categories = selected_stats
    N = len(categories)
    values = stats_df.iloc[:, 1:].values.tolist()
    values += values[:1]
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories)

    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75], ["0.25", "0.50", "0.75"], color="grey", size=7)
    plt.ylim(0, 1)

    for i in range(len(stats_df)):
        values = stats_df.iloc[i, 1:].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=stats_df.iloc[i, 0])
        ax.fill(angles, values, 'b', alpha=0.1)

    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    st.pyplot(fig)
