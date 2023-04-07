

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

bg_color = "#f0f0f0"
css = f"""
    <style>
        body {{
            background-color: {bg_color};
        }}
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

# 나머지 코드 작성
