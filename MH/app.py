import streamlit as st

st.markdown("""
    <style>
        /* 새로운 글꼴을 추가합니다. */
        @font-face {
          font-family: 'Montserrat';
          src: url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
          font-weight: normal;
          font-style: normal;
        }

        /* 기본 글꼴을 새로운 글꼴로 대체합니다. */
        body {
          font-family: 'Montserrat', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

st.write("안녕하세요, Streamlit에서 Montserrat 글꼴을 적용하였습니다.")
