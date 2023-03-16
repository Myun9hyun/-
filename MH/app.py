import streamlit as st
import numpy as np

tab0, tab1, tab2 = st.tabs(["🏠 Homepage", "📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)
with tab0:
    tab0.subheader("💸2030의 소비트렌드 분석💸")
    st.write("위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다.")
    st.image("https://cdn.pixabay.com/photo/2018/01/07/20/56/graph-3068300_960_720.jpg", width=500)
    '''
    * ~홈페이지~
    * 안뇽

    '''
with tab1:
    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)
with tab2:
    tab2.subheader("A tab with the data")
    tab2.write(data)

# 버튼 클릭 시 실행할 함수 정의
def open_link(url):
    js = f"window.open('{url}')"  # 새 탭에서 링크 열기
    html = '<img src onerror="{}">'.format(js)  # 이미지 태그에 js 코드 삽입
    return html

# 버튼 생성 및 클릭 시 실행할 함수 매개변수 전달
if st.button('Open Link'):
    link = 'https://www.google.com'  # 연결할 링크
    st.write(open_link(link), unsafe_allow_html=True)  # 위젯에 HTML 삽입
