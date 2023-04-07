import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# 이미지 업로드
image = Image.open("MH/image/newjeans.jpg")

# 이미지에 텍스트 추가
draw = ImageDraw.Draw(image)
text = "Hello, world!"
font = ImageFont.truetype("MH/font/arial-cufonfonts/ARIAL.TTF", 36)
draw.text((10, 10), text, font=font, fill=(7, 7, 7))

# streamlit에 이미지 표시
st.image(image, caption='Image overlaid with text')
