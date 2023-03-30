import streamlit as st

# 초기 상태 설정
total_apples = 10

# 사용자 입력 처리
with st.form(key='buy_form'):
    quantity = st.number_input('사과 갯수', min_value=1, max_value=total_apples)
    if st.form_submit_button('구매'):
        st.session_state['quantity'] = quantity

# 상태 업데이트
if 'quantity' in st.session_state:
    repeat = st.session_state['quantity']
    while repeat > 0 and total_apples > 0:
        total_apples -= 1
        repeat -= 1

# 상태 출력
if total_apples == 0:
    st.warning('품절되었습니다.')
else:
    st.write(f'사과 갯수: {total_apples}')
