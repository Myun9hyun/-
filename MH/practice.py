import streamlit as st
import pandas as pd
import os


FILE_PATH1 = 'data1.csv'
FILE_PATH2 = 'data2.csv'
FILE_PATH3 = 'data3.csv'

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

def load_data3():
    try:
        data3 = pd.read_csv(FILE_PATH3)
    except FileNotFoundError:
        data3 = pd.DataFrame(columns=['Name', 'Product', 'Mount'])
    return data3

# 데이터를 파일에 저장하기
def save_data(data):
    data.to_csv(FILE_PATH1, index=False)

def save_data2(data2):
    data2.to_csv(FILE_PATH2, index=False)

def save_data3(data3):
    data3.to_csv(FILE_PATH3, index=False)

# 데이터 초기화 함수
def clear_data():
    global data, data2, data3
    data = pd.DataFrame(columns=['Name', 'Price', 'Mount'])
    data2 = pd.DataFrame(columns=['Name', 'Point','Product'])
    data3 = pd.DataFrame(columns=['Name', 'Product', 'Mount'])
    # 파일 삭제
    os.remove(FILE_PATH1)
    os.remove(FILE_PATH2)
    os.remove(FILE_PATH3)

# 불러온 데이터를 전역 변수로 저장
data = load_data()
data2 = load_data2()
data3 = load_data3()

# 사용자로부터 이름, 점수, 포인트, 수량을 입력받아 데이터프레임에 추가하는 함수
def add_data(name, price, mount):
    global data
    if name in data['Name'].values:
                st.warning(f'{name} (은)는 이미 있는 품목이야!')
                return
    data = data.append({'Name': name, 'Price': price, 'Mount': mount}, ignore_index=True)

def add_data2(name, point):
    global data2
    if name in data2['Name'].values:
                st.warning(f'{name} (은)는 이미 있는 이름이야!')
                return
    data2 = data2.append({'Name': name, 'Point': point}, ignore_index=True)

def add_data3(name, price, mount):
    global data3
    data3 = data3.append({'Name': name, 'Price': price, 'Mount': mount}, ignore_index=True)

def purchase_item(name, product_name, mount):
    global data, data2
    # data에서 product_name에 해당하는 row 선택
    row = data[data['Name'] == product_name].iloc[0]
    # data2에서 name에 해당하는 row 선택
    row2 = data2[data2['Name'] == name].iloc[0]
    # 구매하고자 하는 수량만큼 차감
    if row['Mount'] >= mount:
        data.loc[data['Name'] == product_name, 'Mount'] -= mount
        save_data(data)
        # 품목 가격만큼 point 차감
        total_price = row['Price'] * mount
        if row2['Point'] >= total_price:
            # 데이터프레임에 구매내역 추가
            data3 = load_data3()
            purchase_df = data3[(data3['Name'] == name) & (data3['Product'] == product_name)]
            if purchase_df.empty:
                purchase_df = pd.DataFrame({
                    'Name': [name],
                    'Product': [product_name],
                    'Mount': [mount]
                })
                data3 = pd.concat([data3, purchase_df], ignore_index=True)
            else:
                data3.loc[(data3['Name'] == name) & (data3['Product'] == product_name), 'Mount'] += mount
            save_data3(data3)
            # 구매자의 포인트 차감
            data2.loc[data2['Name'] == name, 'Point'] -= total_price
            save_data2(data2)
            st.success(f'{product_name} {mount}개 구매 완료!')
            # # 구매내역 호출 버튼 생성
            # st.button("구매내역 확인", on_click=view_purchase_history)
        else:
            st.warning(f'{name}은(는) {product_name}을(를) 구매할 포인트가 부족해!(┬┬﹏┬┬)')
    else:
        st.warning(f'{product_name}(은)는 품절되었어(⊙_⊙;)')


def save_purchase_history(name, product_name, mount):
    global data3
    data3 = data3.append({'Name': name, 'Product': product_name, 'Mount': mount}, ignore_index=True)
    
def delete_data(row_index):
            global data
            data = data.drop(index=row_index).reset_index(drop=True)
def delete_data2(row_index):
            global data2
            data2 = data2.drop(index=row_index).reset_index(drop=True)
def delete_data3(row_index):
            global data3
            data3 = data3.drop(index=row_index).reset_index(drop=True)
# Streamlit 앱 생성
# Streamlit 앱 생성
def main():
    password = 1234
    st.title('💜아기자기 다락방💙')
    st.write('아기자기의 다락방에 아깅이들을 초대할게!')
    tab1, tab2= st.tabs(["Howto", "Menu"])
    with tab2:
        options = ["데이터조회🔎", "물건구매🎁","데이터추가➕",'포인트지급📝', "데이터 초기화💣", "구매내역🛒", "데이터삭제✂"]
        option = st.selectbox("기능 선택", options)
        
        # 사용자로부터 이름, 점수, 포인트를 입력받는 UI 구성
        
        if option == '데이터추가➕':
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
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
        elif option == '포인트지급📝':
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
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
                st.write('물품 목록이야╰(*°▽°*)╯')
                st.write(data)
                st.write('지급된 포인트 목록이야ヾ(•ω•`)o')
                st.write(data2)
        # 포인트 차감 버튼
        elif option == '물건구매🎁':
            st.write('지급된 포인트와 물품 목록은 "데이터조회" 기능을 이용해줘(❁´◡`❁)')
            # 구매자 이름 입력창
            name = st.text_input('이름을 입력해줘😀')
            # 구매하려는 품목 선택창
            product_name = st.selectbox('구매하려는 품목을 선택해줘(❁´◡`❁)', options=data['Name'].tolist())
            # 구매 수량 입력창
            mount = st.number_input('구매 수량을 입력해줘╰(*°▽°*)╯', min_value=1)

            # 구매 버튼 클릭시 purchase_item 함수 실행
            if st.button('구매하기'):
                purchase_item(name, product_name, mount)

        elif option == '데이터 초기화💣':
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
            password_input = st.number_input('비밀번호를 입력해주세요 : ')
            if password_input == password:
                st.write('접근을 허용합니다')
                # 데이터 초기화 버튼
                st.write('☢아래의 버튼을 누르면 전부 초기화 됩니다!☢')
                if st.button('데이터 초기화'):
                    clear_data()
                    st.warning('데이터가 초기화 되었습니다.')
            else:
                st.warning('비밀번호가 틀렸습니다')
        elif option == '구매내역🛒':
            if st.button('구매내역 조회'):
                st.write(data3)
        elif option == "데이터삭제✂":
            st.error('⚠️길드 간부진만 접근할 수 있는 메뉴야o(￣┰￣*)ゞ!⚠️')
            password_input = st.number_input('비밀번호를 입력해주세요 : ')
            if password_input == password:
                st.success('접근을 허용합니다')
                delete_datas = ['품목', '명단', '구매내역']
                delete_datass = st.selectbox('삭제하려는 데이터를 선택하세요', delete_datas)
                if delete_datass == '품목':
                    # 사용자로부터 삭제할 행 번호 입력받기
                    st.write("품목입니다")
                    st.write(data)
                    row_index = st.number_input('삭제하고 싶은 품목의 번호를 입력해주세요', min_value=0, max_value=data.shape[0]-1)
                    if st.button('품목 삭제'):
                    # 해당 행이 존재할 경우, 행을 삭제
                        if row_index >= 0 and row_index < data.shape[0]:
                            delete_data(row_index)
                            save_data(data)  # 데이터를 파일에 저장
                            st.success('입력하신 행이 삭제되었습니다.')
                elif delete_datass == '명단':
                    st.write("포인트입니다")
                    st.write(data2)
                    row_index2 = st.number_input('삭제하고 싶은 포인트의 번호를 입력해주세요', min_value=0, max_value=data2.shape[0]-1)
                    if st.button('포인트 삭제'):
                        # 해당 행이 존재할 경우, 행을 삭제
                        if row_index2 >= 0 and row_index2 < data2.shape[0]:
                            delete_data2(row_index2)
                            save_data2(data2)  # 데이터를 파일에 저장
                            st.success('입력하신 행이 삭제되었습니다.')
                elif delete_datass == '구매내역':
                    st.write("구매내역 입니다")
                    st.write(data3)
                    row_index3 = st.number_input('삭제하고 싶은 구매내역의 번호를 입력해주세요', min_value=0, max_value=data2.shape[0]-1)
                    if st.button('구매내역 삭제'):
                        # 해당 행이 존재할 경우, 행을 삭제
                        if row_index3 >= 0 and row_index3 < data3.shape[0]:
                            delete_data3(row_index3)
                            save_data3(data3)  # 데이터를 파일에 저장
                            st.success('입력하신 행이 삭제되었습니다.')
            else :
                st.warning('비밀번호가 틀렸습니다.')
    with tab1:
        st.write()
        '''
        ##### 여기 있는 안내사항을 먼저 읽고 참여해줘!
        ##### 아기자기의 다락방은 아깅이들을 위해 만들었어!
        ##### 잘 이용해줬으면 좋겠어ლ(╹◡╹ლ) 
        ##### 기능을 먼저 알려줄게!
        > * 기능은 각각 ["데이터조회🔎", "물건구매🎁","데이터추가➕",'포인트지급📝', "데이터 초기화💣", "구매내역🛒", "데이터삭제✂"] 들이 있어!
        >> 우리 아깅이들은 데이터조회🔎와 물건구매🎁, 구매내역🛒만 이용할 수 있어!
        >> 나머지 기능들은 우리 빵셔틀들만 이용할 수 있으니 이해해줘!
        > * 데이터조회🔎를 누르면 다락방에 있는 물건들과 아깅이들의 포인트를 확인할 수 있어!
        >> 가지고 있는 포인트와 남아있는 물건을 잘 확인해줘(❁´◡`❁)
        > * 물건구매🎁를 누르면 다락방에 있는 물건을 아깅이가 가지고 있는 포인트로 가져갈 수 있어
        >> 구매 방법은 아래와 같아!
        >>> 1. 구매하는 아깅이의 이름을 입력해
        >>> 1. 가지고 싶은 물건을 목록에서 골라!
        >>> 1. 가지고 싶은 만큼 수량을 골라줘(❗수량 제한이 있으니 꼭 주의해서 구매해줘❗)
        >>> 1. 구매 버튼을 누르면 물건이 구매내역에 추가되고 포인트가 사용될거야!
        > * 구매내역🛒은 아깅이가 구매한 물건을 볼 수 있어!
        >> 구매한 물건이 맞는지 확인해주고, 혹시나 잘못 되었다면 빵셔틀들에게 꼭 알려줘! 우리가 고쳐줄게!
        '''
if __name__ == '__main__':
    main()
