import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터프레임을 업로드하는 함수
@st.cache
def load_data(file):
    df = pd.read_csv(file)
    return df

# 필요한 columns들만 추출하는 함수
def filter_dataframe(df, conf, year):
    # CONF를 기반으로 데이터프레임 필터링
    df = df[df['CONF'] == conf]

    # YEAR를 기반으로 데이터프레임 필터링
    df = df[df['YEAR'] == year]

    # 선택된 columns들만 추출
    columns_to_show = st.multiselect('Select columns to show:', df.columns.tolist())
    df = df[columns_to_show]

    return df

# radar chart를 생성하는 함수
def create_radar_chart(df, stats):
    fig = px.line_polar(df, r=stats, theta='TEAM', line_close=True)
    fig.update_traces(fill='toself')
    st.plotly_chart(fig)

# streamlit 앱 시작
def main():
    st.title("Radar Chart for NCAA Basketball Teams")

    # 데이터프레임 업로드
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        df = load_data(file)

        # CONF와 YEAR를 선택
        conf = st.sidebar.selectbox('Select conference:', df['CONF'].unique())
        year = st.sidebar.selectbox('Select year:', df['YEAR'].unique())

        # 데이터프레임 필터링
        filtered_df = filter_dataframe(df, conf, year)

        # radar chart 생성
        if 'TEAM' in filtered_df.columns:
            stats = st.multiselect('Select statistics for radar chart:', filtered_df.columns.tolist())
            create_radar_chart(filtered_df, stats)

# 앱 실행
if __name__ == '__main__':
    main()
