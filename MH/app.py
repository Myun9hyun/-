import streamlit as st
import pandas as pd
import os

names = [] # 길드원 닉네임 입력 리스트
weekly_missions = [] # 주간미션 점수 입력 리스트
suros = []  # 수로 점수 리스트
flags = []  # 플래그 점수 리스트
cozem_sums = [] # 전체 코젬 합산 갯수에 따른 코젬 갯수 입력 리스트
novel_p = [] # 노블 사용 여부 리스트
flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트


weekly_total = data['Cozem_Total'].sum()
# 이번주 위클리 분배
def divide_cozem(weekly_total):
    cozem = weekly_total // 4  # 몫
    cozem_else = weekly_total % 4  # 나머지
    if weekly_total < 3:  # 입력값이 3 미만인 경우
        return [weekly_total] + [0] * (3 - weekly_total)
    if cozem_else == 0:  # 4로 나누어 떨어지는 경우
        return [cozem] * 4
    elif cozem_else == 1:  # 4로 나누었을 때 나머지가 1인 경우
        return [cozem_else, cozem_else, cozem_else, cozem_else + 1]
    elif cozem_else == 2:  # 4으로 나누었을 때 나머지가 2인 경우
        return [cozem_else, cozem_else, cozem_else + 1, cozem_else + 1]
    elif cozem_else == 3:  # 4으로 나누었을 때 나머지가 3인 경우
        return [cozem_else, cozem_else + 1, cozem_else + 1, cozem_else + 1]
# 입력값이 4미만일 경우 오류 -> 해결 필요
n = weekly_total
manager(n)

# 위클리 코젬 내야하는 갯수
def manager(n):
    print(f"반디 : {divide_cozem(n)[1]} 개")
    print(f"샴푸 : {divide_cozem(n)[2]} 개")
    print(f"둥둥 : {divide_cozem(n)[3]} 개")
    print(f"돌체 : {divide_cozem(n)[0]} 개")

def Flag_cozem(flag):
    if flag >= 0 and flag < 500:
        i = 0
        return i
    if flag >= 500 and flag <= 750:
        i = 1
        return i
    elif flag > 750 and flag < 1000:
        i = 2
        return i
    elif flag == 1000:
        i = 3
        return i

def Suro_cozem(suro):
    if suro < 500:
        i = 0
    else:
        i = (suro // 500)
    return i

def cozem_sum(suro, flag):
    answer = 0
    answer = Suro_cozem(suro) + Flag_cozem(flag)
    return answer

def novel_p(weekly_mission, suro, flag):
    if (weekly_mission >= 3) and (suro > 0) and (flag > 0):
        novel = 'O'
    elif weekly_mission == 5 and suro >= 1500:
        novel = 'O'
    elif weekly_mission == 5 and flag >= 650:
        novel = 'O'
    else:
        novel = 'X'
    return novel



# 데이터를 저장할 파일 경로 지정
FILE_PATH = 'data.csv'

# 파일에서 데이터 불러오기
def load_data():
    try:
        data = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Name', 'Weekly_Mission', 'Suro', 'Flag', 'Cozem_Total', 'Novel'])
    return data

# 데이터를 파일에 저장하기
def save_data(data):
    data.to_csv(FILE_PATH, index=False)

# 데이터 초기화 함수
def clear_data():
    global data
    data = pd.DataFrame(columns=['Name', 'Weekly_Mission', 'Suro', 'Flag', 'Cozem_Total', 'Novel'])
    # 파일 삭제
    os.remove(FILE_PATH)

# 불러온 데이터를 전역 변수로 저장
data = load_data()

# 사용자로부터 이름과 점수를 입력받아 데이터프레
def add_data(name, weekly_mission, suro, flag):
    global data
    suro_cozem = Suro_cozem(suro)  # Suro_cozem 함수를 이용해 suro_cozem 값을 계산
    flag_cozem = Flag_cozem(flag)  # flag_cozem 함수를 이용해 flag_cozem 값을 계산
    cozem_total = suro_cozem + flag_cozem  # 코젬 총합 계산
    novel_value = novel_p(weekly_mission, suro, flag)  # Novel 값 계산

    data = data.append({
        'Name': name, 
        'Weekly_Mission': weekly_mission, 
        'Suro': suro, 
        'Suro_Cozem': suro_cozem,  # suro_cozem 값을 추가
        'Flag': flag, 
        'Flag_Cozem': flag_cozem,  # flag_cozem 값을 추가
        'Cozem_Total': cozem_total,  # 코젬 총합 값을 추가
        'Novel': novel_value  # Novel 값을 추가
    }, ignore_index=True)


def main():
    st.title('Add and Display Data')
    
    # 사용자로부터 이름과 점수를 입력받는 UI 구성
    name = st.text_input('Enter Name')
    weekly_mission = st.number_input('Enter weekly mission', min_value=0, max_value=5)
    suro = st.number_input('Enter suro', min_value=0, max_value=100000)
    flag = st.number_input('Enter flag', min_value=0, max_value=1000)
    

    # 이름과 점수가 입력되면 데이터프레임에 추가
    if st.button('Add Data'):
        add_data(name, weekly_mission ,suro, flag)  # 수정된 add_data 함수를 호출
        save_data(data)  # 데이터를 파일에 저장
        st.success('Data Added Successfully')
    
    # 저장된 데이터
    if st.button('Display Data'):
        st.write(data[['Name', 'Weekly_Mission', 'Suro', 'Suro_Cozem', 'Flag', 'Flag_Cozem', 'Cozem_Total', 'Novel']])
        # if st.button('Display Data'):
        #     st.write(data[['Name', 'Weekly_Mission', 'Suro', 'Suro_Cozem', 'Flag', 'Flag_Cozem', 'Cozem_Total', 'Novel']])


    if st.button('Clear Data'):
        clear_data()
        st.warning('Data Cleared Successfully')

    if st.button('Cozem sum'):
        weekly_total = data['Cozem_Total'].sum()
        st.write(f"{weekly_total}개")

    if st.button('Warning'):
        # 경고자 명단
        st.write(data[data['Novel'] == 'X'])
    
    if st.button('monthly'):
        # 먼슬리 참여 가능자 명단
        st.write(data[data['Novel'] == 'O'])

if __name__ == '__main__':
    main()

