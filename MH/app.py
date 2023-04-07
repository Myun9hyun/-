import streamlit as st
from PIL import Image, ImageDraw, ImageFont


# 이미지 업로드
image = Image.open("MH/image/newjeans.jpg")
width, height = image.size
# 이미지에 텍스트 추가
draw = ImageDraw.Draw(image)
text = "Hello, world!"
font = ImageFont.truetype("MH/font/arial-cufonfonts/ARIAL.TTF", 36)
text_width, text_height = draw.textsize(text, font=font)
x = (width - text_width) // 2
y = (height - text_height) // 2

# 이미지에 텍스트 추가
draw = ImageDraw.Draw(image)
draw.text((x, y), text, font=font, fill=(255, 255, 255))

# streamlit에 이미지 표시
st.image(image, caption='Image overlaid with text')
