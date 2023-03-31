import streamlit as st
import pandas as pd
import os
import base64

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

def add_data(name, weekly_mission, suro, flag):
    global data
    # 중복 검사
    if name in data['Name'].values:
        st.warning(f'{name} (은)는 이미 있는 이름이야!')
        return
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


# 다운로드 버튼 클릭 시 CSV 파일 다운로드
def download_csv(data, file_name):
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}.csv">Download CSV</a>'
    return href


def main():
    st.title('cozem')
    
    # 사용자로부터 이름과 점수를 입력받는 UI 구성
    name = st.text_input('이름을 입력하세요')
    weekly_mission = st.number_input('주간미션 점수를 입력하세요', min_value=0, max_value=5)
    suro = st.number_input('수로 점수를 입력하세요', min_value=0, max_value=100000)
    flag = st.number_input('플래그 점수를 입력하세요', min_value=0, max_value=1000)
    

    # 이름과 점수가 입력되면 데이터프레임에 추가
    if st.button('데이터 추가'):
        add_data(name, weekly_mission ,suro, flag)  # 수정된 add_data 함수를 호출
        save_data(data)  # 데이터를 파일에 저장
        st.success('데이터가 추가되었습니다.')

    # if st.button('데이터 삭제'):
    #     name_to_delete = st.text_input('삭제할 이름을 입력하세요')
    #     if name_to_delete in data['Name'].values:
    #         data = data[data['Name'] != name_to_delete]

    # 저장된 데이터
    if st.button('차트 열기'):
        if not data.empty:
            st.write(data[['Name', 'Weekly_Mission', 'Suro', 'Suro_Cozem', 'Flag', 'Flag_Cozem', 'Cozem_Total', 'Novel']])
        else:
            st.write('입력되어있는 데이터가 없습니다.')
    # 데이터 전부 삭제
    if st.button('차트 초기화'):
        clear_data()
        st.warning('Data Cleared Successfully')

    if st.button('위클리 코젬 합계 계산'):
        weekly_total = data['Cozem_Total'].sum()
        st.write(f"이번주 위클리 이벤트 코젬의 합은{weekly_total}개 입니다.")

    if st.button('노블 제한목록 보기'):
        # 경고자 명단
        warning = data[data['Novel'] == 'X']
        warning_list = warning['Name'].tolist()
        st.write('이번주 노블 사용제한 목록 입니다.')
        st.write(f"노블 제한자 :  {warning_list}.")
        st.write(data[data['Novel'] == 'X'])
    
    if st.button('노블 사용가능 목록 보기'):
        # 먼슬리 참여 가능자 명단
        monthly = data[data['Novel'] == 'O']
        monthly_list = monthly['Name'].tolist()
        st.write('이번주 노블 사용가능 목록입니다.(먼슬리 참여 가능자)')
        st.write(f"사용가능자 :  {monthly_list}.")
        st.write(data[data['Novel'] == 'O'])
    # 다운로드 버튼 클릭
    if st.button("다운로드"):
        file_name = st.text_input("저장할 파일명을 입력하세요:", "example.csv")

        # 데이터프레임을 CSV 파일로 저장
        data.to_csv(file_name, index=False)
        st.success(f"{file_name} 파일이 저장되었습니다.")



    if st.button('위클리 코젬 분배 계산'):
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

        st.write(f"이번주 위클리 이벤트 코젬은 총 {weekly_total}개 입니다.")
        st.write(f"반디 : {a} 개")
        st.write(f"샴푸 : {b} 개")
        st.write(f"둥둥 : {c} 개")
        st.write(f"돌체 : {d} 개")
        st.write(f"영래 : {e} 개")
if __name__ == '__main__':
    main()

