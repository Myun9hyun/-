import streamlit as st
import numpy as np

tab0, tab1, tab2 = st.tabs(["🏠 Homepage", "📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab0.subheader("2030의 소비트렌드 분석")
'''
* 홈페이지!!
st.image("https://static.streamlit.io/examples/cat.jpg", width=200)


'''
tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)