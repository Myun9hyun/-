import streamlit as st
import numpy as np

tab0, tab1, tab2 = st.tabs(["🏠 Homepage", "📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

with tab0:
    tab0.subheader("💸2030의 소비트렌드 분석💸")
    st.write("위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다.")
    st.image("https://cdn.pixabay.com/photo/2018/01/07/20/56/graph-3068300_960_720.jpg", width=500)
    '''
    * 보여줄수 있는 자료 입니다.
    > * 차트1
    > * 차트2
    > * 그래프1
    > * 그래프2

    '''
with tab1:
    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)
    st.write
    '''
    ---
    ### 차트임
    ---
    '''
with tab2:
    tab2.subheader("A tab with the data")
    tab2.write(data)
    st.write'''
    ---
    ### 데이터임
    ---
    '''

