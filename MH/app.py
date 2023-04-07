import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# 이미지 열기
image = Image.open("MH/image/newjeans.jpg")

# 이미지 사이즈 가져오기
width, height = image.size

# 이미지 위에 텍스트 추가
draw = ImageDraw.Draw(image)
text = "hi"
font = ImageFont.truetype("MH/font/arial.ttf", 36)  # 한글 폰트 사용
textwidth, textheight = draw.textsize(text, font)
x = (width - textwidth) / 2
y = (height - textheight) / 2
draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

# 결과 이미지 출력
st.image(image)
