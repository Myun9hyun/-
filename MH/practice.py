import pandas as pd
import streamlit as st

# 데이터프레임1: 품목, 수량, 가격
df1 = pd.DataFrame({
    '품목': ['사과', '바나나', '오렌지'],
    '수량': [10, 5, 8],
    '가격': [1000, 1500, 800]
})

# 데이터프레임2: 이름, 포인트
df2 = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '포인트': [10000, 5000, 8000]
})

# 구매 함수
def purchase(name, item, quantity):
    # 데이터프레임1에서 해당 품목의 수량을 가져옴
    stock = df1.loc[df1['품목'] == item, '수량'].values[0]
    # 구매하려는 수량이 재고보다 많으면 구매 실패 메시지 출력
    if stock < quantity:
        st.write('재고가 부족합니다.')
        return
    # 데이터프레임1에서 해당 품목의 가격을 가져옴
    price = df1.loc[df1['품목'] == item, '가격'].values[0]
    # 데이터프레임2에서 해당 이름의 포인트를 가져옴
    points = df2.loc[df2['이름'] == name, '포인트'].values[0]
    # 구매하려는 가격이 보유한 포인트보다 많으면 구매 실패 메시지 출력
    if price * quantity > points:
        st.write('포인트가 부족합니다.')
        return
    # 구매 완료 메시지 출력
    st.write('구매가 완료되었습니다.')
    # 데이터프레임1에서 해당 품목의 수량을 구매한 수량만큼 감소시킴
    df1.loc[df1['품목'] == item, '수량'] -= quantity
    # 데이터프레임2에서 해당 이름의 포인트를 구매한 가격만큼 차감시킴
    df2.loc[df2['이름'] == name, '포인트'] -= price * quantity

# streamlit 앱
st.title('구매 프로그램')
st.write(df1)
st.write(df2)

# 구매자의 이름 입력
name = st.text_input('이름을 입력하세요:', '')

# 구매할 품목과 수량 입력
item = st.selectbox('구매할 품목을 선택하세요:', df1['품목'].tolist())
quantity = st.number_input('구매할 수량을 입력하세요:', min_value=1, max_value=10, value=1)

# 구매 버
# 구매 버튼
if st.button('구매'):
    if name and item and quantity:
        purchase(name, item, quantity)
    else:
        st.write('모든 항목을 입력하세요.')
