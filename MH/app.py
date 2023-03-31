import streamlit as st
import pandas as pd

# 빈 데이터프레임 생성
data = pd.DataFrame(columns=['Name', 'Score'])

# 사용자로부터 이름과 점수를 입력받아 데이터프레임에 추가하는 함수
def add_data(name, score):
    global data
    data = data.append({'Name': name, 'Score': score}, ignore_index=True)

# Streamlit 앱 생성
def main():
    st.title('Add and Display Data')
    
    # 사용자로부터 이름과 점수를 입력받는 UI 구성
    name = st.text_input('Enter Name')
    score = st.number_input('Enter Score', min_value=0, max_value=100)
    
    # 이름과 점수가 입력되면 데이터프레임에 추가
    if st.button('Add Data'):
        add_data(name, score)
        st.success('Data Added Successfully')
    
    # 저장된 데이터프레임 출력
    if st.button('Display Data'):
        st.write(data)

if __name__ == '__main__':
    main()
