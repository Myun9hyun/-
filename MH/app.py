import random
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
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
import os
import openpyxl
from io import BytesIO
import base64
import datetime

st.set_page_config(page_title="BanShamDoongDolYoung", page_icon=":rabbit:", layout="wide")
password = 1234

image = Image.open("MH/image/cover_guild.jpg")
# width, height = image.size
# # 이미지에 텍스트 추가
# draw = ImageDraw.Draw(image)
# text_kor = "아기자기"
# text_eng = "Welcome to"
# font_kor = ImageFont.truetype("MH/font/arial-cufonfonts/NanumSquareNeo-eHv.ttf", 50)
# font_eng = ImageFont.truetype("MH/font/arial-cufonfonts/ARIAL.TTF", 50)
# text_width, text_height = draw.textsize(text_kor, font=font_kor)

# stroke_width = 2
# stroke_fill = (0, 0, 0)

# x = text_width - 100
# y = height - text_height - 200
# z = height - text_height - 255

# # 테두리가 있는 텍스트 그리기
# draw.text((x - stroke_width, y), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x + stroke_width, y), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x, y - stroke_width), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x, y + stroke_width), text_kor, font=font_kor, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x, y), text_kor, font=font_kor, fill=(255, 255, 255))
# draw.text((x - stroke_width, z), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x + stroke_width, z), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x, z - stroke_width), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x, z + stroke_width), text_eng, font=font_eng, fill=stroke_fill, stroke_width=stroke_width)
# draw.text((x, z), text_eng, font=font_eng, fill=(255, 255, 255))


# # streamlit에 이미지 표시
st.image(image, use_column_width=True)

with st.sidebar:
    choice = option_menu("Menu", ["메인페이지", "길드페이지", "직위관리", "아카이브", "이것저것"],
                         icons=['house', 'bi bi-emoji-smile', 'bi bi-robot', 'bi bi-palette'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

    data = {
        'Name': ['💾Google Docs','📫문의방'],
        'Link': ['[![GitHub](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)](https://onedrive.live.com/edit.aspx?resid=221CE48C87202DCA!2450&ithint=file%2cxlsx&authkey=!ADKQOeLCxzQp_5o)',
         '[![GitHub](https://img.shields.io/badge/Kakao%20talk-FFBE00?style=for-the-badge&logo=kakaotalk&logoColor=white)](https://open.kakao.com/o/gUmZwuzd)']
    }
    df = pd.DataFrame(data)
    # st.sidebar.dataframe(df)
    st.write(df.to_markdown(index=False))
# choice = st.sidebar.selectbox("메뉴를 선택해주세요", menu)

# 선택된 메뉴에 따라 다른 탭 출력
if choice == "메인페이지":
    st.header("💜아기자기 길드 페이지💚")
    st.write()
    '''
    ### 아기자기 길드 페이지에 오신것을 환영합니다😊
    > * 47포 길드
    > * Lv220 이상 가입 가능
    > * 연합길드 '초초' 보유
    '''
    
    

elif choice == "길드페이지":
    tab1, tab2= st.tabs(["😎Manager", "💎Cozem"])
    with tab1:
        st.header("😎Manager")
        st.write()
        col1, col2 = st.columns(2)
        with col1:
            '''
            ---
            ### 길드 간부진 💪
            | 직책 | 이름  | 직업 | 간부진 1:1오픈채팅 |
            | :---: | :---: | :---: | :---: |
            | 길마👑 | 뱌닢 | 나이트로드 | [![Colab](https://img.shields.io/badge/kakaotalk-뱌닢-yellow)](https://open.kakao.com/o/spPPOAhc) |
            | 부마 | 릎샴  | 아크 | [![Colab](https://img.shields.io/badge/kakaotalk-릎샴-yellow)](https://open.kakao.com/o/s0FeFIee) |
            | 부마 | 둥둥향 | 캐논슈터 | [![Colab](https://img.shields.io/badge/kakaotalk-둥둥향-yellow)](https://open.kakao.com/o/sl6WBJUc) |
            | 부마 | 돌체라페  | 메르세데스 | [![Colab](https://img.shields.io/badge/kakaotalk-돌체라페-yellow)](https://open.kakao.com/o/sEmQw9Ye) |
            | 부마 | 영래곰  | 듀얼블레이드 | [![Colab](https://img.shields.io/badge/kakaotalk-영래곰-yellow)](https://open.kakao.com/o/sBK5y3md) |
            '''

        with col2:
            st.image("MH/image/elinel.jpg", use_column_width=True)
    with tab2:
        st.header("💎코어젬스톤💎")
      
elif choice == "직위관리":
    st.header("길드원 직위 관리 페이지")
    tab1, tab2, tab3, tab4 = st.tabs(["💎Cozem", "📋Grade", "❌Warning", "⏸Pause"])
    with tab1:
        st.header("💎코어젬스톤💎")
        st.image("MH/image/cozem_guild.jpg", use_column_width=True)
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
        FILE_PATH5 = 'data5.csv'

        # 파일에서 데이터 불러오기
        def load_data():
            try:
                data = pd.read_csv(FILE_PATH)
            except FileNotFoundError:
                data = pd.DataFrame(columns=['Name', 'Weekly_Mission', 'Suro', 'Flag', 'Cozem_Total', 'Novel', 'Role','Main_Name'])
            return data
        def load_data5():
            try:
                data5 = pd.read_csv(FILE_PATH5)
            except FileNotFoundError:
                data5 = pd.DataFrame(columns=['Name'])
            return data5

        # 데이터를 파일에 저장하기
        def save_data(data):
            data.to_csv(FILE_PATH, index=False)

        def save_data5(data5):
            data5.to_csv(FILE_PATH5, index=False)

        # 데이터 초기화 함수
        def clear_data():
            global data, data5
            data = pd.DataFrame(columns=['Name', 'Weekly_Mission', 'Suro', 'Flag', 'Cozem_Total', 'Novel', 'Role','Main_Name'])
            data5 = pd.DataFrame(columns=['Name'])
            # 파일 삭제
            os.remove(FILE_PATH)
            os.remove(FILE_PATH5)
        # 데이터 삭제 함수
        def delete_data(row_index):
            global data
            data = data.drop(index=row_index).reset_index(drop=True)
        def delete_data5(row_index):
            global data5
            data5 = data5.drop(index=row_index).reset_index(drop=True)
        # 불러온 데이터를 전역 변수로 저장
        data = load_data()
        data5 = load_data5()
        def add_name(names): # 낮 품목 저장
            global data5 
            if names in data5['Name'].values:
                # st.warning(f'{names} (은)는 이미 있는 이름ㅇㅇ이야!')
                return
            data5 = data5.append({'Name': names}, ignore_index=True)

        def add_data(name,character_type, weekly_mission, suro, flag):
            global data
            # role = st.radio("본캐/부캐 선택", ("본캐", "부캐"))
            if character_type == "부캐":
                main_name = st.text_input("본캐의 이름을 입력하세요.")
                if main_name not in data['Name'].values:
                    st.warning(f'{main_name} (은)는 존재하지 않는 이름이야!')
                    return
                main_row = data[data['Name'] == main_name].iloc[0]
                data = data.append({
                    'Name': name, 
                    'Weekly_Mission': weekly_mission, 
                    'Suro': suro,
                    'Suro_Cozem': suro_cozem,  # suro_cozem 값을 추가
                    'Flag': flag, 
                    'Flag_Cozem': flag_cozem,  # flag_cozem 값을 추가
                    'Cozem_Total': main_row['Cozem_Total'] + (Suro_cozem(suro) + Flag_cozem(flag)),
                    'Novel': novel_p(weekly_mission, suro, flag),
                    'Role': role,
                    'Main_Name': main_name,
                }, ignore_index=True)
            else:
                # 중복 검사
                if name in data['Name'].values:
                    # st.warning(f'{name} (은)는 이미 있는 이름이야!')
                    return
                suro_cozem = Suro_cozem(suro)  # Suro_cozem 함수를 이용해 suro_cozem 값을 계산
                flag_cozem = Flag_cozem(flag)  # flag_cozem 함수를 이용해 flag_cozem 값을 계산
                cozem_total = suro_cozem + flag_cozem  # 코젬 총합 계산
                novel_value = novel_p(weekly_mission, suro, flag)  # Novel 값 계산
                data = data.append({
                    'Name': name, 
                    'Weekly_Mission': weekly_mission, 
                    'Suro': suro,
                    'Suro_Cozem': suro_cozem,
                    'Flag': flag, 
                    'Flag_Cozem': flag_cozem,
                    'Cozem_Total': cozem_total,  # 코젬 총합 값을 추가
                    'Novel': novel_value,  # Novel 값을 추가
                    'Role': '본캐',
                    'Main_Name' : '본캐'
                }, ignore_index=True)

        # def role(Role):
        def add_character_data(name, character_type, weekly_mission, suro, flag):
            global data, data5
            add_name(name)  # 입력된 이름을 데이터에 추가
            if character_type == '본캐':
                add_data(name,character_type, weekly_mission, suro, flag)
            elif character_type == '부캐':
                main_name = st.text_input('본캐 이름을 입력하세요')
                main_data = data.loc[data['Name'] == main_name]
                if len(main_data) == 0:
                    st.warning(f"{main_name} (은)는 등록되어있지 않아!.")
                    return
                else:
                    main_data_index = main_data.index[0]
                    suro_cozem = Suro_cozem(suro)
                    flag_cozem = Flag_cozem(flag)
                    cozem_total = suro_cozem + flag_cozem
                    data.loc[main_data_index, 'Cozem_Total'] += cozem_total
                    if main_data['Suro'].values[0] >= 4000:
                        novel_value = main_data['Novel'].values[0]
                    else:
                        novel_value = novel_p(weekly_mission, suro, flag)  # Novel 값 계산
                    if weekly_mission >= 2:
                        novel_value = main_data['Novel'].values[0]
                    else:
                        novel_value = novel_p(weekly_mission, suro, flag)
                    role = character_type
                    warning_count = 0
                    warning_main = data[(data['Novel'] == 'X') & (data['Role'] == '본캐')]
                    if name in warning_main['Name'].values:
                        warning_count = warning_count + 1
                    data = data.append({
                        'Name': name, 
                        'Weekly_Mission': weekly_mission, 
                        'Suro': suro, 
                        'Suro_Cozem': suro_cozem,
                        'Flag': flag, 
                        'Flag_Cozem': flag_cozem,
                        'Cozem_Total': cozem_total,
                        'Novel': novel_value,
                        'Role' : role,
                        'Main_Name' : main_name
                    }, ignore_index=True)
            else:
                st.warning(f"{character_type} (은)는 본캐/부캐가 아닙니다!")

        def download_xlsx(df, file_name):
            # 파일 확장자가 .xlsx가 아니면 파일명 끝에 .xlsx를 붙여줌
            if not file_name.endswith(".xlsx"):
                file_name += ".xlsx"
            # 파일을 열어 BytesIO 객체에 쓰기
            with BytesIO() as buffer:
                df.to_excel(buffer, index=False)
                # 파일 포인터를 맨 앞으로 이동시켜 파일 내용을 읽음
                buffer.seek(0)
                # 다운로드 링크 생성
                b64 = base64.b64encode(buffer.read()).decode()
                return f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{file_name}">다운로드</a>'


        def main():
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
            password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0)
            if password_input == password:
                st.success('접근을 허용합니다')
                options = ["이름추가","데이터 추가➕", "데이터 조회🔎", "데이터 삭제✂", "데이터 초기화💣", "노블 사용⭕제한❌", "위클리 코젬 계산📋", "데이터 다운로드💾"]
                option = st.selectbox("기능 선택", options)
                
                if option == "데이터 추가➕":
                    select_name = st.selectbox('이름을 골라줘(❁´◡`❁)', options=data5['Name'].tolist())
                    is_main_character = st.radio('본캐/부캐', ('본캐', '부캐'))
                    weekly_mission = st.number_input('주간 미션 점수를 입력해주세요', min_value=0)
                    suro = st.number_input('수로 점수를 입력해주세요', min_value=0)
                    flag = st.number_input('플래그 점수를 입력해주세요', min_value=0)
                    add_character_data(select_name, is_main_character, weekly_mission, suro, flag)
                    if st.button('추가하기'):
                        save_data(data)  # 데이터를 파일에 저장
                        st.success(f'{select_name}의 데이터가 추가되었습니다!')
                elif option == "이름추가":
                    
                    name = st.text_input('이름을 입력해줘')
                
            # 이름, 점수, 포인트가 입력되면 데이터프레임에 추가
                    if st.button('이름추가'):
                        if name in data5['Name'].values:
                            st.warning(f"{name}은(는) 이미 있는 이름이야!")
                            return
                        else:
                        # if st.button('추가'):
                            add_name(name)
                            save_data5(data5)  # 데이터를 파일에 저장
                            st.success('이름이 추가되었어!')
                    

                elif option == "데이터 조회🔎":
                    # 저장된 데이터
                    st.write("버튼을 누르면 입력하신 데이터를 확인할 수 있습니다.")
                    if st.button('차트 열기'):
                        if not data.empty:
                            st.write(data[['Name', 'Weekly_Mission', 'Suro', 'Suro_Cozem', 'Flag', 'Flag_Cozem', 'Cozem_Total', 'Novel','Role','Main_Name']])
                        else:
                            st.write('입력되어있는 데이터가 없습니다.')
                
                elif option == "데이터 삭제✂":
                    st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ')
                    if password_input == password:
                        st.success('접근을 허용합니다')
                    # 데이터 삭제 기능
                    # if st.button('데이터 삭제'):
                        # 사용자로부터 삭제할 행 번호 입력받기
                        st.write(data[['Name', 'Weekly_Mission', 'Suro', 'Suro_Cozem', 'Flag', 'Flag_Cozem', 'Cozem_Total', 'Novel','Role','Main_Name']])
                        row_index = st.number_input('삭제하고 싶은 데이터의 번호를 입력해주세요', min_value=0, max_value=data.shape[0]-1)
                        st.write("Enter를 입력하면 삭제됩니다.")
                        if st.button('데이터 삭제'):
                            # 해당 행이 존재할 경우, 행을 삭제
                            if row_index >= 0 and row_index < data.shape[0]:
                                delete_data(row_index)
                                save_data(data)  # 데이터를 파일에 저장
                                st.success('입력하신 행이 삭제되었습니다.')
                    else:
                        st.warning('비밀번호가 틀렸습니다.')

                elif option == "데이터 초기화💣":
                    st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0,key='pass1')
                    if password_input == password:
                        st.success('접근을 허용합니다')
                        # 데이터 전부 삭제
                        st.write("⚠️버튼을 누르면 데이터가 다 날아갑니다!⚠️")
                        st.write("⚠️신중하게 누르세요!!⚠️")
                        if st.button('차트 초기화'):
                            clear_data()
                            st.warning('차트가 초기화 되었습니다')
                    else:
                        st.warning('비밀번호가 틀렸습니다.')
                elif option == "노블 사용⭕제한❌":
                    if st.button('노블 제한목록 보기'):
                    # 경고자 명단
                        warning = data[data['Novel'] == 'X']
                        warning_list = warning['Name'].tolist()
                        warning_WM = warning[warning['Weekly_Mission'] < 3]
                        warning_WM_list = warning_WM['Name'].tolist()
                        warning_suro = warning[warning['Suro'] == 0]
                        warning_suro_list = warning_suro['Name'].tolist()
                        warning_flag = warning[warning['Flag'] == 0]
                        warning_flag_list = warning_flag['Name'].tolist()
                        warning_main = data[(data['Novel'] == 'X') & (data['Role'] == '본캐')]
                        warning_main_list = warning_main['Name'].tolist()


                        if not warning_main_list:
                            st.write('이번주 노블 사용제한자는 없습니다.')
                        else:
                            st.write('이번주 경고자 목록입니다(본캐).')
                            st.write(f"경고자 :  {warning_main_list}.")
                            st.write(warning_main)
                        if not warning_list:
                            st.write('이번주 노블 사용제한자는 없습니다.')
                        else:
                            st.write('이번주 노블 사용제한 목록 입니다.')
                            st.write(f"노블 제한자 :  {warning_list}.")
                            st.write(data[data['Novel'] == 'X'])
                        if not warning_WM_list:
                            st.write('이번주 주간미션 미달자는 없습니다.')
                        else:
                            st.write(f"노블 제한자 중 주간미션 미달자입니다 :  {warning_WM_list}.")
                        if not warning_suro_list:
                            st.write('이번주 지하수로 미실시자는 없습니다.')
                        else:
                            st.write(f"노블 제한자 중 지하수로 미실시자입니다 :  {warning_suro_list}.")
                        if not warning_flag_list:
                            st.write('이번주 플래그 미실시자는 없습니다.')
                        else:
                            st.write(f"노블 제한자 중 플래그 미실시자입니다 :  {warning_flag_list}.")

                    
                    if st.button('노블 사용가능 목록 보기'):
                        # 먼슬리 참여 가능자 명단
                        novel_member = data[data['Novel'] == 'O']
                        monthly = data[(data['Novel'] == 'O') & (data['Role'] == '본캐')]
                        novel_list = novel_member['Name'].tolist()
                        monthly_list = monthly['Name'].tolist()
                        
                        st.write('이번주 노블 사용가능 목록입니다.')
                        st.write(f"노블 사용가능자 :  {novel_list}.")
                        st.write(novel_member)
                        st.write('이번주 먼슬리 참여가능자 목록입니다.')
                        st.write(f"먼슬리 참여가능자 :  {monthly_list}.")
                        st.write(monthly)

                elif option == "위클리 코젬 계산📋":
                    if st.button('위클리 코젬 합계 계산'):
                        weekly_main = data[(data['Role'] == '본캐')]
                        weekly_main_total = weekly_main['Cozem_Total'].sum()
                        # weekly_total = data['Cozem_Total'].sum()
                        # st.write(f"이번주 위클리 이벤트 코젬의 합은{weekly_total}개 입니다.")
                        st.write(f"이번주 위클리 이벤트 코젬의 합은{weekly_main_total}개 입니다.")
                        st.write(weekly_main)

                    if st.button('위클리 코젬 분배 계산'):
                        weekly_main = data[(data['Role'] == '본캐')]
                        weekly_main_total = weekly_main['Cozem_Total'].sum()
                        quotient = weekly_main_total // 5
                        remainder = weekly_main_total % 5
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
                        st.write(f"이번주 위클리 이벤트 코젬은 총 {weekly_main_total}개 입니다.")
                        st.write(f"반디 : {a} 개")
                        st.write(f"샴푸 : {b} 개")
                        st.write(f"둥둥 : {c} 개")
                        st.write(f"돌체 : {d} 개")
                        st.write(f"영래 : {e} 개")
                elif option == "데이터 다운로드💾":
                    st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ', min_value=0, key='password2')
                    if password_input == password:
                        st.success('접근을 허용합니다')
                        # 다운로드 버튼 클릭
                        if st.button("다운로드"):
                            file_name = st.text_input("저장할 파일명을 입력하세요:", "아기자기.xlsx")
                            st.markdown(download_xlsx(data, file_name), unsafe_allow_html=True)
            else:
                st.warning('비밀번호가 틀렸습니다.')
                # else:
                #     st.warning('비밀번호가 틀렸습니다.')

        if __name__ == '__main__':
                main()
    with tab2:
        # 업로드한 파일을 데이터프레임으로 변환하는 함수
        st.header("직위 관리 페이지")

        # 업로드된 엑셀 파일을 저장하고, 데이터프레임으로 변환하는 함수
        def upload_excel_file(uploadedfile):
            df = pd.read_excel(uploadedfile, engine="openpyxl")
            return df

        # 엑셀 파일을 저장하는 함수
        def save_uploaded_file(uploadedfile):
            with open(uploadedfile.name, 'wb') as f:
                f.write(uploadedfile.getbuffer())
            return st.success("저장되었습니다: {}".format(uploadedfile.name))

        # Streamlit 앱
        def main():
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
            password_input = st.number_input('비밀번호를 입력해주세요 : ', min_value=0, key='password1')
            if password_input == password:
                st.success('접근을 허용합니다')
                st.write()
                '''
                ### ❗파일 업로드 하면 에러 없어짐❗
                '''
                st.write("지난주 길드컨텐츠 참여목록 엑셀을 업로드 해주세요")
                uploaded_file1 = st.file_uploader("Excel 파일 업로드", type=["xlsx"], key="upload1")

                if uploaded_file1 is not None:
                    # 업로드한 파일을 저장하고, 데이터프레임으로 변환
                    save_uploaded_file(uploaded_file1)
                    df1 = upload_excel_file(uploaded_file1)

                    # 데이터프레임 출력
                    st.write("지난주 길드컨텐츠 참여자")
                    st.write(df1)

                st.write("이번주 길드컨텐츠 참여목록 엑셀을 업로드 해주세요")
                uploaded_file2 = st.file_uploader("Excel 파일 업로드", type=["xlsx"], key="upload2")

                if uploaded_file2 is not None:
                    # 업로드한 파일을 저장하고, 데이터프레임으로 변환
                    save_uploaded_file(uploaded_file2)
                    df2 = upload_excel_file(uploaded_file2)

                    # 데이터프레임 출력
                    st.write("이번주 길드컨텐츠 참여자")
                    st.write(df2)

                df1_O = df1[df1['Novel'] == 'O']
                df1_X = df1[df1['Novel'] == 'X']
                
                df2_O = df2[df2['Novel'] == 'O']
                df2_X = df2[df2['Novel'] == 'X']

                name1O_index = df1_O['Name'].tolist()
                name1X_index = df1_X['Name'].tolist()
                name2O_index = df2_O['Name'].tolist()
                name2X_index = df2_X['Name'].tolist()

                novel_down = name1O_index and name2X_index
                novel_up = name1X_index and name2O_index
                if st.button("직위 상승/하락자 목록"):
                    if not novel_up:
                        st.write("이번주 직위 상승자는 없습니다.")
                    else : 
                        st.write(f"이번주 직위 상승자는 다음과 같습니다 :  {novel_up} ")
                    if not novel_down:
                        st.write("이번주 직위 하락자는 없습니다.")
                    else:
                        st.write(f"이번주 직위 하락자는 다음과 같습니다 :  {novel_down} ")
            else:
                st.warning('비밀번호가 틀렸습니다.')
    
        if __name__ == "__main__":
            main()
    with tab3:
        st.header("❗경고자 관리❗")
        FILE_PATH1 = 'data1.csv'
        st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
        password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0, key='password3')
        if password_input == password:
            st.success('접근을 허용합니다')
            options = ["경고자 추가➕","경고횟수 추가/차감", "경고자 조회🔎", "경고자 삭제✂", "데이터 초기화💣" ]
            option = st.selectbox("기능 선택", options, key='select1')
        # 파일에서 데이터 불러오기
            def load_data1():
                try:
                    data1 = pd.read_csv(FILE_PATH1)
                except FileNotFoundError:
                    data1 = pd.DataFrame(columns=['Name', 'Warning'])
                return data1

            # 데이터를 파일에 저장하기
            def save_data1(data1):
                data1.to_csv(FILE_PATH1, index=False)

            # 데이터 초기화 함수
            def clear_data1():
                global data1
                data1 = pd.DataFrame(columns=['Name', 'Warning'])
                # 파일 삭제
                os.remove(FILE_PATH1)
            # 데이터 삭제 함수
            def delete_data(row_index):
                global data1
                data1 = data1.drop(index=row_index).reset_index(drop=True)

            # 불러온 데이터를 전역 변수로 저장
            data1 = load_data1()
            def add_data1(name, warning_count):
                global data1
                if name in data1['Name'].values:
                    st.warning(f'{name} (은)는 이미 있는 이름이야!')
                    return
                data1 = data1.append({
                    'Name': name, 
                    'Warning' : warning_count
                }, ignore_index=True)
            

            def main():
                if option == "경고자 삭제✂":
                    st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0, key='pass3')
                    if password_input == password:
                        st.success('접근을 허용합니다')
                    # 데이터 삭제 기능
                    # if st.button('데이터 삭제'):
                        # 사용자로부터 삭제할 행 번호 입력받기
                        st.write(data1[['Name','Warning']])
                        row_index = st.number_input('삭제하고 싶은 데이터의 번호를 입력해주세요', min_value=0, max_value=data1.shape[0]-1)
                        st.write("Enter를 입력하면 삭제됩니다.")
                        if st.button('데이터 삭제'):
                            # 해당 행이 존재할 경우, 행을 삭제
                            if row_index >= 0 and row_index < data1.shape[0]:
                                delete_data(row_index)
                                save_data1(data1)  # 데이터를 파일에 저장
                                st.success('입력하신 행이 삭제되었습니다.')
                    else:
                        st.warning('비밀번호가 틀렸습니다.')
                elif option == "경고자 추가➕":
                    name = st.text_input("경고자 이름을 입력해주세요")
                    warning_count = data1.loc[data1['Name']==name, 'Warning'].values[0] if name in data1['Name'].values else 0
                    if st.button('경고자 이름 추가'):
                        add_data1(name, warning_count)
                        save_data1(data1)
                        st.success(f"경고자 {name}이(가) 추가되었습니다.")
                elif option == '경고횟수 추가/차감':
                    name = st.text_input("경고자 이름을 입력해주세요")
                    filtered_data = data1.loc[data1['Name'] == name, 'Warning']
                    if not filtered_data.empty:
                        warning_count = filtered_data.iloc[0]
                        if st.button("경고횟수 추가"):
                            warning_count += 1
                            data1.loc[data1['Name'] == name, 'Warning'] = warning_count
                            save_data1(data1)
                            st.success("경고 횟수가 증가되었습니다.")
                        if st.button("경고횟수 차감"):
                            warning_count -= 1
                            data1.loc[data1['Name'] == name, 'Warning'] = warning_count
                            save_data1(data1)
                            st.success('경고 횟수가 차감되었습니다.')
                    else:
                        st.warning("입력한 이름에 해당하는 데이터가 없습니다.")


                elif option == "경고자 조회🔎":
                    if st.button('경고 횟수 확인'):
                        warning_one = data1[data1['Warning'] == 1]
                        warning_two = data1[data1['Warning'] == 2]
                        warning_one_list = warning_one['Name'].tolist()
                        warning_two_list = warning_two['Name'].tolist()
                        st.write("경고자 전체 명단입니다.")
                        st.write(data1)
                        if not warning_one_list:
                            st.write("경고 1회자는 없습니다.")
                        else : 
                            st.write("경고 1회 명단입니다.")
                            st.write(f"{warning_one_list}")
                        if not warning_two_list:
                            st.write("경고 2회자는 없습니다.")
                        else : 
                            st.write("경고 2회 명단입니다.")
                            st.write(f"{warning_two_list}")

                elif option == "데이터 초기화💣":
                    st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0,key='pass2')
                    if password_input == password:
                        st.success('접근을 허용합니다')
                        # 데이터 전부 삭제
                        st.write("⚠️버튼을 누르면 데이터가 다 날아갑니다!⚠️")
                        st.write("⚠️신중하게 누르세요!!⚠️")
                        if st.button('차트 초기화'):
                            clear_data1()
                            st.warning('차트가 초기화 되었습니다')
                    else:
                        st.warning('비밀번호가 틀렸습니다.')
            if __name__ == "__main__":
                main()
        else:
            st.warning('비밀번호가 틀렸습니다.')    
    with tab4 :
        st.header("⏸유예기간 관리⏸")
        FILE_PATH2 = 'data2.csv'
        st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
        password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0, key='password5')
        if password_input == password:
            st.success('접근을 허용합니다')
            options = ["유예자 추가➕", "유예자 조회🔎", "유예자 삭제✂", "데이터 초기화💣" ]
            option = st.selectbox("기능 선택", options, key='select3')
        # 파일에서 데이터 불러오기
            def load_data2():
                try:
                    data2 = pd.read_csv(FILE_PATH2)
                except FileNotFoundError:
                    data2 = pd.DataFrame(columns=['Name', 'Why', 'Period'])
                return data2

            # 데이터를 파일에 저장하기
            def save_data2(data2):
                data2.to_csv(FILE_PATH2, index=False)

            # 데이터 초기화 함수
            def clear_data2():
                global data2
                data2 = pd.DataFrame(columns=['Name', 'Why', 'Period'])
                # 파일 삭제
                os.remove(FILE_PATH2)
            # 데이터 삭제 함수
            def delete_data2(row_index):
                global data2
                data2 = data2.drop(index=row_index).reset_index(drop=True)

            # 불러온 데이터를 전역 변수로 저장
            data2 = load_data2()
            def add_data2(name, why, period):
                global data2
                if name in data2['Name'].values:
                    st.warning(f'{name} (은)는 이미 있는 이름이야!')
                    return
                data2 = data2.append({
                    'Name': name, 
                    'Why' : why,
                    'Period' : period

                }, ignore_index=True)
            

            def main():
                if option == "유예자 삭제✂":
                    st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0, key='pass4')
                    if password_input == password:
                        st.success('접근을 허용합니다')
                    # 데이터 삭제 기능
                    # if st.button('데이터 삭제'):
                        # 사용자로부터 삭제할 행 번호 입력받기
                        st.write(data2[['Name','Why', 'Period']])
                        row_index = st.number_input('삭제하고 싶은 데이터의 번호를 입력해주세요', min_value=0, max_value=data2.shape[0]-1)
                        st.write("Enter를 입력하면 삭제됩니다.")
                        if st.button('데이터 삭제'):
                            # 해당 행이 존재할 경우, 행을 삭제
                            if row_index >= 0 and row_index < data2.shape[0]:
                                delete_data2(row_index)
                                save_data2(data2)  # 데이터를 파일에 저장
                                st.success('입력하신 행이 삭제되었습니다.')
                    else:
                        st.warning('비밀번호가 틀렸습니다.')
                elif option == "유예자 추가➕":
                    name = st.text_input("유예자 이름을 입력해주세요")
                    why = st.text_input("사유를 입력해주세요(곤란하면 개인사유로 작성)")
                    day = st.date_input(
                        "유예기한을 설정해주세요",
                        datetime.date(2023, 4, 10))
                    if st.button('유예자 이름 추가'):
                        add_data2(name, why, day)
                        save_data2(data2)
                        st.success(f"유예자 {name}이(가) 추가되었습니다.")

                elif option == "유예자 조회🔎":
                    if st.button('유예자 확인'):
                        st.write("유예자 명단입니다.")
                        st.write(data2)

                elif option == "데이터 초기화💣":
                    st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0,key='pass6')
                    if password_input == password:
                        st.success('접근을 허용합니다')
                        # 데이터 전부 삭제
                        st.write("⚠️버튼을 누르면 데이터가 다 날아갑니다!⚠️")
                        st.write("⚠️신중하게 누르세요!!⚠️")
                        if st.button('차트 초기화'):
                            clear_data2()
                            st.warning('차트가 초기화 되었습니다')
                    else:
                        st.warning('비밀번호가 틀렸습니다.')
            if __name__ == "__main__":
                main()
        else:
            st.warning('비밀번호가 틀렸습니다.')
        

elif choice == "아카이브":
    st.header("길드 아카이브")
    options = st.selectbox(
    '원하는 종류를 골라주세요',
    ('포스터', '길드사진'))
    if options=='포스터':
        st.write("길드포스터 아카이브🎨")
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
    elif options=='길드사진':
        st.write("길드 사진 아카이브입니다.")
        col1, col2=st.columns(2)
        with col1:
            st.write("**리나와 한컷**")
            st.image("MH/image/guild1.jpg", use_column_width=True)
        with col2:
            st.write("**왕의 쉼터**")
            st.image("MH/image/guild2.jpg", use_column_width=True)
        col3, col4 = st.columns(2)
        with col3:
            st.write("**옷맞춤**")
            st.image("MH/image/guild3.jpg", use_column_width=True)
        with col4:
            st.write("**엘리넬**")
            st.image("MH/image/elinel.jpg", use_column_width=True)
else:
    tab1, tab2, tab3= st.tabs(["🎁Random Box", "🔗Link","🏚Attic"])
    with tab1:
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
        | 꽝💣 | 코젬, 경뿌, 반파별4개, 소경축비, 수에큐3개 | 7.4% |
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

    with tab2:
        tab2.subheader("🖇️ Link Tab")
        tab2.write("각종 링크는 아래에 있습니다.")
        st.write()
        '''
        ---
        | 구분 | 이름  | 링크 | 
        | :---: | :---: | :---: | 
        | GoogleDocs | 📑아기자기명단 | [![Colab](https://img.shields.io/badge/GoogleDocs-아기자기명단-green)](https://onedrive.live.com/edit.aspx?resid=221CE48C87202DCA!2450&ithint=file%2cxlsx&authkey=!ADKQOeLCxzQp_5o) | 
        '''
    with tab3:
        FILE_PATH1 = 'data1.csv'
        FILE_PATH2 = 'data2.csv'
        FILE_PATH3 = 'data3.csv'
        FILE_PATH4 = 'data4.csv'
        FILE_PATH5 = 'data5.csv'

        # 파일에서 데이터 불러오기
        def load_data(): #낮 품목
            try:
                data = pd.read_csv(FILE_PATH1)
            except FileNotFoundError:
                data = pd.DataFrame(columns=['Name', 'Price', 'Mount'])
            return data

        def load_data2():
            try:
                data2 = pd.read_csv(FILE_PATH2)
            except FileNotFoundError:
                data2 = pd.DataFrame(columns=['Name', 'Point'])
            return data2

        def load_data3():
            try:
                data3 = pd.read_csv(FILE_PATH3)
            except FileNotFoundError:
                data3 = pd.DataFrame(columns=['Name', 'Product', 'Mount'])
            return data3

        def load_data4(): # 밤 품목
            try:
                data4 = pd.read_csv(FILE_PATH4)
            except FileNotFoundError:
                data4 = pd.DataFrame(columns=['Name', 'Price', 'Mount'])
            return data4
        def load_data5(): # 밤 장바구니
            try:
                data5 = pd.read_csv(FILE_PATH5)
            except FileNotFoundError:
                data5 = pd.DataFrame(columns=['Name', 'Product', 'Mount'])
            return data5

        # 데이터를 파일에 저장하기
        def save_data(data):
            data.to_csv(FILE_PATH1, index=False)

        def save_data2(data2):
            data2.to_csv(FILE_PATH2, index=False)

        def save_data3(data3):
            data3.to_csv(FILE_PATH3, index=False)

        def save_data4(data4):
            data4.to_csv(FILE_PATH4, index=False)

        def save_data5(data5):
            data5.to_csv(FILE_PATH5, index=False)

        # 데이터 초기화 함수
        def clear_data():
            global data, data2, data3, data4, data5
            data = pd.DataFrame(columns=['Name', 'Price', 'Mount'])
            data2 = pd.DataFrame(columns=['Name', 'Point','Product'])
            data3 = pd.DataFrame(columns=['Name', 'Product', 'Mount'])
            data4 = pd.DataFrame(columns=['Name', 'Price', 'Mount'])
            data5 = pd.DataFrame(columns=['Name', 'Product', 'Mount'])
            # 파일 삭제
            os.remove(FILE_PATH1)
            os.remove(FILE_PATH2)
            os.remove(FILE_PATH3)
            os.remove(FILE_PATH4)
            os.remove(FILE_PATH5)

        # 불러온 데이터를 전역 변수로 저장
        data = load_data()
        data2 = load_data2()
        data3 = load_data3()
        data4 = load_data4()
        data5 = load_data5()

        # 사용자로부터 이름, 점수, 포인트, 수량을 입력받아 데이터프레임에 추가하는 함수
        def add_data(name, price, mount): # 낮 품목 저장
            global data
            if name in data['Name'].values:
                        st.warning(f'{name} (은)는 이미 있는 품목이야!')
                        return
            data = data.append({'Name': name, 'Price': price, 'Mount': mount}, ignore_index=True)

        def add_data4(name, price, mount): # 밤 품목 저장
            global data4
            if name in data4['Name'].values:
                        st.warning(f'{name} (은)는 이미 있는 품목이야!')
                        return
            data4 = data4.append({'Name': name, 'Price': price, 'Mount': mount}, ignore_index=True)

        def add_data2(name, point): # 포인트 배분 
            global data2
            if name in data2['Name'].values:
                        st.warning(f'{name} (은)는 이미 있는 이름이야!')
                        return
            data2 = data2.append({'Name': name, 'Point': point}, ignore_index=True)

        def add_data3(name, price, mount):
            global data3
            data3 = data3.append({'Name': name, 'Price': price, 'Mount': mount}, ignore_index=True)

        def add_data5(name, price, mount):
            global data5
            data5 = data5.append({'Name': name, 'Price': price, 'Mount': mount}, ignore_index=True)

        def purchase_item(name, product_name, mount): # 낮 구매하기
            global data, data2
            # data에서 product_name에 해당하는 row 선택
            row = data[data['Name'] == product_name].iloc[0]
            # data2에서 name에 해당하는 row 선택
            row2 = data2[data2['Name'] == name].iloc[0]
            # 구매하고자 하는 수량만큼 차감
            if row['Mount'] >= mount:
                data.loc[data['Name'] == product_name, 'Mount'] -= mount
                save_data(data)
                # 품목 가격만큼 point 차감
                total_price = row['Price'] * mount
                if row2['Point'] >= total_price:
                    # 데이터프레임에 구매내역 추가
                    data3 = load_data3()
                    purchase_df = data3[(data3['Name'] == name) & (data3['Product'] == product_name)]
                    if purchase_df.empty:
                        purchase_df = pd.DataFrame({
                            'Name': [name],
                            'Product': [product_name],
                            'Mount': [mount]
                        })
                        data3 = pd.concat([data3, purchase_df], ignore_index=True)
                    else:
                        data3.loc[(data3['Name'] == name) & (data3['Product'] == product_name), 'Mount'] += mount
                    save_data3(data3)
                    # 구매자의 포인트 차감
                    data2.loc[data2['Name'] == name, 'Point'] -= total_price
                    save_data2(data2)
                    st.success(f'{product_name} {mount}개 구매 완료!')
                    # # 구매내역 호출 버튼 생성
                    # st.button("구매내역 확인", on_click=view_purchase_history)
                else:
                    st.warning(f'{name}은(는) {product_name}을(를) 구매할 포인트가 부족해!(┬┬﹏┬┬)')
            else:
                st.warning(f'{product_name}(은)는 품절되었어(⊙_⊙;)')

        def purchase_item2(name, product_name, mount): # 밤 구매하기
            global data4, data2
            # data에서 product_name에 해당하는 row 선택
            row = data4[data4['Name'] == product_name].iloc[0]
            # data2에서 name에 해당하는 row 선택
            row2 = data2[data2['Name'] == name].iloc[0]
            # 구매하고자 하는 수량만큼 차감
            if row['Mount'] >= mount:
                data4.loc[data4['Name'] == product_name, 'Mount'] -= mount
                save_data4(data4)
                # 품목 가격만큼 point 차감
                total_price = row['Price'] * mount
                if row2['Point'] >= total_price:
                    # 데이터프레임에 구매내역 추가
                    data5 = load_data5()
                    purchase_df = data5[(data5['Name'] == name) & (data5['Product'] == product_name)]
                    if purchase_df.empty:
                        purchase_df = pd.DataFrame({
                            'Name': [name],
                            'Product': [product_name],
                            'Mount': [mount]
                        })
                        data5 = pd.concat([data5, purchase_df], ignore_index=True)
                    else:
                        data5.loc[(data5['Name'] == name) & (data5['Product'] == product_name), 'Mount'] += mount
                    save_data5(data5)
                    # 구매자의 포인트 차감
                    data2.loc[data2['Name'] == name, 'Point'] -= total_price
                    save_data2(data2)
                    st.success(f'{product_name} {mount}개 구매 완료!')
                    # # 구매내역 호출 버튼 생성
                    # st.button("구매내역 확인", on_click=view_purchase_history)
                else:
                    st.warning(f'{name}은(는) {product_name}을(를) 구매할 포인트가 부족해!(┬┬﹏┬┬)')
            else:
                st.warning(f'{product_name}(은)는 품절되었어(⊙_⊙;)')


        def save_purchase_history(name, product_name, mount): # 낮 구매내역 저장
            global data3
            data3 = data3.append({'Name': name, 'Product': product_name, 'Mount': mount}, ignore_index=True)
        def save_purchase_history2(name, product_name, mount): # 밤 구매내역 저장
            global data5
            data5 = data5.append({'Name': name, 'Product': product_name, 'Mount': mount}, ignore_index=True)
            
        def delete_data(row_index):
                    global data
                    data = data.drop(index=row_index).reset_index(drop=True)
        def delete_data2(row_index):
                    global data2
                    data2 = data2.drop(index=row_index).reset_index(drop=True)
        def delete_data3(row_index):
                    global data3
                    data3 = data3.drop(index=row_index).reset_index(drop=True)
        def delete_data4(row_index):
                    global data4
                    data4 = data4.drop(index=row_index).reset_index(drop=True)
        def delete_data5(row_index):
                    global data5
                    data5 = data5.drop(index=row_index).reset_index(drop=True)

        # Streamlit 앱 생성
        def main():
            password = 970808
            day_password = 1234
            day = 1234
            night_password = 1234
            night = 1234
            st.title('💜아기자기 다락방💙')
            st.write('아기자기의 다락방에 아깅이들을 초대할게!')
            tab1, tab2, tab3 = st.tabs(["Howto", "Product_poster", "Menu"])
            with tab3:
                option_DN = ['낮🌞', '밤🌙', '간부용😎']
                options_DN = st.selectbox("낮과 밤중에 골라줘!", option_DN)
                if options_DN == '낮🌞':
                    st.error('⚠️시간에 맞춰 공개되는 비밀번호를 입력해줘(￣┰￣*)ゞ!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0)
                    if password_input == day_password:
                        st.success('다락방의 낮에 온걸 환영해!( •̀ ω •́ )✧')
                        options = ["🌞물건/포인트보기🔎", "🌞물건구매🎁","🌞구매내역🛒"]
                        option = st.selectbox("기능을 선택해줘!ヾ(≧▽≦*)o", options)
                    # 사용자로부터 이름, 점수, 포인트를 입력받는 UI 구성
                        if option == '🌞물건/포인트보기🔎':
                        # 저장된 데이터프레임 출력
                            if st.button('🌞물건/포인트보기🔎'):
                                st.write('물품 목록이야╰(*°▽°*)╯')
                                st.write('price는 가격, mount는 수량을 의미해!')
                                st.write(data)
                                st.write('다락방 1회차에서 남기고 간 포인트와 이번 다락방에서 새롭게 지급된 포인트 합쳐서 보여줄게!')
                                st.write('ヾ(•ω•`)o')
                                st.write(data2)
                        # 포인트 차감 버튼
                        elif option == '🌞물건구매🎁':
                            st.write('지급된 포인트와 물품 목록은 "물건/포인트보기🔎" 기능을 이용해줘(❁´◡`❁)')
                            # 구매자 이름 입력창
                            name = st.text_input('이름을 입력해줘😀')
                            # 구매하려는 품목 선택창
                            product_name = st.selectbox('구매하려는 품목을 선택해줘(❁´◡`❁)', options=data['Name'].tolist())
                            # 구매 수량 입력창
                            mount = st.number_input('구매 수량을 입력해줘╰(*°▽°*)╯', min_value=1)
                            # 구매 버튼 클릭시 purchase_item 함수 실행
                            if st.button('구매하기'):
                                purchase_item(name, product_name, mount)
                        elif option == '🌞구매내역🛒':
                            if st.button('구매내역 조회'):
                                st.write(data3)
                    else:
                        st.warning('비밀번호가 틀렸습니다')
                elif options_DN == '밤🌙':           
                    st.error('⚠️시간에 맞춰 공개되는 비밀번호를 입력해줘(￣┰￣*)ゞ!⚠️')
                    password_input = st.number_input('비밀번호를 입력해주세요 : ', min_value=0)
                    if password_input == night_password:
                        st.success("다락방의 밤에 찾아와줘서 고마워!ヾ(≧▽≦*)o")
                        options_night = ["🌙물건/포인트보기🔎", "🌙물건구매🎁",'🌙구매내역🛒']
                        option_night = st.selectbox("기능을 선택해줘!ヾ(≧▽≦*)o", options_night)
                        
                        if option_night == '🌙물건/포인트보기🔎':
                        # 저장된 데이터프레임 출력
                            if st.button('🌙물건/포인트보기🔎'):
                                st.write('물품 목록이야╰(*°▽°*)╯')
                                st.write('price는 가격, mount는 수량을 의미해!')
                                st.write(data4)
                                st.write('다락방 1회차에서 남기고 간 포인트와 이번 다락방에서 새롭게 지급된 포인트 합쳐서 보여줄게!')
                                st.write('ヾ(•ω•`)o')
                                st.write(data2)
                        # 포인트 차감 버튼
                        elif option_night == '🌙물건구매🎁':
                            st.write('지급된 포인트와 물품 목록은 "물건/포인트보기🔎" 기능을 이용해줘(❁´◡`❁)')
                            # 구매자 이름 입력창
                            name = st.text_input('이름을 입력해줘😀')
                            # 구매하려는 품목 선택창
                            product_name = st.selectbox('구매하려는 품목을 선택해줘(❁´◡`❁)', options=data4['Name'].tolist())
                            # 구매 수량 입력창
                            mount = st.number_input('구매 수량을 입력해줘╰(*°▽°*)╯', min_value=1)

                            # 구매 버튼 클릭시 purchase_item 함수 실행
                            if st.button('구매하기'):
                                purchase_item2(name, product_name, mount)
                        elif option_night == '🌙구매내역🛒':
                            if st.button('구매내역 조회'):
                                st.write(data5)
                    else :
                        st.warning('비밀번호가 틀렸습니다.')
                elif options_DN == '간부용😎':
                        options_manager = ['데이터추가➕🌞','데이터추가➕🌙','포인트지급📝', "데이터 초기화💣", "데이터삭제✂"]
                        option_manager = st.selectbox("기능을 선택해줘!ヾ(≧▽≦*)o", options_manager)
                        if option_manager == "데이터추가➕🌞":
                            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
                            password_input = st.number_input('비밀번호를 입력해주세요 : ')
                            if password_input == password:
                                st.success('접근을 허용합니다')
                                name = st.text_input('품목명을 입력해줘')
                                price = st.number_input('가격을 입력해줘', min_value=0, max_value=10000)
                                # point = st.number_input('Enter Point', min_value=0, max_value=50)
                                mount = st.number_input('수량을 입력해줘', min_value=0, max_value=100)
                            
                        # 이름, 점수, 포인트가 입력되면 데이터프레임에 추가
                                if st.button('데이터추가'):
                                    # if st.button('추가'):
                                    add_data(name, price, mount)
                                    save_data(data)  # 데이터를 파일에 저장
                                    st.success('품목이 추가되었어!')
                            else:
                                st.warning('비밀번호가 틀렸습니다')
                        elif option_manager == "데이터추가➕🌙":
                            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
                            password_input = st.number_input('비밀번호를 입력해주세요 : ')
                            if password_input == password:
                                st.success('접근을 허용합니다')
                                name = st.text_input('품목명을 입력해줘')
                                price = st.number_input('가격을 입력해줘', min_value=0, max_value=10000)
                                # point = st.number_input('Enter Point', min_value=0, max_value=50)
                                mount = st.number_input('수량을 입력해줘', min_value=0, max_value=100)
                            
                        # 이름, 점수, 포인트가 입력되면 데이터프레임에 추가
                                if st.button('데이터추가'):
                                    # if st.button('추가'):
                                    add_data4(name, price, mount)
                                    save_data4(data4)  # 데이터를 파일에 저장
                                    st.success('품목이 추가되었어!')
                            else:
                                st.warning('비밀번호가 틀렸습니다')
                        elif option_manager == "데이터삭제✂":
                            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
                            password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0)
                            if password_input == password:
                                st.success('접근을 허용합니다')
                                delete_datas = ['품목🌞','품목🌙', '명단', '구매내역🌞', '구매내역🌙']
                                delete_datass = st.selectbox('삭제하려는 데이터를 선택하세요', delete_datas)
                                if delete_datass == '품목🌞':
                                    # 사용자로부터 삭제할 행 번호 입력받기
                                    st.write("품목입니다")
                                    st.write(data)
                                    row_index = st.number_input('삭제하고 싶은 품목의 번호를 입력해주세요', min_value=0, max_value=data.shape[0]-1)
                                    if st.button('품목 삭제'):
                                    # 해당 행이 존재할 경우, 행을 삭제
                                        if row_index >= 0 and row_index < data.shape[0]:
                                            delete_data(row_index)
                                            save_data(data)  # 데이터를 파일에 저장
                                            st.success('입력하신 행이 삭제되었습니다.')
                                elif delete_datass == '품목🌙':
                                    # 사용자로부터 삭제할 행 번호 입력받기
                                    st.write("품목입니다")
                                    st.write(data4)
                                    row_index4 = st.number_input('삭제하고 싶은 품목의 번호를 입력해주세요', min_value=0, max_value=data.shape[0]-1)
                                    if st.button('품목 삭제'):
                                    # 해당 행이 존재할 경우, 행을 삭제
                                        if row_index4 >= 0 and row_index4 < data.shape[0]:
                                            delete_data4(row_index4)
                                            save_data4(data4)  # 데이터를 파일에 저장
                                            st.success('입력하신 행이 삭제되었습니다.')
                                elif delete_datass == '명단':
                                    st.write("포인트입니다")
                                    st.write(data2)
                                    row_index2 = st.number_input('삭제하고 싶은 포인트의 번호를 입력해주세요', min_value=0, max_value=data2.shape[0]-1)
                                    if st.button('포인트 삭제'):
                                        # 해당 행이 존재할 경우, 행을 삭제
                                        if row_index2 >= 0 and row_index2 < data2.shape[0]:
                                            delete_data2(row_index2)
                                            save_data2(data2)  # 데이터를 파일에 저장
                                            st.success('입력하신 행이 삭제되었습니다.')
                                elif delete_datass == '구매내역🌞':
                                    st.write("구매내역🌞 입니다")
                                    st.write(data3)
                                    row_index3 = st.number_input('삭제하고 싶은 구매내역의 번호를 입력해주세요', min_value=0, max_value=data2.shape[0]-1)
                                    if st.button('구매내역🌞 삭제'):
                                        # 해당 행이 존재할 경우, 행을 삭제
                                        if row_index3 >= 0 and row_index3 < data3.shape[0]:
                                            delete_data3(row_index3)
                                            save_data3(data3)  # 데이터를 파일에 저장
                                            st.success('입력하신 행이 삭제되었습니다.')
                                elif delete_datass == '구매내역🌙':
                                    st.write("구매내역🌙 입니다")
                                    st.write(data5)
                                    row_index5 = st.number_input('삭제하고 싶은 구매내역의 번호를 입력해주세요', min_value=0, max_value=data2.shape[0]-1)
                                    if st.button('구매내역🌙 삭제'):
                                        # 해당 행이 존재할 경우, 행을 삭제
                                        if row_index5 >= 0 and row_index5 < data5.shape[0]:
                                            delete_data5(row_index5)
                                            save_data5(data5)  # 데이터를 파일에 저장
                                            st.success('입력하신 행이 삭제되었습니다.')
                            else :
                                st.warning('비밀번호가 틀렸습니다.')
                        elif option_manager == '데이터 초기화💣':
                            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
                            password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0)
                            if password_input == password:
                                st.write('접근을 허용합니다')
                                # 데이터 초기화 버튼
                                st.write('☢아래의 버튼을 누르면 전부 초기화 됩니다!☢')
                                if st.button('데이터 초기화'):
                                    clear_data()
                                    st.warning('데이터가 초기화 되었습니다.')
                            else:
                                st.warning('비밀번호가 틀렸습니다')
                        elif option_manager == '포인트지급📝':
                            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
                            password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0)
                            if password_input == password:
                                st.success('접근을 허용합니다')
                                name = st.text_input('닉네임을 입력해줘')
                                point = st.number_input('포인트를 입력해줘', min_value=0, max_value=1000)
                        # 이름, 점수, 포인트가 입력되면 데이터프레임에 추가
                                if st.button('데이터추가'):
                                    # if st.button('추가'):
                                    add_data2(name, point)
                                    save_data2(data2)  # 데이터를 파일에 저장
                                    st.success('포인트가 지급되었어!')
                            else :
                                st.warning('비밀번호가 틀렸습니다.')
                        
            with tab1:
                st.write()
                '''
                ##### 여기 있는 안내사항을 먼저 읽고 참여해줘!
                ##### 아기자기의 다락방은 아깅이들을 위해 만들었어!
                ##### 잘 이용해줬으면 좋겠어ლ(╹◡╹ლ) 
                ##### 기능을 먼저 알려줄게!
                > * 기능은 각각 ["물건/포인트보기🔎", "물건구매🎁", "구매내역🛒", "데이터추가➕",'포인트지급📝', "데이터 초기화💣",  "데이터삭제✂"] 들이 있어!
                >> 우리 아깅이들은 물건/포인트보기🔎와 물건구매🎁, 구매내역🛒만 이용할 수 있어!
                >> 나머지 기능들은 우리 빵셔틀들만 이용할 수 있으니 이해해줘!
                > * 물건/포인트보기🔎를 누르면 다락방에 있는 물건들과 아깅이들의 포인트를 확인할 수 있어!
                >> 가지고 있는 포인트와 남아있는 물건을 잘 확인해줘(❁´◡`❁)
                > * 물건구매🎁를 누르면 다락방에 있는 물건을 아깅이가 가지고 있는 포인트로 가져갈 수 있어
                >> 구매 방법은 아래와 같아!
                >>> 1. 구매자인 아깅이의 이름을 정확하게 입력해줘
                >>> 1. 가지고 싶은 물건을 목록에서 골라!
                >>> 1. 가지고 싶은 만큼 수량을 골라줘(❗수량 제한이 있으니 꼭 주의해서 구매해줘❗)
                >>> 1. 구매 버튼을 누르면 물건이 구매내역에 추가되고 포인트가 사용될거야!
                > * 구매내역🛒은 아깅이가 구매한 물건을 볼 수 있어!
                >> 구매한 물건이 맞는지 확인해주고, 혹시나 잘못 되었다면 빵셔틀들에게 꼭 알려줘! 우리가 고쳐줄게!
                > * 품목별 인당 구매 제한을 초과해서 구매하면 구매 기록은 지워질 예정이야! 그럴 땐 우리가 알려줄테니까 다시 구매해줘!
                >> * 구매내역에서 이름이 지워졌어도 너무 놀라지 말아줘(‾◡◝)
                '''
            with tab2:
                options_poster = ["아기자기 다락방🌞", "아기자기 다락방🌙"]
                option_poster = st.selectbox("품목 보기", options_poster)
                if option_poster == '아기자기 다락방🌞':
                    st.error('⚠️시간에 맞춰 공개되는 비밀번호를 입력해줘(￣┰￣*)ゞ!⚠️')
                    password_input_poster = st.number_input('비밀번호를 입력해주세요 : ', min_value=0, key='password_input_poster')

                    if password_input_poster == day:
                        st.success('다락방의 낮을 공개할게!')
                        img_url1='https://github.com/Myun9hyun/trash/raw/main/MH/room/day_new.jpg'
                        img_url2='https://github.com/Myun9hyun/trash/raw/main/MH/room/day_secret_new.jpg'
                        st.image(img_url1)
                        st.image(img_url2)
                    else: 
                        st.warning('비밀번호가 틀린것 같아')
                elif option_poster == '아기자기 다락방🌙':
                    st.error('⚠️시간에 맞춰 공개되는 비밀번호를 입력해줘(￣┰￣*)ゞ!⚠️')
                    password_input_night = st.number_input('비밀번호를 입력해주세요 : ', min_value=0, key='password_input_night')
                    if password_input_night == night:
                        st.success('다락방의 밤을 공개할게!')  
                        img_url1='https://github.com/Myun9hyun/trash/raw/main/MH/room/night_new.jpg'
                        img_url2='https://github.com/Myun9hyun/trash/raw/main/MH/room/night_secret_new.jpg'
                        st.image(img_url1)
                        st.image(img_url2)
                    else: 
                        st.warning('비밀번호가 틀린것 같아')
        
        if __name__ == '__main__':
            main()