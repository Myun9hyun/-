import streamlit as st
import pandas as pd

# 업로드한 파일을 데이터프레임으로 변환하는 함수
def upload_excel_file(file):
    df = pd.read_excel(file)
    return df

# 업로드한 파일을 저장하는 함수
def save_uploaded_file(uploadedfile):
    with open(uploadedfile.name, 'wb') as f:
        f.write(uploadedfile.getbuffer())
    return st.success("저장되었습니다: {}".format(uploadedfile.name))

# Streamlit 앱
def main():
    st.title("Excel 파일 업로드 예제")
    uploaded_file = st.file_uploader("Excel 파일 업로드", type=["xlsx"])
    
    if uploaded_file is not None:
        # 업로드한 파일을 저장하고, 데이터프레임으로 변환
        save_uploaded_file(uploaded_file)
        df = upload_excel_file(uploaded_file)
        
        # 데이터프레임 출력
        st.write("데이터프레임")
        st.write(df)

if __name__ == "__main__":
    main()
