import streamlit as st
import pandas as pd
import pickle

# 모델 불러오기
model_path = "MH/model_RF.pkl"
with open(model_path, 'rb') as f:
model = pickle.load(f)


# 입력된 데이터를 이용해 타겟 변수를 예측하는 함수를 정의합니다.
def predict(model, input_df):
    predictions = model.predict(input_df)
    return predictions

# Streamlit 앱을 정의합니다.
def app():
    # 앱 제목을 설정합니다.
    st.title("Random Forest 모델 예측")
    
    # 데이터 업로드를 위한 사이드바를 만듭니다.
    st.sidebar.title("데이터 업로드")
    uploaded_file = st.sidebar.file_uploader("CSV 파일 선택", type="csv")
    
    # 사용자 입력 폼을 생성합니다.
    st.sidebar.title("입력 특성")
    sepal_length = st.sidebar.slider("꽃받침 길이", 4.0, 8.0, 5.0)
    sepal_width = st.sidebar.slider("꽃받침 너비", 2.0, 4.5, 3.0)
    petal_length = st.sidebar.slider("꽃잎 길이", 1.0, 7.0, 4.0)
    petal_width = st.sidebar.slider("꽃잎 너비", 0.1, 2.5, 1.0)
    
    # 사용자 입력을 데이터프레임으로 결합합니다.
    input_data = {'sepal_length': sepal_length,
                  'sepal_width': sepal_width,
                  'petal_length': petal_length,
                  'petal_width': petal_width}
    input_df = pd.DataFrame([input_data])
    
    # 모델을 이용해 예측합니다.
    if st.sidebar.button("예측"):
        predictions = predict(model, input_df)
        st.write("예측된 타겟 변수 값은:", predictions[0])
    
# Streamlit 앱을 실행합니다.
if __name__ == '__main__':
    app()
