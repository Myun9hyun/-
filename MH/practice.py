import pandas as pd
import streamlit as st
# CSV 파일 불러오기
df = pd.read_csv('products.csv')

# 필요한 열 선택
df = df[['name', 'price', 'stock']]

# 상품 이름으로 정렬
df = df.sort_values(by='name')

# 인덱스 재설정
df = df.reset_index(drop=True)


# 초기 상태 설정
cart = {}

# 제목 출력
st.title('상점 페이지')

# 상품 목록 출력
for i in range(len(df)):
    col1, col2, col3 = st.beta_columns([2, 1, 1])
    name = df.loc[i, 'name']
    price = df.loc[i, 'price']
    stock = df.loc[i, 'stock']
    quantity = 1
    with col1:
        st.write(name)
    with col2:
        st.write(price)
    with col3:
        if stock == 0:
            st.write('품절')
        else:
            quantity = st.number_input('수량', min_value=1, max_value=stock, value=1)
    if quantity > 0:
        if st.button('장바구니에 추가', key=name):
            if name in cart:
                cart[name] += quantity
            else:
                cart[name] = quantity
            st.success(f'{name} {quantity}개를 장바구니에 추가했습니다.')

# 장바구니 출력
if cart:
    st.write('## 장바구니')
    for name, quantity in cart.items():
        st.write(f'{name}: {quantity}개')
else:
    st.write('장바구니에 상품이 없습니다.')
