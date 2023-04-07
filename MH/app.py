import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# 이미지 업로드
image = Image.open("MH/image/newjeans.jpg")

# 이미지에 텍스트 추가
draw = ImageDraw.Draw(image)
text = "Hello, world!"
font = ImageFont.truetype("MH/font/arial-cufonfonts/ARIAL.TTF", 36)
text_width, text_height = draw.textsize(text, font=font)
x = (image.width - text_width) // 2
y = image.height - text_height - 20

# 테두리 색상과 굵기 설정
stroke_width = 2
stroke_fill = (0, 0, 0)

# 테두리가 있는 텍스트 그리기
draw.text((x - stroke_width, y), text, font=font, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x + stroke_width, y), text, font=font, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, y - stroke_width), text, font=font, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, y + stroke_width), text, font=font, fill=stroke_fill, stroke_width=stroke_width)
draw.text((x, y), text, font=font, fill=(255, 255, 255))

# streamlit에 이미지 표시
st.image(image, caption='Image overlaid with text')
