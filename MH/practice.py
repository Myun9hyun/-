import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

menu = ["메인페이지", "데이터페이지", "기타"]
choice = st.sidebar.selectbox("메뉴를 선택해주세요", menu)

if choice == "메인페이지":

    tab0, tab1, tab2, tab3 = st.tabs(["🏠 Mainpage", "🔎Explain", "🗃 Data", "🖇️ Link"])
   

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

        | 이름 | 팀장/팀원  | 역할 분담 | 그 외 역할 | 개인GitHub링크 |
        | :---: | :---: | :---: | :---: | :---: |
        | 이규린 | 팀장👑 | 데이터 전처리✏️ | PPT발표💻 |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/whataLIN)|
        | 강성욱 | 팀원🐜  | 데이터 시각화👓 | PPT발표💻 |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/JoySoon)|
        | 김명현 | 팀원🐜 | 데이터 시각화👓 | 발표자료제작📝 |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Myun9hyun)|
        | 김지영 | 팀원🐜  | 데이터 전처리✏️ | 발표자료제작📝 |[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/jyeongvv)|
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
        > 1. ADJ_T : ?
        > 1. WAB : ?
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
    tab0, tab1, tab2 = st.tabs(["🗃 Data", "📈 Chart", "🖇️ Link"])
    data = np.random.randn(10, 1)
    with tab0:
        tab0.subheader("🗃 Data Tab")
        st.write("사용된 전체 csv파일")
        url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/cbb.csv"
        df = pd.read_csv(url)
        st.write(df)

        options = st.selectbox(
                '검색하고 싶은 데이터를 골라주세요',
                ('Index', 'Columns', 'Mix'))
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

        
        elif options == 'Mix':
            column_names = st.text_input('검색하고 싶은 Columns를 입력하세요')
            # 입력한 컬럼명이 존재하는 경우
            if column_names in df.columns:
                # 점수 입력 받기
                score = st.text_input('그 Columns내에 있는 검색하고 싶은 Index를 입력하세요 ')
                # 입력한 점수와 일치하는 행 찾기
                filtered_df = df[(df[column_names] == score)]
                if score.isdigit():
                    score = int(score)
                # 검색 결과 출력하기
                    if not filtered_df.empty:
                        st.write(filtered_df)
                    else:
                        st.write('No rows found.')
            else:
                st.write('Column not found')
     
    with tab1:
        tab1.subheader("📈 Chart Tab")
        tab1.write()
        '''
        ### Stat Info
        * 차트설명
        ---
        '''
        option = st.selectbox(
        '원하는 차트유형을 골라주세요',
        ('Radar', 'Bar', 'Chart'))
        st.write(f'고르신 {option} 차트를 출력하겠습니다: ')

        if option == 'Radar':
            st.write("Radar 차트 유형입니다")
            option = st.selectbox(
            '원하는 차트를 골라주세요',
            ('Radar1', 'Radar2', 'Radar3', 'Radar4'))
            if option == 'Radar1':
                # 데이터 프레임 만들기
                
                fig = go.Figure()

                # 차트 출력
                
                # 데이터 프레임 만들기
                df2 = pd.DataFrame({
                    'TEAM': ['North Carolina', 'Wisconsin', 'Michigan', 'Texas Tech'],
                    # 'DRB': [30, 23.7, 24.9, 28.7],
                    '2P_O': [53.9, 54.8, 54.7, 52.8],
                    '3P_O': [32.7, 36.5, 35.2, 36.5],
                    '2P_D': [44.6, 44.7, 46.8, 41.9],
                    '3P_D': [36.2, 37.5, 33.2, 29.7],

                })

                # Plotly의 Radar Chart를 만들기
                fig = go.Figure()

                colors = ['Red', 'Green', 'Blue', 'Orange', 'Coral']

                for i, row in df2.iterrows():
                    fig.add_trace(go.Scatterpolar(
                        r=[row['2P_O'], row['3P_O'], row['2P_D'], row['3P_D']],
                        theta=['2점 슛 성공률', '3점 슛 성공률', '2점 슛 허용률', '3점 슛 허용률'],
                        fill='toself',
                        name=row['TEAM'],
                        line=dict(color=colors[i], width=5),
                        fillcolor=colors[i],
                        opacity=0.25
                    ))

                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[23, 55]
                        ),
                    ),
                    showlegend=True
                )

                # Streamlit에서 Radar Chart 표시하기
                st.plotly_chart(fig)
            elif option == 'Radar2':
                st.write("차트2입니다")
                
            elif option == 'Radar3':
                st.write("차트3입니다")
                chart_data = pd.DataFrame(
                np.random.randn(30, 3),
                columns=["a", "b", "c"])
                st.bar_chart(chart_data)

            elif option == 'Radar4':
                st.write("차트 아무거나 넣었습니다")
                # 데이터 프레임 만들기
                df = pd.DataFrame({
                    'name': ['Alice', 'Bob', 'Charlie', 'David'],
                    'science': [90, 60, 70, 80],
                    'math': [80, 70, 60, 90],
                    'history': [60, 80, 70, 90]
                })

                # Theta 순서 변경하기
                df = df[['name', 'math', 'science', 'history']]  # Theta 순서를 [math, science, history]로 변경

                # Plotly의 Radar Chart를 만들기
                fig = go.Figure()

                for index, row in df.iterrows():
                    fig.add_trace(go.Scatterpolar(
                        r=[row['math'], row['science'], row['history']],
                        theta=['Math', 'Science', 'History'],  # Theta 순서도 변경
                        fill='none',
                        mode='lines',
                        name=row['name'],
                        line=dict(color='red', width=2)
                    ))

                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 100]
                        ),
                    ),
                    showlegend=True
                )

                # Streamlit에서 Radar Chart 표시하기
                st.plotly_chart(fig)



        elif option == 'Bar':
            st.write("Bar차트 유형입니다")
            option = st.selectbox(
            '원하는 차트를 골라주세요',
            ('Bar1', 'Bar2', 'Bar3'))
            if option == 'Bar1':
                st.write("승률 데이터 입니다")
                url = "https://raw.githubusercontent.com/Myun9hyun/trash/main/MH/cbb_head.csv"
                df = pd.read_csv(url)
                st.dataframe(df)
                win_rate = ((df['W'] / df['G']) * 100)
                win_rate = win_rate.round(2)
                win_rate = win_rate.rename(
                    index={0 : 'North Carolina', 1 :'Wisconsin', 2 : 'Michigan', 3 :'Texas Tech'},
                    # columns={0 : 'Win_rate'}) 
                )
                # win_rate = win_rate.rename(columns={0 : 'Win_rate'}) 
                win_rate.columns = ['Win_rate']
                win_rate_t = win_rate.T
                st.dataframe(win_rate_t)
                fig = px.bar(win_rate_t)
                
                fig.update_xaxes(title='TEAM')
                fig.update_yaxes(title='Win')

                fig.update_layout(
                    width=600,
                    height=400,
                )

                # y축 범위 수정
                fig.update_yaxes(
                    range=[70, 95]
                )
                st.plotly_chart(fig)
            elif option == 'Bar2':
                st.write("막대 차트 2입니다")
            elif option == 'Bar3':
                st.write("막대 차트 3입니다")
        elif option == 'Chart':
            st.write("차트입니다")
            option = st.selectbox(
            '원하는 차트를 골라주세요',
            ('Chart1', 'Chart2', 'Chart3'))
            if option == 'Chart1':
                st.write("차트1입니다")
            elif option == 'Chart2':
                st.write("차트2입니다")
            elif option == 'Chart3':
                st.write("차트3입니다") 
   
    with tab2:
        tab2.subheader("🖇️ Link Tab")
        
