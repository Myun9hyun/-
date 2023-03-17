import pandas as pd
import numpy as np
import streamlit as st


tab1, tab2, tab3 = st.tabs(["🏠Homepage", "Cozem", "Novel"])

with tab1:
   st.header("HomePage")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("코젬")
    st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAyMDEwMTBfMTkg%2FMDAxNjAyMzE0NjY1MTM3.OCHXBz1V9YHlZgKQWBqvgPyy8dKbnDj_sAMmoL67wWIg.2XpBx6CyawstsbtIl2UTMRJeE0VHPULU1OfbbzPVJkYg.JPEG%2FexternalFile.jpg&type=a340", width=400)
    with st.sidebar:
        st.[element_name]
with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)