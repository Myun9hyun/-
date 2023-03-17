import pandas as pd
import numpy as np
import streamlit as st


# options = ["tab1", "tab2", "Option 3"]

# # 사이드바 위젯을 생성합니다.

# selected_option = st.sidebar.selectbox("Select an option", options)

# 사이드바에 메뉴 만들기
menu = ["Home", "About", "Contact"]
choice = st.sidebar.selectbox("Select an option", menu)

# 선택된 메뉴에 따라 다른 탭 출력
if choice == "Home":
    st.write("아기자기 길드컨텐츠 관리 페이지")
    
elif choice == "Event_reward":
    st.write("Welcome to the About page")
    tab1, tab2, tab3 = st.tabs(["🏠Homepage", "Cozem", "Novel"])
    with tab1:
        st.header("HomePage")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("Core Gemstone💎")
        st.image("https://search.pstatic.net/common/?src=http%3A%2F%2Fcafefiles.naver.net%2FMjAyMDEwMTBfMTkg%2FMDAxNjAyMzE0NjY1MTM3.OCHXBz1V9YHlZgKQWBqvgPyy8dKbnDj_sAMmoL67wWIg.2XpBx6CyawstsbtIl2UTMRJeE0VHPULU1OfbbzPVJkYg.JPEG%2FexternalFile.jpg&type=a340", width=400)
                def flag_cozem(f): # 플래그 점수에 따른 코젬 갯수 계산
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

        def suro(s): # 수로 점수에 따른 코젬 갯수 계산
            if s < 500 and s >= 0:
                return 0
            elif s >= 500:
                i = (s // 500)
                return i

        def cozem_sum(): # 플래그 점수와 수로 점수에 따라 계산된 코젬 갯수 합산
            total_cozem = 0
            total_cozem = suro(s) + flag_cozem(f)
            return total_cozem

        def novel(): # 길드 컨텐츠 조건에 따른 노블 사용 가능 여부 출력
            if (weekly_mission >= 3) and (s > 0) and (f > 0):
                return 'O'
            elif weekly_mission == 5 and s >= 1500:
                return 'O'
            elif weekly_mission == 5 and f >= 650:
                return 'O'
            else:
                return 'X'

        # 위클리 코젬 내야하는 갯수
        def manager(n):
            print(f"반디 : {divide_cozem(n)[1]} 개")
            print(f"샴푸 : {divide_cozem(n)[2]} 개")
            print(f"둥둥 : {divide_cozem(n)[3]} 개")
            print(f"돌체 : {divide_cozem(n)[0]} 개")

        # 이름 입력 받기
        names = [] # 길드원 닉네임 입력 리스트
        weekly_missions = [] # 주간미션 점수 입력 리스트
        suros_cozem = [] # 수로 점수에 따른 코젬 갯수 입력 리스트
        suros = []  # 수로 점수 리스트
        flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
        flags = []  # 플래그 점수 리스트
        cozem_sums = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
        novels = [] # 노블 사용 여부 리스트

        while True:
            name = str(input("이름을 입력하세요 (종료는 엔터): "))
            if name:
                weekly_mission = int(input("주간 미션 점수 입력 : "))
                # flag_cozem = int(input("f입력 : "))
                
                s = int(input("수로 점수 입력 : "))
                f = int(input("플래그 점수 입력 : "))
                
                cozem_sum()
                novel()
                # suro가 500보다 낮을때 0으로 출력되지 않고 None으로 나와서에러나는듯.. -> 해결 완료!
                
            
            if not name:
                break
            names.append(name)
            weekly_missions.append(weekly_mission)
            suros_cozem.append(suro(s))
            suros.append(s)
            flags_cozem.append(flag_cozem(f))
            flags.append(f)
            cozem_sums.append(cozem_sum())
            novels.append(novel())

        # 위클리 코젬 전체 합
        weekly_total = sum(cozem_sums)
        print(f"이번주 위클리 코젬 갯수 총합 : {weekly_total}개")

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
        divide_weekly_cozem = manager(n)
        print("이번주 위클리 코젬 분배 갯수 입니다.")
        print(divide_weekly_cozem)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
else:
    st.write("Welcome to the Contact page")

