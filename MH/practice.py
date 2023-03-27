import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib

menu = ["메인페이지", "데이터페이지", "기타"]
choice = st.sidebar.selectbox("메뉴를 선택해주세요", menu)

if choice == "메인페이지":

    tab0, tab1, tab2, tab3 = st.tabs(["🏠 Main", "🔎Explain", "🗃 Data", "🖇️ Link"])
   

    with tab0:
        tab0.subheader("🏀스포츠 Too Too🏀")
        st.write()
        '''
        **⬆️위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다!⬆️**
        '''
        st.image("https://cdn.pixabay.com/photo/2020/09/02/04/06/man-5537262_960_720.png", width=700)
        '''
        ---

        ### Team 💪

        | 이름 | 팀장/팀원  | 역할 분담 | 그 외 역할 | 머신러닝모델링 | GitHub |
        | :---: | :---: | :---: | :---: | :---: | :---: |
        | 이규린 | 팀장👑 | 데이터 전처리✏️ | PPT발표💻 | 랜덤포레스트 |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/whataLIN)|
        | 강성욱 | 팀원🐜  | 데이터 시각화👓 | PPT발표💻 | XG Boost |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/JoySoon)|
        | 김명현 | 팀원🐜 | 데이터 시각화👓 | 발표자료제작📝 | 선형회귀 |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Myun9hyun)|
        | 김지영 | 팀원🐜  | 데이터 전처리✏️ | 발표자료제작📝 | 결정트리 |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/jyeongvv)|
        ---
        
        '''
    with tab1:
        tab1.subheader("🔎Explain")
        tab1.write()
        '''
        ---
        ### 자료 설명
        > * '13~'21년 동안의 미국 대학 농구 데이터를 사용하여 각 팀마다의 승률을 계산하고 예측하는 모듈을 만든다.  
        > * 추가적으로 각 팀의 세부 스탯이 승률에 어떤 영향을 미치는 지도 알아본다.
        ---
        ### Chart & Data List 📝
        > * 넣어둔 데이터 & 차트
        >> * CSV 파일 전체
        >> * CSV 데이터프레임 Index 혹은 Columns 검색 상자
        > * 차트
        >> * 레이더 차트(스탯)
        >> * 바차트
        ---
        '''
    with tab2:
        tab2.subheader("🗃 Data Tab")
        st.write("다음은 CSV 데이터의 일부입니다.")
        # GitHub URL
        url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/cbb_head.csv"

        # CSV 파일 읽기
        try:
            df = pd.read_csv(url)
        except pd.errors.EmptyDataError:
            st.error("CSV 파일을 찾을 수 없습니다.")
            st.stop()
        # DataFrame 출력
        st.write(df)
        tab2.write()
        '''
        ###### 각 Columns의 설명입니다.
        > 1. TEAM : 참여하는 학교의 이름
        > 1. CONF : 소속 지역
        > 1. G : 게임수
        > 1. W : 승리한 게임수
        > 1. ADJOE : 조정된 공격 효율성(평균 디비전 I 방어에 대해 팀이 가질 공격 효율성(점유율당 득점)의 추정치)
        > 1. ADJDE : 수정된 방어 효율성(평균 디비전 I 공격에 대해 팀이 가질 방어 효율성(점유율당 실점)의 추정치)
        > 1. BARTHAG : 전력 등급(평균 디비전 I 팀을 이길 가능성)
        > 1. EFG_O : 유효슛 비율
        > 1. EFG_D : 유효슛 허용 비율
        > 1. TOR : 턴오버 비율(흐름 끊은 비율)
        > 1. TORD : 턴오버 허용 비율(흐름 끊긴 비율)
        > 1. ORB : 리바운드 차지 횟수
        > 1. DRB : 리바운드 허용 횟수
        > 1. FTR : 자유투 비율
        > 1. FTRD : 자유투 허용 비율
        > 1. 2P_O : 2점 슛 성공 비율
        > 1. 2P_D : 2점 슛 허용 비율
        > 1. 3P_O : 3점 슛 성공 비율
        > 1. 3P_D : 3점 슛 허용 비율
        > 1. ADJ_T : 조정된 템포(팀이 평균 디비전 I 템포로 플레이하려는 팀을 상대로 가질 템포(40분당 점유)의 추정치)
        > 1. WAB : "Wins Above Bubble"은 NCAA 농구 대회의 예선 라운드에 참가하는 팀을 결정하는 데 사용되는 "버블"(일정 선) 기준에서 얼마나 높은 승리를 거두었는지를 나타내는 지표입니다.
        > 1. POSTSEASON : 팀이 시즌을 마무리한 등수
        > 1. SEED : NCAA 토너먼트에 참가하는 시드(등수)
        > 1. YEAR : 시즌
        '''

    with tab3:
        tab3.subheader("🖇️ Link Tab")
        tab3.write("추가적인 자료는 아래의 링크에서 확인 하시면 됩니다.")
        st.write()
        '''
        * Kaggle 데이터 출처
        * College Basketball Dataset
        > [![Colab](https://img.shields.io/badge/kaggle-College%20Basketball%20Dataset-skyblue)](https://www.kaggle.com/datasets/andrewsundberg/college-basketball-dataset)
        
        * colab링크1[제목]
        > [![Colab](https://img.shields.io/badge/colab-Data%20preprocessing-yellow)](https://colab.research.google.com/drive/1qTboYP4Pa73isvE4Lt3l5XYLaIhX9Tix?usp=sharing) 
        '''

elif choice == "데이터페이지":
    tab0, tab1, tab2, tab3 = st.tabs(["🗃 Data", "📈 Chart", "🦾 Machine Learning" ,"Streamlit 진행상태.."])
    data = np.random.randn(10, 1)
    with tab0:
        tab0.subheader("🗃 Data Tab")
        st.write("사용된 전체 csv파일")
        url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/cbb.csv"
        df = pd.read_csv(url)
        st.write(df)

        options = st.selectbox(
                '검색하고 싶은 데이터를 골라주세요',
                ('Index', 'Columns', 'Index_in_Column'))
        if options == 'Index':
            index_name = st.text_input('검색하고 싶은 index를 입력해 주세요')
            filtered_df = df[df.apply(lambda row: index_name.lower() in row.astype(str).str.lower().values.tolist(), axis=1)]
            st.write(filtered_df)


        elif options == 'Columns':
            column_name = st.text_input('검색하고 싶은 columns를 입력해 주세요')
            if column_name in df.columns:
                filtered_df = df[[column_name]]
                st.write(filtered_df)
            else:
                st.write('Column이 입력되지 않았습니다.')

        
        elif options == 'Index_in_Column':
            column_names = st.text_input('검색하고 싶은 Columns를 입력하세요')
            # 입력한 컬럼명이 존재하는 경우
            if column_names in df.columns:
                c_index = st.text_input('그 Columns내에 있는 검색하고 싶은 Index를 입력하세요 ')
                # 입력한 점수와 일치하는 행 찾기
                if c_index.isdigit():
                    c_index = int(c_index)
                    filtered_df = df[(df[column_names] == c_index)]
                # 검색 결과 출력하기
                    if not filtered_df.empty:
                        st.write(filtered_df)
                    else:
                        st.write('검색된 Index가 없습니다.')
                else:
                    filtered_df = df[(df[column_names] == c_index)]
                    st.write(filtered_df)
            else:
                st.write('검색된 Columns가 없습니다.')
     
    with tab1:
        tab1.subheader("📈 Chart Tab")
        st.write()
        '''
        ### Stat Info
        '''
        option = st.selectbox(
        '원하는 차트를 골라주세요',
        ('스탯비교 그래프', '승률데이터 그래프', 'Chart'))
        st.write(f'고르신 {option}를 출력하겠습니다: ')

        if option == '스탯비교 그래프':
            # CSV 파일이 업로드되었는지 확인
            url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/cbb.csv"
            df = pd.read_csv(url)

            # 선택한 컬럼명으로 데이터프레임 필터링
            conf_val = st.selectbox("원하는 지역을 골라주세요", options=df['CONF'].unique())
        
            year_list = df['YEAR'].unique().tolist()
            year_list.sort(reverse=False) # 오름차순 정렬
            year_val = st.selectbox("원하는 시즌을 골라주세요", options=year_list)
            filtered_df = df[(df['CONF'] == conf_val) & (df['YEAR'] == year_val)]


            # TEAM의 컬럼명으로 데이터프레임 필터링하여 radar chart 출력
            team_col = "TEAM"
            team_vals = st.multiselect("비교하고 싶은 Team을 골라주세요", options=filtered_df[team_col].unique())
            stats = st.multiselect('Radar chart로 나타내고 싶은 스탯을 골라주세요:', filtered_df.columns.tolist())

            # make_subplots로 1x1 subplot 만들기
            fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'polar'}]])

            # 선택한 각 team별로 trace 추가하기
            for team_val in team_vals:
                team_df = filtered_df[filtered_df[team_col] == team_val]
                theta = stats + [stats[0]]
                fig.add_trace(go.Scatterpolar(
                    r=team_df[stats].values.tolist()[0] + [team_df[stats].values.tolist()[0][0]],
                    theta=theta,
                    fill='toself',
                    name=team_val
                ), row=1, col=1)

            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 70])))
            st.plotly_chart(fig)

        elif option == '승률데이터 그래프':
            st.write("승률 데이터 계산입니다")
            url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/Basketball_processing.csv"
            df = pd.read_csv(url)
            df = df.iloc[:, 1:]
            unique_CONF = df['CONF'].unique()
            
            # 각 고유값에 해당하는 인덱스 추출하여 딕셔너리에 저장
            index_dict = {}
            for CONF in unique_CONF:
                index_dict[CONF] = df[df['CONF'] == CONF].index.tolist()
            
            # 사용자로부터 지역 입력 받기
            user_CONF = st.selectbox("원하시는 지역을 골라주세요:", unique_CONF)
            
            # 선택한 지역에 해당하는 모든 행 출력
            if user_CONF in unique_CONF:
                indices = index_dict[user_CONF]
                sub_df = df.loc[indices]
                st.write(f"### 해당 지역 '{user_CONF}'에 소속된 팀들의 데이터입니다. ")
                st.write(sub_df)
                
                # 사용자로부터 시즌 입력 받기
                # user_YEAR = st.selectbox("원하시는 시즌을 골라주세요:", [''] + sub_df['YEAR'].unique().tolist())
                unique_years = sub_df['YEAR'].unique().tolist()
                sorted_years = sorted(unique_years, reverse=False) # 오름차순 정렬
                user_YEAR = st.selectbox("원하시는 시즌을 골라주세요:", [''] + sorted_years)

                # 선택한 시즌에 해당하는 행 출력
                if user_YEAR != "":
                    sub_df = sub_df[sub_df['YEAR'] == int(user_YEAR)]
                    st.write(f"### 해당 '{user_CONF}' 지역에 소속된 팀 {user_YEAR} 시즌의 데이터입니다. ")
                    st.write(sub_df)
                    # 승률 계산
                    df_winrate = (sub_df['W'] / sub_df['G']) * 100
                    # 계산한 승률을 소수점 아래 2자리까지 표현
                    df_winrate_round = df_winrate.round(2)
                    sub_df_Team = sub_df[['TEAM']]
                    result = pd.concat([sub_df_Team, df_winrate_round], axis=1)
                    df_result = result.rename(columns={0: 'win_rate'})
                    df_result.reset_index(drop=True, inplace=True)
                    # st.write(df_result)
                    df_long = pd.melt(df_result, id_vars=['TEAM'], value_vars=['win_rate'])
                    fig = px.bar(df_long, x='TEAM', y='value', color='TEAM')
                    st.write(f"'{user_CONF}' 지역에 소속된 팀들의 {user_YEAR} 시즌의 승률 그래프입니다. ")
                    st.plotly_chart(fig)
            else:
                st.warning("다시 골라주세요.")

        elif option == 'Chart':
            st.write("승률 데이터 계산입니다")
    with tab2:
        tab2.subheader("🦾 Machine Learning")
        st.write("머신러닝 모델입니다")
        option = st.selectbox(
        '원하는 차트를 골라주세요',
        ('Chart1', 'Chart2', 'Chart3'))
        if option == 'Chart1':
            # 모델 불러오기
           # 랜덤 포레스트 모델 불러오기
            model_path = "MH/LRmodel.pkl"
            model = joblib.load(model_path)

            st.write("LinearRegressor")
            # 첫번째 행
            r1_col1, r1_col2 = st.columns(2)
            경기수 = r1_col1.slider("경기수", 0, 40)
            승리수 = r1_col2.slider("승리수", 0, 40)

            predict_button = st.button("예측")

            if predict_button:
                    variable1 = np.array([승리수, 경기수]*28)
                    model1 = joblib.load('MH/LRmodel.pkl')
                    pred1 = model1.predict([variable1])
                    pred1 = pred1.round(2)
                    st.metric("결과: ", pred1[0])
        elif option == 'Chart2':

            # 랜덤 포레스트 모델 불러오기
            model_path = "MH/RFmodel.pkl"
            model = joblib.load(model_path)

            # Streamlit 앱 설정
            st.title('Random Forest Model')
            st.write('입력 변수')

            # 입력 변수를 위한 슬라이더 추가
            x1 = st.slider('X1', 0.0, 1.0, 0.5, 0.01)
            x2 = st.slider('X2', 0.0, 1.0, 0.5, 0.01)
            x3 = st.slider('X3', 0.0, 1.0, 0.5, 0.01)
            x4 = st.slider('X4', 0.0, 1.0, 0.5, 0.01)

            # 모델을 사용하여 예측 수행
            x = np.array([x1, x2, x3, x4] * 19 + [x4]).reshape(1, -1)

            y = model.predict(x)[0]

            # 예측 결과 출력
            st.subheader('예측 결과')
            st.write('Y:', y)

        elif option == 'Chart3':

            # 결정트리 모델 불러오기
            model_path = "MH/DecisionTree.pkl"
            model = joblib.load(model_path)

            # Streamlit 앱 설정
            st.title('결정트리 모델')
            st.write('입력 변수')

            # 입력 변수를 위한 슬라이더 추가
            x1 = st.slider('X1', 0.0, 10.0, 0.5, 0.01)
            x2 = st.slider('X2', 0.0, 1.0, 0.5, 0.01)

            # 모델을 사용하여 예측 수행
            # x = np.array([x1 * 77], [x2]).reshape(1, -1)
            x = np.array([x1, x2] *38 + [x1]).reshape(1, -1)  # 입력값의 차원을 맞춰줍니다.

            y = model.predict(x)
            y = y[0]

            # 예측 결과 출력
            st.subheader('예측 결과')
            st.write('Y:', round(y, 2))

    with tab3:
        tab3.subheader("Streamlit 진행상태..")
        st.write()
        '''
        ### 현재 진행상태
        > * 메인페이지 구현완료.
        > * 데이터 페이지 내 data tab 데이터 검색 기능 추가..
        > * 데이터 페이지-Bar차트-지역/시즌에 따른 팀들의 승률 데이터 추가
        > * ...

        ### 추가해야 할 기능
        > * 머신러닝 모델링 구형
        > * 팀들의 스탯 별 레이더차트 비교

        '''
