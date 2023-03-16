import streamlit as st
import numpy as np

tab0, tab1, tab2 = st.tabs(["🏠 Homepage", "📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)
with tab0:
    tab0.subheader("2030의 소비트렌드 분석")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    '''
    * ~홈페이지~
    * 안뇽

    '''
with tab1:
    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)
with tab2:
    tab2.subheader("A tab with the data")
    tab2.write(data)