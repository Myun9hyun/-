import pandas as pd
import numpy as np
import streamlit as st


tab1, tab2, tab3 = st.tabs(["🏠Homepage", "Cozem", "Novel"])

with tab1:
   st.header("HomePage")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("코젬")
   st.image("https://upload3.inven.co.kr/upload/2021/02/07/bbs/i13327956984.jpg?MW=800", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)