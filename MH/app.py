

# import streamlit as st
# import base64

# with open("MH/image/back.jpg", "rb") as f:
#     img_bytes = f.read()

# if not img_bytes:
#     st.write("Error: Failed to read image file.")

# st.write(f"Image Bytes: {img_bytes}")

# b64 = base64.b64encode(img_bytes).decode()

# st.write(f"B64: {b64}")

# st.markdown(
#     f'<style>body {{background-image: url("data:image/jpeg;base64,{b64}")}}</style>',
#     unsafe_allow_html=True,
# )
# 
import streamlit as st

st.set_page_config(page_title="My Page", page_icon=":guardsman:", layout="wide", page_bg_color="#f0f0f0")


# Streamlit 앱의 나머지 코드
