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
st.title("🐻아기자기 랜덤박스🎁")
st.write()
'''
##### 랜덤박스🎁 내 물품은 다음과 같습니다

| 구분 |  구성품 | 확률 | 
|:---: | :---: | :---: | 
| 꽝💣 | 코젬, 경뿌, 반파별4개, 수에큐3개 | 7.4% |
| 대박🎊 | 명큡, 앱솔상자, 강환불, 미코젬, 주흔 한묶음 | 6% |
| 일반💰 | 반빨별, 재획비, 경축비, 고보킬, 고대비, 명훈, 장큐, 거코젬 | 3% | 


'''
# 값과 그에 해당하는 확률을 리스트로 지정합니다.
values = ['코젬', '경뿌', '반파별4개', '수에큐3개', '소경축비', '명큡', '앱상', '강환불', '미코젬', '주흔_한묶음', '반빨별', '재획비', '경축비', '고보킬', '고대비', '명훈', '장큐', '거코젬']
probabilities = [0.074, 0.074, 0.074, 0.074, 0.074, 0.03, 0.03, 0.03, 0.03, 0.03, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06, 0.06]


# 출력을 원하는 개수를 입력받습니다.
n = st.number_input("상자를 오픈하실 개수를 입력하세요:", min_value=1, max_value=10, step=1, value=1)

# 값을 랜덤하게 선택하여 출력합니다.
selected_values = random_values(values, probabilities,n)
# st.success('This is a success message!', icon="✅")
open_button = st.button("상자 열기")
if open_button:
    # st.balloons()
    selected_values = random_values(values, probabilities, n)
    if selected_values in ['코젬' or '경뿌' or '반파별4개' or'수에큐3개' or '소경축비']:
        # if values in ['코젬', '경뿌', '반파별4개', '수에큐3개', '소경축비']:
        for i in range(min(n, len(selected_values))):
            st.success(f"아쉽습니다.. {selected_values[i]}(이)가 나왔습니다..")

    elif values in ['명큡' or '앱상' or'강환불' or'미코젬' or '주흔_한묶음']:
        st.balloons()
        for i in range(min(n, len(selected_values))):
            st.balloons(
            st.success(f"상자에서 {selected_values[i]}(이)가 나왔습니다!")
            )
    elif values in ['반빨별' or '재획비' or'경축비' or '고보킬' or '고대비' or '명훈' or '장큐' or '거코젬']:
        for i in range(min(n, len(selected_values))):
            st.success(f"축하드립니다! {selected_values[i]}(이)가 당첨되었습니다!")
# open_button = st.button("상자 열기")
# if open_button:
#     selected_values = random_values(values, probabilities, n)
#     if values in ('코젬', '경뿌', '반파별4개', '수에큐3개', '소경축비'):
#         for i in range(min(n, len(selected_values))):
#             st.write(f"축하드립니다! {selected_values[i]}(이)가 당첨되었습니다!")
#     elif values in ('명큡', '앱상', '강환불', '미코젬', '주흔_한묶음'):
#         st.balloons()
#         for i in range(min(n, len(selected_values))):
#             st.write(f"축하드립니다! {selected_values[i]}(이)가 당첨되었습니다!")
#     elif values in ('반빨별', '재획비', '경축비', '고보킬', '고대비', '명훈', '장큐', '거코젬'):
#         for i in range(min(n, len(selected_values))):
#             st.write(f"축하드립니다! {selected_values[i]}(이)가 당첨되었습니다!")
