import streamlit as st

# 배경에 사용할 이미지 파일 경로를 지정합니다.
bg_image = 'MH/image/newjeans.jpeg'

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/jpeg;base64,{base64.b64encode(open(bg_image, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 이후에는 일반적인 Streamlit 코드를 작성합니다.
