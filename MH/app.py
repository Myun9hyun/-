# streamlit 라이브러리 호출
import streamlit as st

#st.write 내부만 고치기!
st.write(
    """
   import streamlit as st
import matplotlib.pyplot as plt

# pie chart 데이터 생성
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# pie chart 생성
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart Example')

# streamlit에 pie chart 업로드
st.pyplot(fig)

    """
)
# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2020/01/26/21/57/computer-4796017_960_720.jpg"
)