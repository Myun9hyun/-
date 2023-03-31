import streamlit as st
import pandas as pd
import os

names = [] # 길드원 닉네임 입력 리스트
weekly_missions = [] # 주간미션 점수 입력 리스트
suros_cozem = [] # 수로 점수에 따른 코젬 갯수 입력 리스트
suros = []  # 수로 점수 리스트
flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
flags = []  # 플래그 점수 리스트
cozem_sums = [] # 전체 코젬 합산 갯수에 따른 코젬 갯수 입력 리스트
novels = [] # 노블 사용 여부 리스트

def flag_cozem(f):
    # input(f"f입력 : {n} ")
    if f >= 0 and f < 500:
        i = 0
        return i
    if f >= 500 and f <= 750:
        i = 1
        return i
    elif f > 750 and f < 1000:
        i = 2
        return i
    elif f == 1000:
        i = 3
        return i

def suro(s):
    if s < 500 and s >= 0:
        return 0
    elif s >= 500:
        i = (s // 500)
        return i

def cozem_sum():
    answer = 0
    answer = suro(s) + flag_cozem(f)
    return answer

def novel():
    if (weekly_mission >= 3) and (s > 0) and (f > 0):
        return 'O'
    elif weekly_mission == 5 and s >= 1500:
        return 'O'
    elif weekly_mission == 5 and f >= 650:
        return 'O'
    else:
        return 'X'


# 데이터를 저장할 파일 경로 지정
FILE_PATH = 'data.csv'

# 파일에서 데이터 불러오기
def load_data():
    try:
        data = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Name', 'Weekly_Mission',	'Suro',	'Suro_Cozem',	'Flag',	'Flag_Cozem',	'Cozem_Total',	'Novel'])
    return data

# 데이터를 파일에 저장하기
def save_data(data):
    data.to_csv(FILE_PATH, index=False)

# 데이터 초기화 함수
def clear_data():
    global data
    data = pd.DataFrame(columns=['Name', 'Weekly_Mission',	'Suro',	'Suro_Cozem',	'Flag',	'Flag_Cozem',	'Cozem_Total',	'Novel'])
    # 파일 삭제
    os.remove(FILE_PATH)

# 불러온 데이터를 전역 변수로 저장
data = load_data()

# 사용자로부터 이름과 점수를 입력받아 데이터프레임에 추가하는 함수
def add_data(name, weekly_mission, suro, flag):
    global data
    data = data.append({'Name': name, 'Weekly_Mission' : weekly_mission, 'Score': suro, 'Flag' : flag }, ignore_index=True)

# Streamlit 앱 생성
def main():
    st.title('Add and Display Data')
    
    # 사용자로부터 이름과 점수를 입력받는 UI 구성
    name = st.text_input('Enter Name')
    weekly_mission = st.number_input('Enter weekly mission', min_value=0, max_value=5)
    suro = st.number_input('Enter suro', min_value=0, max_value=100000)
    flag = st.number_input('Enter flag', min_value=0, max_value=1000)
    
    
    # 이름과 점수가 입력되면 데이터프레임에 추가
    if st.button('Add Data'):
        add_data(name, weekly_mission ,suro, flag)
        save_data(data)  # 데이터를 파일에 저장
        st.success('Data Added Successfully')
    
    # 저장된 데이터프레임 출력
    if st.button('Display Data'):
        st.write(data)

    # 데이터 초기화 버튼
    if st.button('Clear Data'):
        clear_data()
        st.warning('Data Cleared Successfully')

if __name__ == '__main__':
    main()
