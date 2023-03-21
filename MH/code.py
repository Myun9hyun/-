# import streamlit as st

# # 이름과 점수를 저장할 리스트를 생성합니다.
# name_list = []
# score_list = []

# # 입력 폼을 생성합니다.
# st.write('이름과 점수를 입력하세요.')
# name = st.text_input('이름')
# score = st.number_input('점수')

# # '추가' 버튼을 누르면 입력받은 값을 리스트에 추가합니다.
# if st.button('추가'):
#     # name_list.append(name)
#     # score_list.append(score)
#     st.write('이름: {}, 점수: {}'.format(name, score))
    
#     # 추가한 값을 리스트에 출력합니다.
#     # st.write('이름 리스트: {}'.format(name_list))
#     # st.write('점수 리스트: {}'.format(score_list))

# # '종료' 버튼을 누르면 리스트를 출력합니다.
# if st.button('종료'):
#     name_list.append(name)
#     score_list.append(score)
#     st.write('이름 리스트: {}'.format(name_list))
#     st.write('점수 리스트: {}'.format(score_list))
import streamlit as st

# 이름과 점수를 담을 리스트
name_list = []
score_list = []

# 사용자로부터 이름과 점수 값을 입력받음
while True:
    name = st.text_input('이름을 입력하세요:')
    score = st.number_input('점수를 입력하세요:')

    if st.button('추가'):
        name_list.append(name)
        score_list.append(score)
        st.success('입력되었습니다.')
    elif st.button('종료'):
        st.write('입력이 종료되었습니다.')
        break

# 입력된 전체 값을 출력
st.write('이름\t점수')
st.write('----\t----')
for i in range(len(name_list)):
    st.write('{}\t{}'.format(name_list[i], score_list[i]))
