import pandas as pd
import numpy as np
import streamlit as st

names = [] # 길드원 닉네임 입력 리스트
weekly_missions = [] # 주간미션 점수 입력 리스트
suros_cozem = [] # 수로 점수에 따른 코젬 갯수 입력 리스트
suros = []  # 수로 점수 리스트
flags_cozem = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
flags = []  # 플래그 점수 리스트
cozem_sums = [] # 플래그 점수에 따른 코젬 갯수 입력 리스트
novels = [] # 노블 사용 여부 리스트

names.append(name)
weekly_missions.append(weekly_mission)
suros_cozem.append(suro(s))
suros.append(s)
flags_cozem.append(flag_cozem(f))
flags.append(f)
cozem_sums.append(cozem_sum())
novels.append(novel())
# options = ["tab1", "tab2", "Option 3"]

# # 사이드바 위젯을 생성합니다.

# selected_option = st.sidebar.selectbox("Select an option", options)

# 사이드바에 메뉴 만들기
menu = ["Home", "Event_reward", "Contact"]
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
        f_input = st.number_input("플래그 점수를 입력해주세요")
        def suro(s):
            if s < 500 and s >= 0:
                return 0
            elif s >= 500:
                i = (s // 500)
                return i
        s_input = st.number_input("수로 점수를 입력해주세요")
        def cozem_sum():
            answer = 0
            answer = suro(s) + flag_cozem(f)
            return answer
        if st.button("계산하기"):
            result_suro = suro(s_input)
            st.write(f"플래그 점수 {f}점, 수로 점수 {s}에 따른 코젬은 {cozem_sums}개 입니다.")
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
else:
    st.write("Welcome to the Contact page")

