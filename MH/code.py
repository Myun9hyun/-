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


with st.sidebar:
    choice = option_menu("Contents", ["메인페이지", "데이터페이지", "시뮬레이션"],
                         icons=['house', 'kanban', 'bi bi-robot'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fafafa"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

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
        ### 자료 설명
        > * '13~'19년 동안의 미국 대학 농구 데이터를 사용하여 각 팀마다의 승률을 계산하고 예측하는 모듈을 만든다. 
        > * 가상의 스탯을 지닌 선수 5명을 추가하고 선택한 지역에 참가했을때 예측 승률에 대해서 알아본다.
        ---
        ### Chart & Data List 📝
        > * Data 목록
        >> * CSV 파일 전체
        >> * CSV 데이터프레임 Index 혹은 Columns 검색 기능
        > * Chart 목록
        >> * 스탯 비교 그래프(Radar)
        >> * 승률 비교 그래프(Bar)
        > * 머신러닝 모듈 목록
        >> * 선형회귀
        >> * Random Forest
        >> * Decision Tree
        >> * XG Boost
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
        
        * colab 전처리 데이터 링크
        > [![Colab](https://img.shields.io/badge/colab-Data%20preprocessing-yellow)](https://colab.research.google.com/drive/1qTboYP4Pa73isvE4Lt3l5XYLaIhX9Tix?usp=sharing) 
        * colab 선형 회귀 모델링 데이터 링크
        > [![Colab](https://img.shields.io/badge/colab-Line%20Regression-yellow)](https://colab.research.google.com/drive/1bK8x_1Cich78Mf_6hdFcPp1U01d4RjMv?usp=sharing) 
        * colab 랜덤 포레스트 모델링 데이터 링크
        > [![Colab](https://img.shields.io/badge/colab-Random%20Forest-yellow)](https://colab.research.google.com/drive/1E5AzXyJoulVY-12rxmJjBphqOwf4kpNF?usp=sharing) 
        * colab 결정트리 모델링 데이터 링크
        > [![Colab](https://img.shields.io/badge/colab-Decision%20Tree-yellow)](https://colab.research.google.com/drive/1l059OKEqqQkLu9N6RVd-KpjHDcHQI7eX?usp=sharing) 
        * colab XG Boost 모델링 데이터 링크
        > [![Colab](https://img.shields.io/badge/colab-XG%20Boost-yellow)](https://colab.research.google.com/drive/1yF3dcXCYfcFHVDmOUq1RO-tDxqtajA22?usp=sharing) 
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
        st.write("머신러닝 모델링 예시입니다")
        option = st.selectbox(
        '원하는 차트를 골라주세요',
        ('LinearRegressor', 'RandomForest', 'DecisionTree', 'XGBoost'))

        if option == 'LinearRegressor':
            
            # 선형회귀 모델 불러오기
            model_path = "MH/LRmodel_drop.pkl"
            model = joblib.load(model_path)
            # 데이터 불러오기
            df = pd.read_csv('MH/cbb_drop.csv')
            X = df.drop('P_V', axis=1) # 독립변수 (관측값, 피쳐)
            G = df['G']
            W = df['W']
            ORB = df['ORB']
            FTR = df['FTR']
            two_O = df['2P_O']
            three_O = df['3P_O']


            # 모델 불러오기
            with open('MH/LRmodel_drop.pkl', 'rb') as f:
                model = joblib.load(f)
            st.write("구현한 선형회귀 모델 그래프입니다.")
            # 예측값 계산
            df['predicted'] = model.predict(X)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            # 산점도 그리기
            sns.set_style('darkgrid')
            plt.figure(figsize=(8, 6))
            plt.title('Linear Regression')
            
            sns.scatterplot(x = 'P_V', y='predicted', data=df)
            st.pyplot()
            st.write("LinearRegressor")
            # 첫번째 행
            col1, col2, col3, col4, col5, col6  = st.columns(6)
            G = col1.slider("경기수", 0, 40)
            W = col2.slider("승리수", 0, 40)
            ORB = col3.slider("리바운드 수치", 0, 50)
            FTR = col4.slider("자유투 수치", 0, 50)
            two_O = col5.slider("2점슛 수치", 0, 50)
            three_O = col6.slider("3점슛 수치", 0, 30)
            


            predict_button = st.button("예측")

            if predict_button:
                    predicted = model.predict(X)
                    variable1 = np.array([G, W, ORB, FTR, two_O, three_O])
                    model1 = joblib.load('MH/LRmodel_drop.pkl')
                    pred1 = model1.predict([variable1])
                    pred1 = pred1.round(4)
                   
                    st.metric("승률 예측 결과: ", pred1[0]*100)

        elif option == 'RandomForest':

            # 랜덤포레스트 모델 불러오기
            model_path = "MH/RFmodel_drop.pkl"
            model = joblib.load(model_path)
            # 데이터 불러오기
            df = pd.read_csv('MH/cbb_drop.csv')
            X = df.drop('P_V', axis=1) # 독립변수 (관측값, 피쳐)
            G = df['G']
            W = df['W']
            ORB = df['ORB']
            FTR = df['FTR']
            two_O = df['2P_O']
            three_O = df['3P_O']


            # 모델 불러오기
            with open('MH/RFmodel_drop.pkl', 'rb') as f:
                model = joblib.load(f)
            st.write("구현한 Random Forest 모델입니다.")               
            # 첫번째 행
            col1, col2, col3, col4, col5, col6  = st.columns(6)
            G = col1.slider("경기수", 0, 40)
            W = col2.slider("승리수", 0, 40)
            ORB = col3.slider("리바운드 수치", 0, 50)
            FTR = col4.slider("자유투 수치", 0, 50)
            two_O = col5.slider("2점슛 수치", 0, 50)
            three_O = col6.slider("3점슛 수치", 0, 30)
            
            predict_button = st.button("예측")

            if predict_button:
                    predicted = model.predict(X)
                    variable1 = np.array([G, W, ORB, FTR, two_O, three_O])
                    model1 = joblib.load('MH/RFmodel_drop.pkl')
                    pred1 = model1.predict([variable1])
                    pred1 = pred1.round(4)
                    st.metric("승률 예측 결과: ", pred1[0]*100)

        elif option == 'DecisionTree':

            # 결정트리 모델 불러오기
            model_path = "MH/DecisionTree_drop.pkl"
            model = joblib.load(model_path)
            # 데이터 불러오기
            df = pd.read_csv('MH/cbb_drop.csv')
            X = df.drop('P_V', axis=1) # 독립변수 (관측값, 피쳐)
            G = df['G']
            W = df['W']
            ORB = df['ORB']
            FTR = df['FTR']
            two_O = df['2P_O']
            three_O = df['3P_O']
            st.write("Decision Tree 상관관계에 따른 히트맵입니다.")
            model = joblib.load("MH/DecisionTree_drop.pkl")

            df = pd.read_csv("MH/cbb_drop.csv")
            y = df.pop("P_V")

            feature_importances = pd.Series(model.feature_importances_, index=df.columns)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            plt.figure(figsize=(12, 10))
            sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
            # sns.heatmap(X.iloc[:, sorted_idx].corr(), cmap='coolwarm', annot=True)

            st.pyplot()

            # 모델 불러오기
            with open('MH/DecisionTree_drop.pkl', 'rb') as f:
                model = joblib.load(f)
            st.write("구현한 Decision Tree 모델 그래프입니다.")
            # 첫번째 행
            col1, col2, col3, col4, col5, col6  = st.columns(6)
            G = col1.slider("경기수", 0, 40)
            W = col2.slider("승리수", 0, 40)
            ORB = col3.slider("리바운드 수치", 0, 50)
            FTR = col4.slider("자유투 수치", 0, 50)
            two_O = col5.slider("2점슛 수치", 0, 50)
            three_O = col6.slider("3점슛 수치", 0, 30)
            
            predict_button = st.button("예측")

            if predict_button:
                    predicted = model.predict(X)
                    variable1 = np.array([G, W, ORB, FTR, two_O, three_O])
                    model1 = joblib.load('MH/DecisionTree_drop.pkl')
                    pred1 = model1.predict([variable1])
                    pred1 = pred1.round(4)
                    st.metric("승률 예측 결과: ", pred1[0]*100)


        elif option == 'XGBoost':

            # xgboost 모델 불러오기
            model_path = "MH/XGBoost5.pkl"
            model = joblib.load(model_path)

            # 데이터 불러오기
            df = pd.read_csv('MH/cbb_drop.csv')
            X = df.drop('P_V', axis=1) # 독립변수 (관측값, 피쳐)
            G = df['G']
            W = df['W']
            ORB = df['ORB']
            FTR = df['FTR']
            two_O = df['2P_O']
            three_O = df['3P_O']

            option = st.selectbox(
            '원하는 시각화 결과값을 골라주세요',
            ('전체', '세부'))

            if option == '전체':

                # 전체
                fig = px.bar(
                    x=df.columns[:-1], 
                    y=model.feature_importances_, 
                    labels={'x': '변수', 'y': '중요도'}
                    )

                fig.update_layout(
                    title="중요 변수 확인(전체)", 
                    xaxis_title="변수", 
                    yaxis_title="중요도", 
                    width=800, 
                    height=600
                    )


            elif option == '세부':
                # 세부
                fig = px.bar(
                    x=df.columns[:-1], 
                    y=model.feature_importances_, 
                    labels={'x': '변수', 'y': '중요도'}
                    )

                fig.update_layout(
                    title="중요 변수 확인(세부)", 
                    xaxis_title="변수", 
                    yaxis_title="중요도", 
                    yaxis_range=[0, 0.0004],
                    width=800, 
                    height=600
                    )

            st.plotly_chart(fig)

            # 모델 불러오기
            # Load the XGBoost model
            with open('MH/XGBoost5.pkl', 'rb') as f:
                model = joblib.load(f)

            # Create sliders for input variables
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            G = col1.slider("경기수", 0, 40)
            W = col2.slider("승리수", 0, 40)
            ORB = col3.slider("리바운드 수치", 0, 50)
            FTR = col4.slider("자유투 수치", 0, 50)
            two_O = col5.slider("2점슛 수치", 0, 50)
            three_O = col6.slider("3점슛 수치", 0, 30)

            # Create a button to trigger the prediction
            predict_button = st.button("예측")

            # When the button is pressed, make the prediction and show the result
            if predict_button:

            # Create a DataFrame of the input variables
                X = pd.DataFrame([[G, W, ORB, FTR, two_O, three_O]], columns=['G', 'W', 'ORB', 'FTR', '2P_O', '3P_O'])
           
                # Load the XGBoost model and make the prediction
                model = joblib.load('MH/XGBoost5.pkl')
                prediction = model.predict(X)[0]
                prediction = round(prediction*100, 2)
                st.metric("승률 예측 결과: ", prediction)

                # 예측 결과를 그래프한 결과
                fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = prediction,
                domain = {'x': [0, 1], 'y': [0, 1]},
                gauge = {'axis': {'range': [0, 100]},
                        'steps' : [{'range': [0, 25], 'color': "lightgray"},
                                {'range': [25, 50], 'color': "gray"},
                                {'range': [50, 75], 'color': "lightgray"},
                                {'range': [75, 100], 'color': "gray"}],
                        'bar': {'color': "black"}}))
    
                # Add title and labels to the chart
                fig.update_layout(title={'text': '승률 예측 결과', 'y':0.95, 'x':0.5},
                            xaxis={'visible': False}, yaxis={'visible': False})
    
                st.plotly_chart(fig)

    with tab3:
        tab3.subheader("Streamlit 진행상태..")
        st.write()
        '''
        ### 현재 진행상태
        > * 메인페이지 구현완료.
        > * 데이터 페이지 내 data tab 데이터 검색 기능 추가..
        > * 데이터 페이지-Bar차트-지역/시즌에 따른 팀들의 승률 데이터 추가
        > * 머신러닝 모델링 시각화
        > * 머신러닝 모델링 선형회귀/결정트리 시각화 그래프 추가
        > * side bar 바꿈

        ### 추가해야 할 기능
        > * 수정 후 이 탭 삭제
        > * 시뮬레이션 기능 추가

        '''

elif choice == "시뮬레이션":

    # tab0, tab1, tab2, tab3 = st.tabs(["첫 번째 선수", "첫 번째 선수", "첫 번째 선수", "첫 번째 선수"])
    # players = []
    
    # with tab1:
    #     tab1.subheader("첫 번째 선수")
    
    # i=1

    # while False:
    #     player={}
    #     player["Shooting"] = st.slider("슈팅", min_value=1, max_value=10, value=1, key=f"shooting_1")
    #     player["Dribbling"] = st.slider("드리블", min_value=1, max_value=10, value=1, key=f"Dribbling_1")
    #     player["Passing"] = st.slider("패스", min_value=1, max_value=10, value=1, key=f"Passing_1")
    #     player["Rebounding"] = st.slider("리바운드", min_value=1, max_value=10, value=1, key=f"Rebounding_1")
    #     player["Defense"] = st.slider("수비", min_value=1, max_value=10, value=1, key=f"Defense_1")
    #     player["Stamina"] = st.slider("스테미나", min_value=1, max_value=10, value=1, key=f"Stamina_1")

    #     total_stats=player["Shooting"]+player["Dribbling"]+player["Passing"]+player["Rebounding"]+player["Defense"]+player["Stamina"]
    #     if total_stats > 40:
    #         st.warning("스텟 총합이 40을 넘을 수 없습니다.")
    #     else:


    # if st.button('저장'):
    #     players.append(player)

    # tabs = st.tabs([f"{i}번째 선수" for i in range(1, 6)])


    cols = st.columns(5)
    
    player_keys = [
        "Shooting", "Dribbling", "Rebounding", 'Defense', "Stamina"
    ]       #"Passing"

    pl=pd.DataFrame(columns=player_keys, index=[f"{p}번째 선수" for p in range(1,6)])
    # for i, t in enumerate(tabs):

    url='https://github.com/whataLIN/sportsTOoTOo/raw/main/cbb.csv'
    df = pd.read_csv(url)
    df.drop(['TEAM', 'YEAR','W','G'],axis=1, inplace=True)

    conf_list=list(df['CONF'].unique())
    team_conf= st.selectbox('참가할 대회를 선택해주세요.', options=conf_list)

    position_list=['센터','파워포워드','포인트가드','슈팅가드', '스몰포워드']

    for i, c in enumerate(cols):
        with c:
            st.write(position_list[i])
            st.slider("슈팅", min_value=1, max_value=10, value=1, key=f"Shooting_{i+1}")
            st.slider("드리블", min_value=1, max_value=10, value=1, key=f"Dribbling_{i+1}")
            # st.slider("패스", min_value=1, max_value=10, value=1, key=f"Passing_{i+1}")
            st.slider("리바운드", min_value=1, max_value=10, value=1, key=f"Rebounding_{i+1}")
            st.slider("수비", min_value=1, max_value=10, value=1, key=f"Defense_{i+1}")
            st.slider("스테미나", min_value=1, max_value=10, value=1, key=f"Stamina_{i+1}")
            state = st.session_state
            player = {
                key: value for key, value in [(k, state[f'{k}_{i+1}']) for k in player_keys]
            }
            
            for p in player_keys:           #i는 플레이어번호. p는 능력치
                stat=state[f"{p}_{i+1}"]
                st.write(f"{p} : {stat}")

            pl.loc[f"{i+1}번째 선수"] = player

    
    tdf = df.drop(['POSTSEASON', 'SEED', 'CONF', 'BARTHAG','WAB'], axis=1).copy()
    # tdf = df.drop(['TEAM', 'YEAR','W','G', 'POSTSEASON', 'SEED', 'CONF', 'BARTHAG','WAB'], axis=1).copy()
    
    fromShooting = tdf[['ADJOE', 'EFG_O', 'FTR', '2P_O', '3P_O']].copy()
    fromDribbling = tdf[['TORD']].copy()
    fromRebounding = tdf[['ORB', 'DRB']].copy()
    fromDefense = tdf[['TOR', 'EFG_D', 'ADJDE', '2P_D', '3P_D', 'FTRD']].copy()
    fromStamina = tdf[['ADJ_T']].copy()

    plusVarlist=['ADJOE', 'EFG_O', 'FTR', '2P_O', '3P_O', 'ORB', 'TOR','ADJ_T']
    minusVarlist=['TORD', 'EFG_D', '2P_D', '3P_D', 'FTRD', 'ADJDE', 'DRB']

    pl_to_per=pd.DataFrame(
        0,
        columns=tdf.columns,
        index=pl.index
    )


    def get_max(df):   #최대값을 구해 딕셔너리로 반환하는 함수
        return {key: int(value) for key, value in df.max().to_dict().items()}

        # ADJOE, ADJDE, EFG_O, EFG_D, TOR, TORD, ORB, DRB, FTR, FTRD, 2P_O, 2P_D, 3P_O, 3P_D, ADJ_T
        # postseason, seed는 missed tornament.

    def percentage_cal(stat_pl, final_df, df, stat):
            #df는 스탯별로 영향을 주는 변수끼리 나눈거
            #stat_pl는 선수들의 스탯 모음
            #finaldf는 결과를 반영할 df
            #stat는 선수 스탯을 어디서 가져올건지

        columnlist=df.columns
        addper=[]
        subper=[]
        max_values = get_max(df)  #df의 각 값의 max값이 딕셔너리로 반환

        for i in columnlist:
            if i in plusVarlist:
                addper.append(i)
            else:
                subper.append(i)
                final_df[i]=max_values[i]/5


        for p in range(5):
            for i in addper:      #df의 컬럼명을 차례로 가져옴
                final_df.loc[f"{p+1}번째 선수", i] += (int(max_values[i])/50) * stat_pl.loc[f"{p+1}번째 선수", stat]

        for p in range(5):
            for i in subper:
                final_df.loc[f"{p+1}번째 선수", i] -= (int(max_values[i]) / 50) * stat_pl.loc[f"{p+1}번째 선수", stat]


    percentage_cal(pl, pl_to_per, df=fromShooting, stat='Shooting')
    percentage_cal(pl, pl_to_per, df=fromDribbling, stat='Dribbling')
    percentage_cal(pl, pl_to_per, df=fromRebounding, stat='Rebounding')
    percentage_cal(pl, pl_to_per, df=fromDefense, stat='Defense')
    percentage_cal(pl, pl_to_per, df=fromStamina, stat='Stamina')
    
    # st.write(pl_to_per)
    teaminfo = pd.DataFrame(
        data=pl_to_per.sum(axis=0).values.reshape(1, 15),
        columns=tdf.columns,
        index=["%"])
    st.write("team info: ", teaminfo)

    df_columns = ['ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', 'TOR', 'TORD', 'ORB',
       'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB',
       'CONF_A10', 'CONF_ACC', 'CONF_AE', 'CONF_ASun', 'CONF_Amer', 'CONF_B10',
       'CONF_B12', 'CONF_BE', 'CONF_BSky', 'CONF_BSth', 'CONF_BW', 'CONF_CAA',
       'CONF_CUSA', 'CONF_GWC', 'CONF_Horz', 'CONF_Ind', 'CONF_Ivy',
       'CONF_MAAC', 'CONF_MAC', 'CONF_MEAC', 'CONF_MVC', 'CONF_MWC',
       'CONF_NEC', 'CONF_OVC', 'CONF_P12', 'CONF_Pat', 'CONF_SB', 'CONF_SC',
       'CONF_SEC', 'CONF_SWAC', 'CONF_Slnd', 'CONF_Sum', 'CONF_WAC',
       'CONF_WCC', 'CONF_ind', 'SEED_1.0', 'SEED_2.0', 'SEED_3.0', 'SEED_4.0',
       'SEED_5.0', 'SEED_6.0', 'SEED_7.0', 'SEED_8.0', 'SEED_9.0', 'SEED_10.0',
       'SEED_11.0', 'SEED_12.0', 'SEED_13.0', 'SEED_14.0', 'SEED_15.0',
       'SEED_16.0', 'SEED_Missed Tournament', 'POSTSEASON_2.0',
       'POSTSEASON_4.0', 'POSTSEASON_8.0', 'POSTSEASON_16.0',
       'POSTSEASON_32.0', 'POSTSEASON_64.0', 'POSTSEASON_68.0']

    df_forms = pd.DataFrame(0, columns=df_columns, index=['%'])
    
    df_forms['SEED_Missed Tournament']=1
    df_forms['POSTSEASON_Missed Tournament']=1
    df_forms[f'SEED_Missed Tournament']=1
    df_forms[f'BARTHAG']=0.5
    df_forms[f'CONF_{team_conf}']=1

    for i in range(17): # 인덱스
        col_name = df_columns[i]
        if col_name=='BARTHAG' or col_name=='WAB': continue

        df_forms[col_name]+=teaminfo[col_name]

    
    # teaminfo = pd.DataFrame(
    #     data=pl_to_per.sum(axis=0).values.reshape(1, 15),
    #     columns=tdf.columns,
    #     index=["%"])

    # teaminfo['CONF']=team_conf
    # teaminfo['BARTHAG']=0.5
    # teaminfo["POSTSEASON"]="Missed Tournament"
    # teaminfo['SEED']='Missed Tournament'
    # teaminfo['WAB']=0

    # teaminfo = teaminfo.reindex(columns=["CONF", 'ADJOE', 'ADJDE', 'BARTHAG', 'EFG_O', 'EFG_D', "TOR", "TORD", 'ORB', 'DRB', 'FTR', 'FTRD', '2P_O', '2P_D', '3P_O', '3P_D', 'ADJ_T', 'WAB', 'POSTSEASON', 'SEED'])

    # st.write(teaminfo)
    # st.write(teaminfo[:], df.iloc[:5])
    # st.write(len(teaminfo.columns), len(df.columns))

    # #전처리 다시
    # df.loc[len(df)] = teaminfo
    # ps={"R68":68,"R64":64,"R32":32,"S16":16,"E8":8,"F4":4,"2ND":2,"Champion":1}
    # df['POSTSEASON'] = df['POSTSEASON'].map(ps)
    # df.fillna({'POSTSEASON':'Missed Tournament'}, inplace = True)
    # df.fillna({'SEED':'Missed Tournament'}, inplace = True)
    # df=pd.get_dummies(df, columns=['CONF','SEED','POSTSEASON'])  
    # df = df.tail(1)

    option = st.selectbox(
    '원하는 차트를 골라주세요',
    ('LinearRegressor', 'RandomForest', 'DecisionTree', 'XGBoost')) #'XGBoost'
    model_path = f"KL/{option}.pkl"
    model = joblib.load(model_path)

    st.write(option)

    predict_button = st.button("예측")

    if predict_button:
        variable = df_forms
        model = joblib.load(f'KL/{option}.pkl')
        # pred = model.predict(variable)
        # pred = np.round(pred, 2)
        pred = (model.predict(variable)*100).round(2)
        if option=='XGBoost': pred=str(pred)[1:5]

        st.metric(f"결과: {pred}%")



    
