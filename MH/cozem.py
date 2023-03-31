
import random
import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import joblib
import xgboost as xgb
import seaborn as sns
from streamlit_option_menu import option_menu
names = [] # 길드원 닉네임 입력 리스트
weekly_missions = [] # 주간미션 점수 입력 리스트
suros_cozem = [] # 수로 점수에 따른 코젬 갯수 입력 리스트
suros = []  # 수로 점수 리스트
flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
flags = []  # 플래그 점수 리스트
cozem_sums = [] # 전체 코젬 합산 갯수에 따른 코젬 갯수 입력 리스트
novels = [] # 노블 사용 여부 리스트
with st.sidebar:
    choice = option_menu("Menu", ["메인페이지", "길드페이지", "기타"],
                         icons=['house', 'bi bi-emoji-smile', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# # 사이드바에 메뉴 만들기
# menu = ["메인페이지", "길드페이지", "기타"]
# choice = st.sidebar.selectbox("메뉴를 선택해주세요", menu)

# 선택된 메뉴에 따라 다른 탭 출력
if choice == "메인페이지":
    st.header("❤아기자기 길드 페이지❤")
    st.write()
    '''
    ---
    ### 아기자기 길드 페이지에 오신것을 환영합니다😊
    > * 47포 길드
    > * Lv220 이상 가입 가능
    > * 연합길드 '초초' 보유
    '''
    st.image("https://media.licdn.com/dms/image/D5622AQFO0CCKhf9Drg/feedshare-shrink_2048_1536/0/1679574361605?e=1682553600&v=beta&t=MX4A4NE3E-BJrCI_1-uh3LRAtKZWtpbofbB1ZKN-ykg", width=500)
    
    

elif choice == "길드페이지":
    tab1, tab2, tab3 = st.tabs(["😎Manager", "💎Cozem", "🎨Poster"])
    with tab1:
        st.header("😎Manager")
        st.write()
        '''
        ---
        ### 길드 간부진 💪

        | 직책 | 이름  | 직업 | 간부진 1:1오픈채팅 |
        | :---: | :---: | :---: | :---: |
        | 길마👑 | 뱌닢 | 나이트로드 | [![Colab](https://img.shields.io/badge/kakaotalk-Byanip-yellow)](https://open.kakao.com/o/spPPOAhc) |
        | 부마 | 릎샴  | 아크 | [![Colab](https://img.shields.io/badge/kakaotalk-Leupsham-yellow)](https://open.kakao.com/o/sxIoGj0c) |
        | 부마 | 둥둥향 | 캐논슈터 | [![Colab](https://img.shields.io/badge/kakaotalk-DoongDoongHyang-yellow)](https://open.kakao.com/o/sl6WBJUc) |
        | 부마 | 돌체라페  | 메르세데스 | [![Colab](https://img.shields.io/badge/kakaotalk-DolceLape-yellow)](https://open.kakao.com/o/sEmQw9Ye) |
        | 부마 | 영래곰  | 듀얼블레이드 | [![Colab](https://img.shields.io/badge/kakaotalk-DolceLape-yellow)](https://open.kakao.com/o/sBK5y3md) |
        '''
    with tab2:
        st.header("💎코어젬스톤💎")
        st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAyMDEwMTBfMTkg%2FMDAxNjAyMzE0NjY1MTM3.OCHXBz1V9YHlZgKQWBqvgPyy8dKbnDj_sAMmoL67wWIg.2XpBx6CyawstsbtIl2UTMRJeE0VHPULU1OfbbzPVJkYg.JPEG%2FexternalFile.jpg&type=a340", width=400)
        option = st.selectbox()
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
        # if __name__ == '__main__':
        #     main()


    with tab3:
        st.header("길드포스터 아카이브🎨")
        st.write("길드홍보 포스터 저장소입니다")
        option = st.selectbox(
        '원하는 포스터를 골라주세요',
        ('초기포스터', '주황', '빨강', '파랑', '오디움', '회색', '봄'))
        if option == '초기포스터':
            st.write("초기 포스터입니다")
            st.image("https://media.licdn.com/dms/image/C5622AQHPwfyHde85sQ/feedshare-shrink_800/0/1679574735456?e=1682553600&v=beta&t=Ytn7R_Z91rmAmepLWj48OFjKC_lZKyrPIU64Fb42U8M", width=500)
        elif option == '주황':
            st.write("주황색 컨셉 포스터입니다")
            st.image("https://media.licdn.com/dms/image/C5622AQGnvm84OE9XOQ/feedshare-shrink_2048_1536/0/1679574742562?e=1682553600&v=beta&t=Q20T7_h7lySXZjCr2h2WW0P8H7I1KZ3Udv3LPxxTonw", width=500)
        elif option == '빨강':
            st.write("빨간색 컨셉 포스터입니다")
            st.image("https://media.licdn.com/dms/image/D5622AQHnVCtQebUnkg/feedshare-shrink_2048_1536/0/1679574752576?e=1682553600&v=beta&t=UEFF6vu0CO9MJ-eov77W5LShxNIm9kY4Qysep0ZiUHI", width=500)
        elif option == '파랑':
            st.write("파란색 컨셉 포스터입니다")
            st.image("https://media.licdn.com/dms/image/C5622AQEB9rQJ982QuA/feedshare-shrink_2048_1536/0/1679575884228?e=1682553600&v=beta&t=Uhyaq3z2-z-65xf2WPO1er8hzP51SF4ZYlLdmMJndL4", width=500)    
        elif option == '오디움':
            st.write("오디움 컨셉 포스터입니다")
            st.image("https://media.licdn.com/dms/image/C5622AQE7RR2V8WJzkQ/feedshare-shrink_2048_1536/0/1679575867836?e=1682553600&v=beta&t=sqzte_TDGnXR0BU5OiYUF4nkFrolt17Oj-RVG-vBBRc", width=500)
        elif option == '회색':
            st.write("회색 컨셉 포스터입니다")
            st.image("https://media.licdn.com/dms/image/C5622AQF4OfxEF3RA7Q/feedshare-shrink_2048_1536/0/1679575859198?e=1682553600&v=beta&t=lNiV7RGiigxhNZsi8fYomkA7M4USwxk4Sy_7NtC2Un0", width=500)
        elif option == '봄':
            st.write("봄 컨셉 포스터입니다")
            st.image("https://media.licdn.com/dms/image/D5622AQFO0CCKhf9Drg/feedshare-shrink_2048_1536/0/1679574361605?e=1682553600&v=beta&t=MX4A4NE3E-BJrCI_1-uh3LRAtKZWtpbofbB1ZKN-ykg", width=500)    
      
        
else:


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
        selected_values = random_values(values, probabilities, n)
        for i in range(min(n, len(selected_values))):
            if selected_values[i] in ['코젬', '경뿌', '반파별4개', '수에큐3개', '소경축비']:
                st.error(f"아쉽습니다.. {selected_values[i]}(이)가 나왔습니다..")
            elif selected_values[i] in ['명큡', '앱상', '강환불', '미코젬', '주흔_한묶음']:
                st.balloons()
                st.success(f"축하드립니다! 상자에서 {selected_values[i]}(이)가 나왔습니다!")
            else:
                st.warning(f"상자에서 {selected_values[i]}(이)가 나왔습니다!")

