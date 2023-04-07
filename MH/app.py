import streamlit as st
import base64

st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":sunglasses:",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("MH/image/newjeans.jpg", "rb") as f:
    img_bytes = f.read()

st.write(f"Image Bytes: {img_bytes}")

b64 = base64.b64encode(img_bytes).decode()

st.write(f"B64: {b64}")

st.markdown(
    f'<style>body {{background-image: url("data:image/jpeg;base64,{b64}")}}</style>',
    unsafe_allow_html=True,
)

