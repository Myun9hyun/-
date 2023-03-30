import streamlit as st

# 초기 상태 설정
total_apples = 10

# 반복문으로 구매 반복
for i in range(3):
    # 사용자 입력 처리
    with st.form(key=f'buy_form_{i}'):
        quantity = st.number_input('사과 갯수', min_value=1, max_value=total_apples)
        st.form_submit_button('구매')

    # 상태 업데이트
    if 'quantity' in st.session_state:
        total_apples -= st.session_state['quantity']

    # 상태 출력
    st.write(f'{i+1}번째 구매 후 남은 사과 갯수: {total_apples}')

    # 남은 사과가 없으면 반복 종료
    if total_apples == 0:
        st.warning('더 이상 사과가 남아있지 않습니다.')
        break
