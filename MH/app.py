import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded"
)

bg_image_url = "MH/image/newjeans.jpg"
bg_css = f"""
    <style>
        body {{
            background-image: url('{bg_image_url}');
            background-size: cover;
        }}
    </style>
"""

st.markdown(bg_css, unsafe_allow_html=True)

# Streamlit 앱의 나머지 코드
