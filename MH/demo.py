import streamlit as st
import pandas as pd
import os
from PIL import Image
import requests
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import joblib
import xgboost as xgb
import seaborn as sns
from streamlit_option_menu import option_menu

password1 = "창설이벤트"
answer1 = "아기자기"
password2 = "아깅이"
answer2 = "뱌닢"
password3 = "반디"
answer3 = "릎샴"
password4 = "금손"
answer4 = "둥둥향"
password5 = "둥둥"
answer5 = "1"
password6 = "커피"
answer6 = ""

with st.sidebar:
    choice = option_menu("Menu", ["메인페이지", "퀴즈", "아깅이소리함", "아카이브", "이것저것"],
                         icons=['house', 'bi bi-emoji-smile', 'bi bi-robot', 'bi bi-palette'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

st.write("창설이벤트에 참가해줘서 고마워!")

# ----------------------------------------------------------------------------------------------------------
# 1번
quiz1_password = st.text_input("1번 문제 오픈을 위한 비밀번호를 입력해주세요!",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("우리 길드의 이름은 뭘까?(⊙_⊙)？")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1 == answer1:
            st.balloons()
            st.success("정답입니다!")
            st.write("우리 길드와 함께해줘서 고마워 ╰(*°▽°*)╯")
            st.write("2번 문제 오픈을 위한 비밀번호는 '아깅이' 입니다")
        else:
            st.warning("다시 한 번 생각해봐!")
    if st.button("힌트 보기", key="check_hint_button1"):
            st.write("이건 힌트를 줄 수가 없어! 잘 생각해 봐")
elif quiz1_password != "" and quiz1_password != password1:
    st.error("비밀번호가 틀렸어!")

# ----------------------------------------------------------------------------------------------------------
# 2번
quiz2_password = st.text_input("2번 문제 오픈을 위한 비밀번호를 입력해주세요!")
if quiz2_password == password2:
    quiz2 = st.text_input("아기자기 길드의 길드마스터로, 디코에 자주 출몰하는 간부의 이름은?")
    if st.button("정답 확인"):
        if quiz2 == answer2:
            st.balloons()
            st.success("정답입니다!")
            # st.image("메지지 이미지 넣기")
            st.write("[뱌닢]은 우리 길드의 길드마스터야!")
            st.write("[뱌닢]은 길드를 위해 누구보다 열심히 일해😊")
            st.write("[뱌닢]은 매번 위클리 이벤트로 분배된 코젬을 나누는 역할을 하고있어!")
            st.write("[뱌닢]은 길드 노블 공지, 길드 컨텐츠 미이행자 공지, 길드 이벤트 공지등의 역할도 하고 있어!")
            st.write("[뱌닢]은 길드 개편을 위해 많은 노력을 했어!")
            st.write("3번 문제 오픈을 위한 비밀번호는 '반디' 야!")
        else :
            st.warning("다시 한 번 생각해봐!")
    if st.button("힌트 보기"):
        st.write("이 사람의 예전 직업은 '제로'였어!")
        st.write("이 사람의 예전 본캐의 닉네임은 '반디풀잎' 이야!")
elif quiz2_password != "" and quiz2_password != password2:
    st.error("비밀번호가 틀렸어!")

# ----------------------------------------------------------------------------------------------------------
# 3번
quiz3_password = st.text_input("3번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz3_password3")
if quiz3_password == password3:
    quiz3 = st.text_input("이번 메이플 팬페스트 금손 부스에 참석한 간부는 누구일까?")
    if st.button("정답 확인", key= "check_answer_button3"):
        if quiz3 == answer3:
            st.balloons()
            st.success("정답입니다!")
            # st.image("메지지 이미지 넣기")
            st.write("[릎샴]은 이번 팬페스트에 '볼빵빵하우스'라는 부스 담당자로 참석했어!")
            st.write("[릎샴]은 길드에서 포스터, 길드규정문 등을 만드는 디자인 역할을 하고 있어!")
            st.write("[릎샴]은 이번 창설이벤트 경품으로 제공되는 물품도 만들었어!")
            st.write("4번 문제 오픈을 위한 비밀번호는 '금손' 이야!")
        else : 
            st.warning("다시 한 번 생각해봐!")
    if st.button("힌트 보기", key = "check_hint_button3"):
        st.write("캡틴 김수호와 직업이 같은 사람을 생각해봐!")
        st.write("이 사람은 '이달의 아깅이' 이벤트에서 키링 이미지 제작도 해주고 있어!")
elif quiz3_password != "" and quiz3_password != password3:
    st.error("비밀번호가 틀렸어!")

# ----------------------------------------------------------------------------------------------------------
# 4번
quiz4_password = st.text_input("4번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz4_password")
if quiz4_password == password4:
    quiz4 = st.text_input("이 페이지 누가 만들었을까?")
    if st.button("정답 확인", key="check_answer_button4"):
        if quiz4 == answer4:
            st.balloons()
            st.success("정답입니다!")
            # st.image("메지지 프로필 넣기")
            st.write("[둥둥향]은 하찮은 컴퓨터 실력으로 페이지 만드는 역할을 맡고 있어!")
            st.write("[둥둥향]은 공지방에서 이벤트 정리글을 공유하는 역할을 하고 있어!")
            st.write("[둥둥향]은 공지글의 멘트를 작성하는 역할을 하고 있어!")
            st.write("5번 문제 오픈을 위한 비밀번호는 '둥둥'이야!")
        else :
            st.error("다시 한번 생각해봐!")
    if st.button("힌트 보기", key = "check_hint_button4"):
        st.write("이 사람의 직업은 캐논마스터야!")
        st.write("이 사람은 공지방에서 이벤트 알림이 역할을 하고 있어!")
elif quiz4_password != "" and quiz4_password != password4:
    st.error("비밀번호가 틀렸어!")

# ----------------------------------------------------------------------------------------------------------
# 5번
quiz5_password = st.text_input("5번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz5_password")
if quiz5_password == password5:
    quiz5 = st.text_input("문제를 읽고, 아래의 보기에서 정답을 '숫자'로 입력해줘!")
    st.write("나는 공지방에서 썬데이 메이플 공지를 하고 있습니다!")
    st.write("나의 직업은 '영웅' 직업군입니다")
    st.write("나는 누구 일까요?")
    st.write("---")
    st.write("1. 돌체라페")
    st.write("2. 카페라떼")
    st.write("3. 콤퓨타")
    st.write("4. 턴테이블")
    st.write("5. 퀸메아")
    if st.button("정답 확인", key = "check_answer_button5"):
        if quiz5 == answer5:
            st.balloons()
            st.success("정답입니다!")
            st.write("[돌체라페]는 간부진 막내로서 다른 간부들을 위해 열심히 도와주고 있어!")
            st.write("[돌체라페]는 매주 금요일 10시 썬데이메이플 내용을 공지방에 공유해주고 있어")
            st.write("[돌체라페]는 매주 일요일 길드 컨텐츠 이행여부를 확인하고, 직위 상승/하락을 확인하고 있어")
            st.write("[돌체라페]는 간부진들 중 막내야!")
            st.write("6번 문제 오픈을 위한 비밀번호는 '커피'야!")
        else  :
            st.warning("다시 한 번 생각해봐!")
    if st.button("힌트 보기", key = "check_hint_button5"):
        st.write("나는 연유가 들어간 커피야!")
elif quiz5_password != "" and quiz5_password != password5:
    st.error("비밀번호가 틀렸어!")

# ----------------------------------------------------------------------------------------------------------
# 6번
quiz6_password = st.text_input("6번 문제 오픈을 위한 비밀번호를 입력해주세요!", key = "quiz6_password")
if quiz6_password == password6:
    quiz6 = st.text_input("")





st.header("간부진들에게 하고싶은 말을 남겨주세요")
FILE_PATH10 = 'data10.csv'
options = ["의견 남기기➕", "내용 조회🔎", "내용 삭제✂", "초기화💣" ]
option = st.selectbox("기능 선택", options, key='select3')
# 파일에서 데이터 불러오기
def load_data10():
    try: 
        data10 = pd.read_csv(FILE_PATH10)
    except FileNotFoundError:
        data10 = pd.DataFrame(columns=['Name', 'Comment', 'Day'])
    return data10

# 데이터를 파일에 저장하기
def save_data10(data10):
    data10.to_csv(FILE_PATH10, index=False)

# 데이터 초기화 함수
def clear_data10():
    global data10
    data10 = pd.DataFrame(columns=['Name', 'Comment', 'Day'])
    # 파일 삭제
    os.remove(FILE_PATH10)

# 데이터 삭제 함수
def delete_data10(row_index):
    global data10
    data10 = data10.drop(index=row_index).reset_index(drop=True)

# 불러온 데이터를 전역 변수로 저장
data10 = load_data10()
def add_data10(name, comment, day):
    global data10
    new_data10 = pd.DataFrame({'Name': [name], 'Comment': [comment], 'Day': [day]})
    data10 = pd.concat([data10, new_data10], ignore_index=True)
def main():
    if option == "내용 삭제✂":
        st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
        password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0, key='pass1')
        if password_input == password:
            st.success('접근을 허용합니다')
            st.write(data10[['Name','Comment', 'Day']])
            row_index = st.number_input('삭제하고 싶은 데이터의 번호를 입력해주세요', min_value=0, max_value=data10.shape[0]-1)
            st.write("Enter를 입력하면 삭제됩니다.")
            if st.button('데이터 삭제'):
                # 해당 행이 존재할 경우, 행을 삭제
                if row_index >= 0 and row_index < data10.shape[0]:
                    delete_data10(row_index)
                    save_data10(data10)  # 데이터를 파일에 저장
                    st.success('입력하신 행이 삭제되었습니다.')
        else:
            st.warning('비밀번호가 틀렸습니다.')
    elif option == "의견 남기기➕":
        name = st.text_input("의견 남기시는 분의 이름을 입력해주세요")
        comment = st.text_input("내용을 적어주세요")
        day = st.date_input(
            "의견 남기는 날짜를 설정해주세요",
            datetime.date.today())
        if st.button('의견 남기기'):
            add_data10(name, comment, day)
            save_data10(data10)
            st.success("감사합니다!!ヾ(•ω•`)o")

    elif option == "내용 조회🔎":
        st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
        password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0,key='pass2')
        if password_input == password:
            st.success('접근을 허용합니다')
            if st.button('내용 확인'):
                st.write("내용입니다.")
                st.write(data10)
        else:
            st.warning('비밀번호가 틀렸습니다.')

    elif option == "초기화💣":
        st.error('⚠️길드 간부진만 접근할 수 있는 메뉴입니다!⚠️')
        password_input = st.number_input('비밀번호를 입력해주세요 : ',min_value=0,key='pass3')
        if password_input == password:
            st.success('접근을 허용합니다')
            # 데이터 전부 삭제
            st.write("⚠️버튼을 누르면 데이터가 다 날아갑니다!⚠️")
            st.write("⚠️신중하게 누르세요!!⚠️")
            if st.button('초기화'):
                clear_data10()
                st.warning('초기화 되었습니다')
        else:
            st.warning('비밀번호가 틀렸습니다.')
if __name__ == "__main__":
    main()