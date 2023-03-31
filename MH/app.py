# import streamlit as st
# import pandas as pd
# import os

# names = [] # 길드원 닉네임 입력 리스트
# weekly_missions = [] # 주간미션 점수 입력 리스트
# suros_cozem = [] # 수로 점수에 따른 코젬 갯수 입력 리스트
# suros = []  # 수로 점수 리스트
# flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
# flags = []  # 플래그 점수 리스트
# cozem_sums = [] # 전체 코젬 합산 갯수에 따른 코젬 갯수 입력 리스트
# novels = [] # 노블 사용 여부 리스트




# # 데이터를 저장할 파일 경로 지정
# FILE_PATH = 'data.csv'

# # 파일에서 데이터 불러오기
# def load_data():
#     try:
#         data = pd.read_csv(FILE_PATH)
#     except FileNotFoundError:
#         data = pd.DataFrame(columns=['Name', 'Weekly_Mission',	'Suro',	'Suro_Cozem',	'Flag',	'Flag_Cozem',	'Cozem_Total',	'Novel'])
#     return data

# # 데이터를 파일에 저장하기
# def save_data(data):
#     data.to_csv(FILE_PATH, index=False)

# # 데이터 초기화 함수
# def clear_data():
#     global data
#     data = pd.DataFrame(columns=['Name', 'Weekly_Mission',	'Suro',	'Suro_Cozem',	'Flag',	'Flag_Cozem',	'Cozem_Total',	'Novel'])
#     # 파일 삭제
#     os.remove(FILE_PATH)
# def flag_cozem(flag):
#     # input(f"f입력 : {n} ")
#     if flag >= 0 and flag < 500:
#         i = 0
#         return i
#     if flag >= 500 and flag <= 750:
#         i = 1
#         return i
#     elif flag > 750 and flag < 1000:
#         i = 2
#         return i
#     elif flag == 1000:
#         i = 3
#         return i

# def Suro_cozem(suro):
#     if suro < 500 and suro >= 0:
#         return 0
#     elif suro >= 500:
#         i = (suro // 500)
#         return i

# def cozem_sum():
#     answer = 0
#     answer = suro(s) + flag_cozem(f)
#     return answer

# def novel():
#     if (weekly_mission >= 3) and (s > 0) and (f > 0):
#         return 'O'
#     elif weekly_mission == 5 and s >= 1500:
#         return 'O'
#     elif weekly_mission == 5 and f >= 650:
#         return 'O'
#     else:
#         return 'X'


# # 불러온 데이터를 전역 변수로 저장
# data = load_data()

# # 사용자로부터 이름과 점수를 입력받아 데이터프레임에 추가하는 함수
# # def add_data(name, weekly_mission, suro, flag):
# #     global data
# #     data = data.append({
# #         'Name': name, 
# #         'Weekly_Mission' : weekly_mission, 
# #         'Suro': suro, 
# #         'Flag' : flag,
# #          }, ignore_index=True)
# def add_data(name, weekly_mission, suro, flag):
#     global data
#     suro_cozem = Suro_cozem(suro)  # Suro_cozem 함수로부터 반환된 값을 변수에 저장합니다.
#     flag_cozem = flag_cozem(flag)  # flag_cozem 함수로부터 반환된 값을 변수에 저장합니다.
#     cozem_total = suro_cozem + flag_cozem  # 코젬 총합을 계산합니다.
#     novel_use = novel()  # novel 함수로부터 반환된 값을 변수에 저장합니다.
    
#     # 데이터프레임에 추가합니다.
#     data = data.append({
#         'Name': name, 
#         'Weekly_Mission': weekly_mission, 
#         'Suro': suro, 
#         'Suro_Cozem': suro_cozem,  # Suro_cozem 함수로부터 반환된 값을 추가합니다.
#         'Flag': flag, 
#         'Flag_Cozem': flag_cozem,  # flag_cozem 함수로부터 반환된 값을 추가합니다.
#         'Cozem_Total': cozem_total,  # 코젬 총합을 추가합니다.
#         'Novel': novel_use  # novel 함수로부터 반환된 값을 추가합니다.
#     }, ignore_index=True)

# # Streamlit 앱 생성
# def main():
#     st.title('Add and Display Data')
    
#     # 사용자로부터 이름과 점수를 입력받는 UI 구성
#     name = st.text_input('Enter Name')
#     weekly_mission = st.number_input('Enter weekly mission', min_value=0, max_value=5)
#     suro = st.number_input('Enter suro', min_value=0, max_value=100000)
#     flag = st.number_input('Enter flag', min_value=0, max_value=1000)
    

#     if flag:
#         flags_cozem.append(flag_cozem(flag))
#         flags.append(flag)
    
#     # 이름과 점수가 입력되면 데이터프레임에 추가
#     if st.button('Add Data'):
#         add_data(name, weekly_mission ,suro, flag)
#         save_data(data)  # 데이터를 파일에 저장
#         st.success('Data Added Successfully')
    
#     # 저장된 데이터프레임 출력
#     # if st.button('Display Data'):
#     #     st.write(data)
#     if st.button('Display Data'):
#         st.write(data[['Name', 'Weekly_Mission', 'Suro', 'Suro_Cozem', 'Flag', 'Flag_Cozem', 'Cozem_Total', 'Novel']])


#     # 데이터 초기화 버튼
#     if st.button('Clear Data'):
#         clear_data()
#         st.warning('Data Cleared Successfully')

# if __name__ == '__main__':
#     main()



import streamlit as st
import pandas as pd
import os

names = [] # 길드원 닉네임 입력 리스트
weekly_missions = [] # 주간미션 점수 입력 리스트
suros = []  # 수로 점수 리스트
flags = []  # 플래그 점수 리스트
cozem_sums = [] # 전체 코젬 합산 갯수에 따른 코젬 갯수 입력 리스트
novels = [] # 노블 사용 여부 리스트
flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트

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

def cozem_sum(s, f):
    answer = 0
    answer = Suro_cozem(s) + flag_cozem(f)
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
    novel_value = novel()  # Novel 값 계산

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
    
    def novel():
        if (weekly_mission >= 3) and (suro > 0) and (flag > 0):
            return 'O'
        elif weekly_mission == 5 and suro >= 1500:
            return 'O'
        elif weekly_mission == 5 and flag >= 650:
            return 'O'
        else:
            return 'X'

    # 이름과 점수가 입력되면 데이터프레임에 추가
    if st.button('Add Data'):
        add_data(name, weekly_mission ,suro, flag)  # 수정된 add_data 함수를 호출
        save_data(data)  # 데이터를 파일에 저장
        st.success('Data Added Successfully')
    
    # 저장된 데이터
    if st.button('Display Data'):
        #     st.write(data)
        if st.button('Display Data'):
            st.write(data[['Name', 'Weekly_Mission', 'Suro', 'Suro_Cozem', 'Flag', 'Flag_Cozem', 'Cozem_Total', 'Novel']])


    if st.button('Clear Data'):
        clear_data()
        st.warning('Data Cleared Successfully')

if __name__ == '__main__':
    main()

