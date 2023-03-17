import pandas as pd
import numpy as np
import streamlit as st


# options = ["tab1", "tab2", "Option 3"]

# # 사이드바 위젯을 생성합니다.

# selected_option = st.sidebar.selectbox("Select an option", options)

# 사이드바에 메뉴 만들기
menu = ["Home", "About", "Contact"]
choice = st.sidebar.selectbox("Select an option", menu)

# 선택된 메뉴에 따라 다른 탭 출력
if choice == "Home":
    st.write("Welcome to the Home page")
elif choice == "About":
    st.write("Welcome to the About page")
else:
    st.write("Welcome to the Contact page")


tab1, tab2, tab3 = st.tabs(["🏠Homepage", "Cozem", "Novel"])
with tab1:
   st.header("HomePage")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("코젬")
    st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAyMDEwMTBfMTkg%2FMDAxNjAyMzE0NjY1MTM3.OCHXBz1V9YHlZgKQWBqvgPyy8dKbnDj_sAMmoL67wWIg.2XpBx6CyawstsbtIl2UTMRJeE0VHPULU1OfbbzPVJkYg.JPEG%2FexternalFile.jpg&type=a340", width=400)
    
with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)