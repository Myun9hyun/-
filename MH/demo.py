import streamlit as st
import pandas as pd
import altair as alt

# 데이터프레임 로드
url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv"
df = pd.read_csv(url).iloc[:, 1:]

# 지역 선택 위젯
unique_CONF = df['CONF'].unique()
user_CONF = st.selectbox("원하시는 지역을 골라주세요:", unique_CONF)

# 선택한 지역에 해당하는 모든 TEAM 출력
if user_CONF in unique_CONF:
    teams = df[df['CONF'] == user_CONF]['TEAM'].unique()
    selected_teams = st.multiselect("팀 선택", teams)

    # 선택한 팀이 있는 경우
    if selected_teams:
        # 선택한 스탯 다중 선택 위젯
        selected_stats = st.multiselect('스탯 선택', options=df.columns.tolist())

        # 선택한 스탯이 있는 경우 레이더 차트 그리기
        if selected_stats:
            # 선택한 팀과 스탯에 해당하는 데이터프레임 만들기
            selected_df = df[df['TEAM'].isin(selected_teams)][selected_stats + ['TEAM']]

            # 팀 이름을 기준으로 그룹화하여 레이더 차트 그리기
            chart = (
                alt.Chart(selected_df)
                .transform_fold(
                    selected_stats,
                    as_=['stat', 'value']
                )
                .mark_area(opacity=0.3)
                .encode(
                    alt.X('stat:N', axis=alt.Axis(title='')),
                    alt.Y('value:Q', axis=alt.Axis(title='')),
                    alt.Color('TEAM:N'),
                    alt.Column('YEAR:O'),
                    tooltip=['TEAM', 'YEAR', 'value']
                )
                .properties(width=200, height=200)
                .facet(
                    column=alt.Column('YEAR:O', sort='descending')
                )
            )
            st.altair_chart(chart)
