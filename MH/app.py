import streamlit as st
import pandas as pd
import os

# 위클리 코젬 내야하는 갯수
def manager(cozem_sums):
    st.write(f"반디 : {divide_cozem(cozem_sums)[1]} 개")
    st.write(f"샴푸 : {divide_cozem(cozem_sums)[2]} 개")
    st.write(f"둥둥 : {divide_cozem(cozem_sums)[3]} 개")
    st.write(f"돌체 : {divide_cozem(cozem_sums)[0]} 개")

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

    if st.button('delete'):
        delete_name = st.text_input('삭제할 이름을 입력하세요')
        data.drop(delete_name, inplace=True)
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

    if st.button('devide'):
        weekly_total = data['Cozem_Total'].sum()
        quotient = weekly_total // 5
        remainder = weekly_total % 5
        a = b = c = d = e = quotient
        for i in range(remainder):
            if i == 0:
                a += 1
            elif i == 1:
                b += 1
            elif i == 2:
                c += 1
            elif i == 3:
                d += 1
            else:
                e += 1

        st.write(f"위클리는 총 {weekly_total}개 입니다.")
        st.write(f"반디 : {a} 개")
        st.write(f"샴푸 : {b} 개")
        st.write(f"둥둥 : {c} 개")
        st.write(f"돌체 : {d} 개")
        st.write(f"영래 : {e} 개")
if __name__ == '__main__':
    main()

