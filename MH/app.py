import streamlit as st

# 탭 생성
tabs = ['Home', 'About', 'Contact']
selected_tab = st.sidebar.radio('Select Tab', tabs)

# 버튼 생성
if selected_tab == 'Home':
    if st.button('Go to About Tab'):
        selected_tab = 'About'
elif selected_tab == 'About':
    if st.button('Go to Home Tab'):
        selected_tab = 'Home'

# 탭 선택에 따른 출력 변경
if selected_tab == 'Home':
    st.write('Welcome to Home Tab!')
elif selected_tab == 'About':
    st.write('Welcome to About Tab!')
else:
    st.write('Welcome to Contact Tab!')
