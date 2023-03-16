import streamlit as st
import numpy as np

tab0, tab1, tab2, tab3= st.tabs(["🏠 Homepage", "📈 Chart", "🗃 Data", "🖇️ Link"])
data = np.random.randn(10, 1)

with tab0:
    tab0.subheader("💸2030의 소비트렌드 분석💸")
    st.write()
    '''
    **⬆️위의 탭에 있는 메뉴를 클릭해 선택하신 항목을 볼 수 있습니다!⬆️**
    '''
    st.image("https://cdn.pixabay.com/photo/2018/01/07/20/56/graph-3068300_960_720.jpg", width=400)
    '''
    ---

     ### Team 💪

    | 이름 | 자료 수집 및 추출 | 데이터 시각화 |
    | :---: | :---: | :---: |
    | 서상원 | 각년도의 남녀종목건수에 대한 비율 시간/나이/성별에 대한 plot  | 그래프 시각화 |
    | 김명현 | 년도, 성별(나이포함)에 대한 구매 품목 상위 5개 변화추이 그래프 | Streamlit 작성 |
    | 배진우 | countplot으로 평일/휴일의 상품판매량 대한 그래프  | 그래프 시각화 |
    ---
    ### Chart & Data List 📝
    > * 차트1
    > * 차트2
    > * 그래프1
    > * 그래프2
    ---
   

    '''
with tab1:
    tab1.subheader("📈 Chart Tab")
    tab1.write()
    
    '''
    ---
    ### 차트제목
    * 차트설명
    ---
    '''
    option = st.selectbox(
    '원하는 차트유형을 골라주세요',
    ('Bar', 'Pie', 'Chart3'))
    st.write('고르신 차트를 출력하겠습니다:', option)
    if option == 'Bar':
        st.write("Bar차트 유형입니다")
    elif option == 'Pie':
        st.write("Pie차트 유형입니다")
    elif option == 'Chart3':
        st.write("차트3입니다")    
with tab2:
    tab2.subheader("🗃 Data Tab")
    tab2.write()
    
    '''
    ---
    ### 데이터제목
    * 데이터설명
    ---
    '''
    option = st.selectbox(
    '원하는 데이터를 골라주세요',
    ('Data1', 'Data2', 'Data3'))
    st.write('고르신 데이터를 출력하겠습니다:', option)
    if option == 'Data1':
        st.write("데이터1입니다")
    elif option == 'Data2':
        st.write("데이터2입니다")
    elif option == 'Data3':
        st.write("데이터3입니다")
    
    tab2.write(data)
with tab3:
    tab3.subheader("🖇️ Link Tab")
    tab3.write("추가적인 자료는 Google Colab 링크를 첨부해드립니다!")
    st.write()
    '''
    * colab링크1[제목]
    > [데이터 링크 2](https://www.google.com/)
    * colab링크2[제목]
    > [데이터 링크 2](https://www.google.com/) 
    '''


