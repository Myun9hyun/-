import pandas as pd
import numpy as np
import streamlit as st

names = [] # 길드원 닉네임 입력 리스트
weekly_missions = [] # 주간미션 점수 입력 리스트
suros_cozem = [] # 수로 점수에 따른 코젬 갯수 입력 리스트
suros = []  # 수로 점수 리스트
flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
flags = []  # 플래그 점수 리스트
cozem_sums = [] # 전체 코젬 합산 갯수에 따른 코젬 갯수 입력 리스트
novels = [] # 노블 사용 여부 리스트

# 사이드바에 메뉴 만들기
menu = ["Home", "Event_reward", "Contact"]
choice = st.sidebar.selectbox("Select an option", menu)

# 선택된 메뉴에 따라 다른 탭 출력
if choice == "Home":
    st.write("아기자기 길드컨텐츠 관리 페이지")
elif choice == "Event_reward":
    st.write("Welcome to the About page")
    tab1, tab2, tab3 = st.tabs(["🏠Homepage", "💎Cozem", "Novel"])
    with tab1:
        st.header("🏠HomePage")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("💎코어젬스톤💎")
        st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAyMDEwMTBfMTkg%2FMDAxNjAyMzE0NjY1MTM3.OCHXBz1V9YHlZgKQWBqvgPyy8dKbnDj_sAMmoL67wWIg.2XpBx6CyawstsbtIl2UTMRJeE0VHPULU1OfbbzPVJkYg.JPEG%2FexternalFile.jpg&type=a340", width=400)
        def flag_cozem(f):
            # input(f"f입력 : {n}   ")
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

        def novel(): # 길드 컨텐츠 조건에 따른 노블 사용 가능 여부 출력
            if (weekly_mission >= 3) and (s > 0) and (f > 0):
                return 'O'
            elif weekly_mission == 5 and s >= 1500:
                return 'O'
            elif weekly_mission == 5 and f >= 650:
                return 'O'
            else:
                return 'X'

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
        
        # def cozem_sum(s):
        #     answer = 0
        #     answer = suro(s) + flag_cozem(f)
        #     return int(answer)
        
        name = st.text_input("이름을 입력하세요 (종료는 엔터): ", key="name_input")
        weekly_mission = int(st.number_input("주간 입력 : "))
        f = int(st.number_input("플래그 점수를 입력해주세요"))
        s = int(st.number_input("수로 점수를 입력해주세요"))

        if st.button("계산하기"):
            result_suro = suro(s)
            cozem_sum = suro(s) + flag_cozem(f)
            st.write(f"{name}님의 이번주 길드컨텐츠 코젬 갯수입니다.")
            st.write(f"플래그 점수 {int(f)}점, 수로 점수 {int(s)}점으로 총 {int(cozem_sum)}개 입니다.")
            names.append(name)
            weekly_missions.append(weekly_mission)
            suros_cozem.append(suro(s))
            suros.append(s)
            flags_cozem.append(flag_cozem(f))
            flags.append(f)
            cozem_sums.append(int(cozem_sum))
            novels.append(novel())
            st.write(f"길드컨텐츠 참여자 입니다. {names}")
            st.write(f"끝")

            weekly_total = sum(cozem_sums)
            st.write()
            st.write(f"이번주 위클리 코젬 갯수 총합 : {weekly_total}개")
            
        if st.button("계산 종료"):
            cozem_sum = suro(s) + flag_cozem(f)
            names.append(name) 
            weekly_missions.append(weekly_mission)
            suros_cozem.append(suro(s))
            suros.append(s)
            flags_cozem.append(flag_cozem(f))
            flags.append(f)
            cozem_sums.append(int(cozem_sum))
            novels.append(novel())
            st.write(f"길드컨텐츠 참여자 입니다. {names}")
            st.write(f"끝")

            weekly_total = sum(cozem_sums)
            st.write()
            st.write(f"이번주 위클리 코젬 갯수 총합 : {weekly_total}개")
           
    with tab3:
        st.header("길드컨텐츠 이행여부 차트")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
         # 데이터프레임 생성
        df = pd.DataFrame({
            'Name': names,
            'Weekly_Mission' : weekly_missions,
            'Suro' : suros,
            'Suro_Cozem' : suros_cozem, 
            'Flag' : flags,
            'Flag_Cozem' : flags_cozem,
            'Cozem_Total' : cozem_sums,
            'Novel' : novels,
            }
            )
        st.dataframe(df)
else:
    st.write("Welcome to the Contact page")
