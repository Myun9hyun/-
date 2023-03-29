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
values = ['코젬', '경뿌', '반파별4개', '수에큐3개', '소경축비', '명큡', '앱상', '강환불', '미코젬', '주흔묶음', '반빨', '재획비', '경축비', '고보킬', '고대비', '명훈', '장큐', '거코젬']
probabilities = [0.074, 0.074, 0.074, 0.074, 0.074, 0.03, 0.03, 0.03, 0.03, 0.03, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]


# 출력을 원하는 개수를 입력받습니다.
n = st.number_input("출력을 원하는 개수를 입력하세요:", min_value=1, max_value=10, step=1, value=1)

# 값을 랜덤하게 선택하여 출력합니다.
selected_values = random_values(values, probabilities,n)
st.write(selected_values)
