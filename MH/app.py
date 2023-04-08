import streamlit as st

st.markdown("""
    <style>
        /* 새로운 글꼴을 추가합니다. */
        @font-face {
          font-family: 'Nanum Gothic';
          src: url('https://cdn.jsdelivr.net/font-nanum/1.0/NanumGothic.ttf') format('truetype');
          font-weight: normal;
          font-style: normal;
        }

        /* 기본 글꼴을 새로운 글꼴로 대체합니다. */
        body {
          font-family: 'Nanum Gothic', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

st.write("안녕하세요, Streamlit에서 글꼴을 변경하였습니다.")
