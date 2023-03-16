import streamlit as st

option = st.selectbox(
    'How would you like to be contacted?',
    ('연령대별 구매 카테고리', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)