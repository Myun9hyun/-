import streamlit as st
import pandas as pd
import os

# 데이터를 저장할 파일 경로 지정
FILE_PATH = 'data.csv'

# 파일에서 데이터 불러오기
def load_data():
    try:
        data = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Name', 'Price','Mount', 'Point'])
    return data

# 데이터를 파일에 저장하기
def save_data(data):
    data.to_csv(FILE_PATH, index=False)

# 데이터 초기화 함수
def clear_data():
    global data
    data = pd.DataFrame(columns=['Name', 'Price','Mount', 'Point'])
    # 파일 삭제
    os.remove(FILE_PATH)

# 불러온 데이터를 전역 변수로 저장
data = load_data()

# 사용자로부터 이름, 점수, 포인트를 입력받아 데이터프레임에 추가하는 함수
def add_data(name, price, point, mount):
    global data
    data = data.append({'Name': name, 'Price': price,'Point': point, 'Mount' : mount }, ignore_index=True)

# 포인트를 차감하는 함수
def deduct_point(name, mount):
    global data
    row = data[data['Name'] == name].iloc[0]  # 이름이 일치하는 row 선택
    if row['Mount'] >= mount:  # 차감 가능한 경우
        data.loc[data['Name'] == name, 'Mount'] -= mount  # 포인트 차감
        save_data(data)  # 데이터를 파일에 저장
        st.success(f'{mount} Point Deducted from {name} Successfully')
    else:  # 차감 불가능한 경우
        st.warning(f'Not Enough Point for {name}')

# Streamlit 앱 생성
def main():
    password = 1234
    st.title('Add, Display and Deduct Point')
    options = ["데이터추가➕", "데이터조회🔎", "포인트 삭제✂", "데이터 초기화💣", "노블 사용⭕or제한❌", "위클리 코젬 계산📋", "데이터 다운로드💾"]
    option = st.selectbox("기능 선택", options)
    
    # 사용자로부터 이름, 점수, 포인트를 입력받는 UI 구성
    
    if option == '데이터추가➕':
        name = st.text_input('Enter Name')
        price = st.number_input('Enter Price', min_value=0, max_value=10000)
        point = st.number_input('Enter Point', min_value=0, max_value=50)
        mount = st.number_input('Enter Mount', min_value=0, max_value=100)
    # 이름, 점수, 포인트가 입력되면 데이터프레임에 추가
        if st.button('데이터추가'):
            # if st.button('추가'):
            add_data(name, price, point, mount)
            save_data(data)  # 데이터를 파일에 저장
            st.success('Data Added Successfully')
    elif option == '데이터조회🔎':
    # 저장된 데이터프레임 출력
        if st.button('데이터조회🔎'):
            st.write(data)

    # 포인트 차감 버튼
    elif option == '포인트 삭제✂':
        st.write(data)
        name = st.text_input('구매하실 품목을 입력하세요')
        mount = st.number_input('구매하실 갯수를 입력하세요', min_value=0)
    
        if st.button('포인트 삭제✂'):
            deduct_point(name, mount)
    elif option == '데이터 초기화💣':
        password_input = st.number_input('비밀번호를 입력해주세요 : '):
        if password_input == password:
            st.write('접근을 허용합니다')
            # 데이터 초기화 버튼
            if st.button('Clear Data'):
                clear_data()
                st.warning('Data Cleared Successfully')

if __name__ == '__main__':
    main()
