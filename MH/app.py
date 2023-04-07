import streamlit as st

bg_image_path = "MH/image/newjeans.jpg"

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded",
    # 배경 이미지 설정
    page_bg_img=bg_image_path
)

# Streamlit 앱의 나머지 코드
