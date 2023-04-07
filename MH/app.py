import streamlit as st
import base64

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("MH/image/newjeans.jpg", "rb") as f:
    bg_image_data = f.read()

bg_image_base64 = base64.b64encode(bg_image_data).decode()

bg_css = f"""
    <style>
        body {{
            background-image: url('data:image/jpg;base64,{bg_image_base64}');
            background-size: cover;
        }}
    </style>
"""

st.markdown(bg_css, unsafe_allow_html=True)

# Streamlit 앱의 나머지 코드
``
