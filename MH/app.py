import streamlit as st
import numpy as np

tab0, tab1, tab2 = st.tabs(["🏠 Homepage", "📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)
elected_tab = st.sidebar.radio('Select Tab', tabs)

# 버튼 생성
if selected_tab == 'Homepage':
    if st.button('Go to Chart Tab'):
        selected_tab = 'Chart'
    elif st.button('Go to Data Tab'):
        selected_tab = 'Data'
elif selected_tab == 'Chart':
    if st.button('Go to Homepage Tab'):
        selected_tab = 'Homepage'
    elif st.button('Go to Data Tab'):
        selected_tab = 'Data' 
elif selected_tab == 'Data':
    if st.button('Go to Homepage Tab'):
        selected_tab = 'Homepage'
    elif st.button('Go to Chart Tab'):
        selected_tab = 'Chart'        

if selected_tab == 'Home':
    st.write('Welcome to Home Tab!')
elif selected_tab == 'About':
    st.write('Welcome to About Tab!')
else:
    st.write('Welcome to Contact Tab!')
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

