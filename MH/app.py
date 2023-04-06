# app.py

import streamlit as st

# 커스텀 테마 적용
st.set_theme({'primaryColor': '#3f51b5', 'backgroundColor': '#f2f2f2',
              'secondaryBackgroundColor': '#fff', 'textColor': '#333',
              'font': 'sans-serif'}, "custom_theme")

# 텍스트 출력
st.header("This is a header")
st.write("This is some text.")
