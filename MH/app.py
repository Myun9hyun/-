import streamlit as st

st.markdown("""
    <style>
        /* 새로운 글꼴을 추가합니다. */
        @font-face {
          font-family: 'Roboto';
          src: url('https://fonts.googleapis.com/css?family=Roboto&display=swap');
          font-weight: normal;
          font-style: normal;
        }

        /* 기본 글꼴을 새로운 글꼴로 대체합니다. */
        body {
          font-family: 'Roboto', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

st.write("안녕하세요, Streamlit에서 Roboto 글꼴을 적용하였습니다.")
