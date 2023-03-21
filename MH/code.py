import streamlit as st
from streamlit.state.session_state import SessionState

# SessionState 객체를 생성합니다.
session_state = SessionState.get(name_list=[], score_list=[])

# 입력 폼을 생성합니다.
st.write('이름과 점수를 입력하세요.')
name = st.text_input('이름')
score = st.number_input('점수')

# '추가' 버튼을 누르면 입력받은 값을 리스트에 추가합니다.
if st.button('추가'):
    session_state.name_list.append(name)
    session_state.score_list.append(score)
    st.write('이름: {}, 점수: {}'.format(name, score))

# '종료' 버튼을 누르면 리스트를 출력합니다.
if st.button('종료'):
    st.write('이름 리스트: {}'.format(session_state.name_list))
    st.write('점수 리스트: {}'.format(session_state.score_list))
