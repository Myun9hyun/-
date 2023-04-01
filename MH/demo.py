import streamlit as st
import pandas as pd
import os


FILE_PATH1 = 'data1.csv'
FILE_PATH2 = 'data2.csv'

# 파일에서 데이터 불러오기
def load_data():
    try:
        data = pd.read_csv(FILE_PATH1)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Name', 'Price', 'Mount'])
    return data

def load_data2():
    try:
        data2 = pd.read_csv(FILE_PATH2)
    except FileNotFoundError:
        data2 = pd.DataFrame(columns=['Name', 'Point'])
    return data2

# 데이터를 파일에 저장하기
def save_data(data):
    data.to_csv(FILE_PATH1, index=False)

def save_data2(data2):
    data2.to_csv(FILE_PATH2, index=False)

# 데이터 초기화 함수
def clear_data():
    global data, data2
    data = pd.DataFrame(columns=['Name', 'Price', 'Mount'])
    data2 = pd.DataFrame(columns=['Name', 'Point','Product'])
    # 파일 삭제
    os.remove(FILE_PATH1)
    os.remove(FILE_PATH2)

# 불러온 데이터를 전역 변수로 저장
data = load_data()
data2 = load_data2()

# 사용자로부터 이름, 점수, 포인트, 수량을 입력받아 데이터프레임에 추가하는 함수
def add_data(name, price, mount):
    global data
    if name in data['Name'].values:
                st.warning(f'{name} (은)는 이미 있는 이름이야!')
                return
    data = data.append({'Name': name, 'Price': price, 'Mount': mount}, ignore_index=True)

def add_data2(name, point):
    global data2
    if name in data2['Name'].values:
                st.warning(f'{name} (은)는 이미 있는 이름이야!')
                return
    data2 = data2.append({'Name': name, 'Point': point}, ignore_index=True)

def deduct_mount(name, mount):
    global data
    row = data[data['Name'] == name].iloc[0]  # 이름이 일치하는 row 선택
    if row['Mount'] >= mount:  # 차감 가능한 경우
        data.loc[data['Name'] == name, 'Mount'] -= mount  # 포인트 차감
        save_data(data)  # 데이터를 파일에 저장
        # st.success(f'{mount} Point Deducted from {name} Successfully')
        return True
    else:  # 차감 불가능한 경우
        st.warning(f'Not enough mount for {name}')
        return False

def deduct_point(name, point):
    global data2
    row = data2[data2['Name'] == name].iloc[0]  # 이름이 일치하는 row 선택
    if row['Point'] >= point:  # 차감 가능한 경우
        data2.loc[data2['Name'] == name, 'Point'] -= point  # 포인트 차감
        data2(data2)  # 데이터를 파일에 저장
        # st.success(f'{point} Point Deducted from {name} Successfully')
    else:  # 차감 불가능한 경우
        st.warning(f'Not Enough Point for {name}')

def purchase_item(name, mount):
    # deduct_mount(name, mount)
    st.success(f'{mount} Point Purchased from {name} Successfully')
    
def add_purchase(name, product, mount):
    global data
    
    # 차감할 mount 계산
    price = prices[product]
    total_price = price * mount
    
    # 차감 함수 호출
    deduct_mount(name, total_price)
    
    # 새로운 데이터프레임 생성
    new_df = pd.DataFrame({'Name': [name], 'Product': [product], 'Mount': [mount], 'Total Price': [total_price]})
    
    # 기존 데이터프레임과 새로운 데이터프레임을 합쳐서 새로운 데이터프레임 생성
    data = pd.concat([data, new_df], ignore_index=True)
    
    # 데이터를 파일에 저장
    save_data(data)
    
    st.success(f'{name} purchased {mount} {product}(s) successfully.')

def delete_data(row_index):
            global data
            data = data.drop(index=row_index).reset_index(drop=True)
def delete_data2(row_index):
            global data2
            data2 = data2.drop(index=row_index).reset_index(drop=True)
# Streamlit 앱 생성
def main():
    password = 1234
    st.title('Add, Display and Deduct Point')
    options = ["데이터추가➕", '포인트분배', "데이터조회🔎", "포인트 삭제✂", "데이터 초기화💣", "구매내역", "데이터삭제✂", "데이터 다운로드💾"]
    option = st.selectbox("기능 선택", options)
    
    # 사용자로부터 이름, 점수, 포인트를 입력받는 UI 구성
    
    if option == '데이터추가➕':
        password_input = st.number_input('비밀번호를 입력해주세요 : ')
        if password_input == password:
            st.success('접근을 허용합니다')
            name = st.text_input('Enter Name')
            price = st.number_input('Enter Price', min_value=0, max_value=10000)
            # point = st.number_input('Enter Point', min_value=0, max_value=50)
            mount = st.number_input('Enter Mount', min_value=0, max_value=100)
    # 이름, 점수, 포인트가 입력되면 데이터프레임에 추가
            if st.button('데이터추가'):
                # if st.button('추가'):
                add_data(name, price, mount)
                save_data(data)  # 데이터를 파일에 저장
                st.success('Data Added Successfully')
        else :
            st.warning('비밀번호가 틀렸습니다.')
    elif option == '포인트분배':
        password_input = st.number_input('비밀번호를 입력해주세요 : ')
        if password_input == password:
            st.success('접근을 허용합니다')
            name = st.text_input('Enter Name')
            point = st.number_input('Enter Point', min_value=0, max_value=50)
    # 이름, 점수, 포인트가 입력되면 데이터프레임에 추가
            if st.button('데이터추가'):
                # if st.button('추가'):
                add_data2(name, point)
                save_data2(data2)  # 데이터를 파일에 저장
                st.success('Data Added Successfully')
        else :
            st.warning('비밀번호가 틀렸습니다.')

    elif option == '데이터조회🔎':
    # 저장된 데이터프레임 출력
        if st.button('데이터조회🔎'):
            st.write(data)
            st.write(data2)
    # 포인트 차감 버튼
    elif option == '포인트 삭제✂':
        st.write(data)
        st.write(data2)
        # Name = st.text_input('구매하시는 분의 이름을 입력해주세요')
        # product = st.text_input('구매하실 품목을 입력하세요')
        # Mount = st.number_input('구매하실 갯수를 입력하세요', min_value=0)
        # # name_index = name.tolist()
        # if st.button('구매하기'):
        #     deduct_mount(Name, Mount)
        item_name = st.text_input('Enter Item Name:')
        item_mount = st.number_input('Enter Item Mount:', value=1)
        if st.button('Purchase'):
            if item_name and item_mount:
                if deduct_mount(item_name, item_mount):
                    # 차감에 성공한 경우
                    purchase_item(item_name, item_mount)  # 품목을 구매합니다
                    # st.success(f'{item_mount} {item_name} Purchased Successfully')
                else:
                    # 차감에 실패한 경우
                    st.warning(f'Failed to purchase {item_name}')

    elif option == '데이터 초기화💣':
        password_input = st.number_input('비밀번호를 입력해주세요 : ')
        if password_input == password:
            st.write('접근을 허용합니다')
            # 데이터 초기화 버튼
            if st.button('Clear Data'):
                clear_data()
                st.warning('Data Cleared Successfully')
    elif option == '구매내역':
        purchase_name
        purchase_product
        purchase_mount
        add_purchase(name, product, mount):

    elif option == "데이터삭제✂":
                # 데이터 삭제 기능
                # if st.button('데이터 삭제'):
                    # 사용자로부터 삭제할 행 번호 입력받기
                    st.write(data)
                    st.write(data2)
                    row_index = st.number_input('삭제하고 싶은 데이터1의 번호를 입력해주세요', min_value=0, max_value=data.shape[0]-1)
                    st.write("Enter를 입력하면 삭제됩니다.")
                    if st.button('데이터1 삭제'):
                        # 해당 행이 존재할 경우, 행을 삭제
                        if row_index >= 0 and row_index < data.shape[0]:
                            delete_data(row_index)
                            save_data(data)  # 데이터를 파일에 저장
                            st.success('입력하신 행이 삭제되었습니다.')
                    elif st.button('데이터2 삭제'):
                        # 해당 행이 존재할 경우, 행을 삭제
                        if row_index >= 0 and row_index < data2.shape[0]:
                            delete_data2(row_index)
                            save_data2(data2)  # 데이터를 파일에 저장
                            st.success('입력하신 행이 삭제되었습니다.')
if __name__ == '__main__':
    main()
