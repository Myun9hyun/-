while True:
    name = st.text_input('이름')
    age = st.number_input('나이')
    gender = st.selectbox('성별', ['여성', '남성'])
    
    # "Add Row" 버튼 클릭시 새로운 행 추가
    if st.button('Add Row'):
        new_row = {'이름': name, '나이': age, '성별': gender}
        df = df.append(new_row, ignore_index=True)
        st.write('새로운 데이터가 추가되었습니다.')
        st.dataframe(df)
    
    # "Add More" 버튼 클릭시 새로운 데이터 추가 입력
    if not st.button('Add More'):
        break