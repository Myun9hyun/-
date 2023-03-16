import streamlit as st
import pandas as pd



option = st.selectbox(
    'How would you like to be contacted?',
    ('연령대별 구매 카테고리', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
{
    labels = ['호박파이', '사과파이', '정어리파이', '엄마손파이']
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)
plt.title("파이 차트")
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90) 
# autopct-> auto percent 자동 확률 계산.
# shadow -> 음영
# startangle -> 0의 값이 시작되는 부분(제목 나오는 곳곳)
plt.axis('equal')
plt.show()
}



