import streamlit as st

bg_color = "#F0F2F6"
bg_image = "MH/image/newjeans.jpg"

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded",
    # background 인자
    background=bg_color,
    # background_image 인자
    background_image=bg_image,
)