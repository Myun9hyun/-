import streamlit as st

bg_image = "MH/image/newjeans.jpg"
st.set_page_config(page_title="My Streamlit App", page_icon=":sunglasses:", layout="wide", initial_sidebar_state="expanded", background_image=bg_image)

# 이미지 출력
st.image(bg_image, use_column_width=True)
