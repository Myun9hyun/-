import streamlit as st

# 초기 상태 설정
total_apples = 10

# 사용자 입력 처리
with st.form(key='buy_form'):
    quantity = st.number_input('사과 갯수', min_value=1, max_value=total_apples)
    submitted = st.form_submit_button('구매')

# 상태 업데이트
if submitted:
    if quantity > total_apples:
        st.error('재고보다 많은 수량을 구매할 수 없습니다.')
    else:
        total_apples -= quantity
        st.session_state.quantity = quantity

# 상태 출력
st.write(f'사과 갯수: {total_apples}')
