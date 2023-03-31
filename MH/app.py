# import streamlit as st
# import sqlite3
# import pandas as pd
# import csv
# # 페이지 넓이 설정
# st.set_page_config(page_title='온라인 상점', page_icon=':shopping_bags:', layout='wide')

# # 데이터베이스 연결
# conn = sqlite3.connect(':memory:')
# cur = conn.cursor()

# # 테이블 생성
# cur.execute("""
# CREATE TABLE IF NOT EXISTS products (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     price INTEGER,
#     quantity INTEGER
# )
# """)

# # csv 파일에서 데이터 가져오기
# with open('MH/products.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         cur.execute(f"INSERT INTO products VALUES ({row[0]}, '{row[1]}', {row[2]}, {row[3]})")

# # 커밋
# conn.commit()


# # 테이블 조회 함수
# def select_products():
#     cur.execute("SELECT * FROM products")
#     products = cur.fetchall()
#     return products

# # 테이블 업데이트 함수
# # def update_product_quantity(id, quantity):
# #     cur.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, id))
# #     conn.commit()

# # # 상품 정보 표시
# # def display_product_info(product):
# #     col1, col2, col3, col4 = st.beta_columns([1, 1, 1, 0.5])
# #     with col1:
# #         st.write(product[0])
# #     with col2:
# #         st.write(product[1])
# #     with col3:
# #         st.write(product[2])
# #         st.write(f"남은 수량: {product[3]}개")  # 수정된 부분
# #     with col4:
# #         if product[3] == 0:
# #             st.write('품절')
# #         else:
# #             quantity = st.number_input('수량', value=1, min_value=1, max_value=product[3], key=f'quantity_{product[0]}')
# #             if st.button(f'구매 ({product[1]})', key=f'buy_{product[0]}'):
# #                 update_product_quantity(product[0], product[3]-quantity)
# #                 st.success(f'{product[1]} {quantity}개 구매 완료')

# # # 메인 함수
# # def main():
# #     # 상품 정보 가져오기
# #     products = select_products()

# #     # 페이지 헤더
# #     st.header('온라인 상점')

# #     # 페이지 내용
# #     for product in products:
# #         display_product_info(product)
# # 테이블 업데이트 함수
# def update_product_quantity(id, quantity):
#     cur.execute("UPDATE products SET quantity = ? WHERE id = ?", (quantity, id))
#     conn.commit()

# # 상품 정보 표시
# def display_product_info(product):
#     col1, col2, col3, col4 = st.beta_columns([1, 1, 1, 0.5])
#     with col1:
#         st.write(product[0])
#     with col2:
#         st.write(product[1])
#     with col3:
#         st.write(product[2])
#         st.write(f"남은 수량: {product[3]}개")
#     with col4:
#         if product[3] == 0:
#             st.write('품절')
#         else:
#             quantity = st.number_input('수량', value=1, min_value=1, max_value=product[3], key=f'quantity_{product[0]}')
#             if st.button(f'구매 ({product[1]})', key=f'buy_{product[0]}'):
#                 update_product_quantity(product[0], product[3]-quantity)
#                 product = (product[0], product[1], product[2], product[3]-quantity)  # 수정된 부분
#                 st.success(f'{product[1]} {quantity}개 구매 완료')
#     return product  # 수정된 부분

# # 메인 함수
# def main():
#     # 상품 정보 가져오기
#     products = select_products()

#     # 페이지 헤더
#     st.header('온라인 상점')

#     # 페이지 내용
#     updated_products = []  # 수정된 부분
#     for product in products:
#         updated_product = display_product_info(product)
#         updated_products.append(updated_product)  # 수정된 부분
#     # 테이블 업데이트
#     for updated_product in updated_products:
#         update_product_quantity(updated_product[0], updated_product[3])



# if __name__ == '__main__':
#     main()
import streamlit as st
import sqlite3
import pandas as pd
import csv

# 페이지 넓이 설정
st.set_page_config(page_title='온라인 상점', page_icon=':shopping_bags:', layout='wide')

# 데이터베이스 연결
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# 테이블 생성
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    stock INTEGER
)
""")
# csv 파일에서 데이터 가져오기
with open('MH/products.csv', 'r', encoding='utf-8') as f:
    products = list(csv.reader(f))[1:]
    cur.execute("DELETE FROM products")
    cur.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products)
conn.commit()

# 테이블 조회 함수
def select_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return [list(product) for product in products]

# 테이블 업데이트 함수
def update_product_quantity(id, quantity):
    cur.execute("UPDATE products SET stock = ? WHERE id = ?", (quantity, id))
    conn.commit()

# 상품 정보 표시
def display_product_info(product):
    col1, col2, col3, col4 = st.beta_columns([1, 1, 1, 0.5])
    with col1:
        st.write(product[0])
    with col2:
        st.write(product[1])
    with col3:
        st.write(product[2])
        st.write(f"남은 수량: {product[3]}개")
    with col4:
        if product[3] == 0:
            st.write('품절')
        else:
            quantity = st.number_input('수량', value=1, min_value=1, max_value=product[3], key=f'quantity_{product[0]}')
            if st.button(f'구매 ({product[1]})', key=f'buy_{product[0]}'):
                new_quantity = product[3] - quantity
                update_product_quantity(product[0], new_quantity)
                updated_product = select_products()[product[0]-1]  # 업데이트된 값을 다시 가져옴
                st.success(f'{updated_product[1]} {quantity}개 구매 완료')
                product[3] = updated_product[3]  # 상품 정보를 수정

# 메인 함수
def main():
    # 상품 정보 가져오기
    products = select_products()

    # 페이지 헤더
    st.header('온라인 상점')

    # 페이지 내용
    for product in products:
        display_product_info(product)


if __name__ == '__main__':
    main()
