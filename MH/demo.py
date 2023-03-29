import streamlit as st
import random

def random_values(values, probabilities, n):
    # n번 값을 랜덤하게 선택하여 반환합니다.
    result = []
    for i in range(n):
        selected_value = random.choices(values, probabilities)[0]
        result.append(selected_value)
    return result

# Streamlit 앱을 실행합니다.
st.title("Random Value Generator")

# 값과 그에 해당하는 확률을 리스트로 지정합니다.
values = [1, 2, 3, 4, 5]
probabilities = [0.1, 0.2, 0.3, 0.3, 0.1]

# 출력을 원하는 개수를 입력받습니다.
n = st.number_input("출력을 원하는 개수를 입력하세요:", min_value=1, max_value=10, step=1, value=1)

# 값을 랜덤하게 선택하여 출력합니다.
selected_values = random_values(values, probabilities, n)
st.write(selected_values)
