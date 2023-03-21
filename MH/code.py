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
#     name_list.append(name)
#     score_list.append(score)
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
# import streamlit as st

# # 이름과 점수를 담을 리스트
# name_list = []
# score_list = []

# # 사용자로부터 이름과 점수 값을 입력받음
# while True:
#     name = st.text_input('이름을 입력하세요:', key='name_input')
#     score = st.number_input('점수를 입력하세요:', key='score_input')

#     if st.button('추가'):
#         name_list.append(name)
#         score_list.append(score)
#         st.success('입력되었습니다.')
#     elif st.button('종료'):
#         st.write('입력이 종료되었습니다.')
#         break

# # 입력된 전체 값을 출력
# st.write('이름\t점수')
# st.write('----\t----')
# for i in range(len(name_list)):
#     st.write('{}\t{}'.format(name_list[i], score_list[i]))

# import streamlit as st

# # 이름과 점수를 담을 리스트
# name_list = []
# score_list = []

# # 사용자로부터 이름과 점수 값을 입력받음
# while True:
#     name = st.text_input('이름을 입력하세요:', key=f'name_input_{len(name_list)}')
#     score = st.number_input('점수를 입력하세요:', key=f'score_input_{len(score_list)}')

#     if st.button('추가'):
#         name_list.append(name)
#         score_list.append(score)
#         st.success('입력되었습니다.')
#     elif st.button('종료'):
#         st.write('입력이 종료되었습니다.')
#         break

# # 입력된 전체 값을 출력
# st.write('이름\t점수')
# st.write('----\t----')
# for i in range(len(name_list)):
#     st.write('{}\t{}'.format(name_list[i], score_list[i]))
import streamlit as st

# 물건 리스트와 수량 리스트
item_list = ['apple', 'banana', 'orange']
quantity_list = [5, 3, 2]

# 물건을 선택하고 수량을 입력받는 함수
def buy_item(item_index):
    quantity = st.number_input(f"{item_list[item_index]} 수량을 입력하세요.", value=1, min_value=1)
    if quantity > quantity_list[item_index]:
        st.error("재고가 부족합니다.")
        return False
    else:
        quantity_list[item_index] -= quantity
        return True

# 각 물건마다 수량과 재고 여부를 표시하는 함수
def show_items():
    for i in range(len(item_list)):
        st.write(f"{item_list[i]}: {quantity_list[i]}개")
        if quantity_list[i] == 0:
            st.warning("매진")

# 상점 UI
st.title("점포")
show_items()
item = st.selectbox("물건을 선택하세요.", item_list)

if st.button("구매"):
    item_index = item_list.index(item)
    if buy_item(item_index):
        st.success(f"{item}를 구매했습니다.")
else:
    st.warning("구매 버튼을 눌러주세요.")
