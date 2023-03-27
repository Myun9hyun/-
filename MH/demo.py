import streamlit as st
import pickle

# 모델 불러오기
model_path = "MH/model.pkl"

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# 예측 함수 정의
def predict(data):
    result = model.predict(data)
    return result

# Streamlit 앱 구성
def main():
    st.title("머신러닝 모델 예측")
    data = st.text_input("데이터를 입력하세요")
    prediction = predict(data)
    st.write("결과:", prediction)

if __name__ == '__main__':
    main()
