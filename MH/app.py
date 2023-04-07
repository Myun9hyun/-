import streamlit as st

# 배경에 사용할 이미지 파일 경로를 지정합니다.
bg_image = 'MH/image/newjeans.jpeg'

# set_page_config 함수를 사용하여 배경을 변경합니다.
st.set_page_config(layout="wide", page_title='My Streamlit App', page_icon=':smiley:', 
                   initial_sidebar_state='expanded', background=bg_image)

# 이후에는 일반적인 Streamlit 코드를 작성합니다.
