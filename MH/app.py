import streamlit as st
import sqlite3
import pandas as pd
import csv

# 페이지 넓이 설정
st.set_page_config(page_title='온라인 상점', page_icon=':shopping_bags:', layout='wide')

# 사이드바 설정
st.sidebar.title('메뉴')
selected_menu = st.sidebar.radio('', ['상품 구매', '장바구니', '주문 내역'])

# 데이터베이스 연결
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# 테이블 생성
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    quantity INTEGER
)
""")

# csv 파일에서 데이터 가져오기
with open('MH/products.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        cur.execute(f"INSERT INTO products VALUES ({row[0]}, '{row[1]}', {row[2]}, {row[3]})")

# 커밋
conn.commit()

# 테이블 조회 함수
def select_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return products

# 테이블 업데이트 함수
def update_product_quantity(id, quantity):
    if quantity <= 0:
        quantity = 0
        cur.execute("UPDATE products SET quantity = ?, status = '품절' WHERE id = ?", (quantity, id))
    else:
        cur.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, id))
    conn.commit()

# 상품 정보 표시
def display_product_info(product, session):
    col1, col2, col3, col4, col5 = st.beta_columns([1, 1, 1, 0.5, 1])
    with col1:
        st.write(product[0])
    with col2:
        st.write(product[1])
    with col3:
        st.write(product[2])
    with col4:
        if product[3] == 0:
            st.write('품절')
        else:
            quantity = st.number_input('수량', value=1, min_value=1, max_value=product[3])
            st.write(f'남은 수량: {product[3]-quantity}')
    with col5:
        if product[3] == 0:
            st.write('품절')
        else:
            if st.button(f'구매 ({product[1]})', key=f'buy_{product[0]}'):
