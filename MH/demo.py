import streamlit as st

# 초기 상품 수량
product_quantity = 10

# a와 b의 현재 상품 수량
a_product_quantity = 0
b_product_quantity = 0

# a와 b의 이름과 현재 상품 수량을 표시하는 함수
def display_user_info(name, product_quantity):
    st.write(f"{name}님의 현재 상품 수량: {product_quantity}")

# a와 b의 상품 구매를 처리하는 함수
def handle_purchase(name, purchase_quantity):
    global product_quantity, a_product_quantity, b_product_quantity
    if product_quantity >= purchase_quantity:
        product_quantity -= purchase_quantity
        if name == "a":
            a_product_quantity += purchase_quantity
        elif name == "b":
            b_product_quantity += purchase_quantity
    else:
        st.write("상품 수량이 부족합니다.")

# Streamlit 애플리케이션을 구성하는 코드
st.title("상점 애플리케이션")

# a와 b의 이름과 현재 상품 수량을 표시
display_user_info("a", a_product_quantity)
display_user_info("b", b_product_quantity)

# 구매 양 입력 받기
purchase_quantity = st.number_input("구매할 상품 수량을 입력하세요.", min_value=0)

# 구매 버튼 누르면 처리
if st.button("구매"):
    handle_purchase("a", purchase_quantity)
    display_user_info("a", a_product_quantity)
    
# b가 보는 현재 상품 수량 표시
display_user_info("b", product_quantity)
