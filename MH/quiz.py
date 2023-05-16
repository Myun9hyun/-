import streamlit as st
import pandas as pd
import random

class RandomBox:
    def __init__(self):
        self.items = []
        self.probabilities = []

    def add_item(self, item, probability):
        self.items.append(item)
        self.probabilities.append(probability)

    def remove_item(self, item):
        index = self.items.index(item)
        self.items.pop(index)
        self.probabilities.pop(index)

    def draw(self, username):
        item = random.choices(self.items, weights=self.probabilities)[0]
        self.remove_item(item)
        return {'Username': username, 'Item': item}

box = RandomBox()

# 사용자 이름을 입력하고, 물품과 확률을 추가하는 입력 창
st.header('랜덤박스 만들기')
usernames = ['Alice', 'Bob', 'Charlie', 'Dave']
username_input = st.selectbox('사용자 이름', usernames)
item_input = st.text_input('추가할 물품')
probability_input = st.number_input('물품의 확률', value=0.0, step=0.1, format='%.1f')
add_button = st.button('추가')
if add_button:
    box.add_item(item_input, probability_input)
    st.success(f'{item_input}이(가) 추가되었습니다.')

# 랜덤박스에서 물품을 뽑는 버튼
st.header('랜덤박스 뽑기')
draw_button = st.button('뽑기')
if draw_button:
    if not box.items:
        st.warning('랜덤박스가 비어있습니다.')
    else:
        item = box.draw(username_input)
        st.success(f'{username_input}이(가) {item["Item"]}을(를) 뽑았습니다.')

        # 데이터프레임에 저장
        df = pd.DataFrame([item])
        if 'data' not in st.session_state:
            st.session_state['data'] = df
        else:
            st.session_state['data'] = pd.concat([st.session_state['data'], df])

# 저장된 데이터프레임 출력
if 'data' in st.session_state:
    st.header('뽑은 랜덤박스 목록')
    st.write(st.session_state['data'])
