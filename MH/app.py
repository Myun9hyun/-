import streamlit as st
import pandas as pd

# 엑셀 파일 업로드


uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

# 업로드한 파일을 데이터프레임으로 변환
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    # 데이터프레임 출력
    st.write(pd.DataFrame(df))
