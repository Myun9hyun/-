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
menu = ["메인페이지", "길드페이지", "기타"]
choice = st.sidebar.selectbox("메뉴를 선택해주세요", menu)

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
    st.write()
    '''
    ---
    ### 길드 간부진 💪

    | 직책 | 이름  | 직업 | 간부진 1:1오픈채팅 |
    | :---: | :---: | :---: | :---: |
    | 길마👑 | 뱌닢 | 나이트로드 | [![GitHub](https://badgen.net/badge/icon/kakaotalk?icon=discord&/color/yellow/yellow)](https://open.kakao.com/o/spPPOAhc) |
    | 부마 | 릎샴  | 아크 | [![GitHub](https://badgen.net/badge/icon/kakaotalk?icon=discord&/color/yellow/yellow)](https://open.kakao.com/o/sxIoGj0c) |
    | 부마 | 둥둥향 | 캐논슈터 | [![GitHub](https://badgen.net/badge/icon/kakaotalk?icon=discord&/color/yellow/yellow)](https://open.kakao.com/o/sl6WBJUc) |
    | 부마 | 돌체라페  | 메르세데스 | [![GitHub](https://badgen.net/badge/icon/kakaotalk?icon=discord&/color/yellow/yellow)](https://open.kakao.com/o/sEmQw9Ye) |

    ---
    '''

elif choice == "길드페이지":
    tab1, tab2, tab3 = st.tabs(["🏠Homepage", "💎Cozem", "🎨Poster"])
    with tab1:
        st.header("🏠HomePage")
        st.write("넣을게 없음..")
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
        
        name = st.text_input("이름을 입력하세요 : ", key="name_input")
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
            st.write(f"저장이 안돼서 이건 실패..")

            weekly_total = sum(cozem_sums)
            st.write()
            st.write(f"이번주 위클리 코젬 갯수 총합 : {weekly_total}개")
           
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
    st.write()
    '''
    ### 여기도 뭐 넣을지 몰?루
    '''
