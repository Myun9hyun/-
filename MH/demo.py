import streamlit as st
import pickle
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# # 모델 불러오기
# model_path = "MH/model.pkl"

# with open(model_path, 'rb') as f:
#     model = pickle.load(f)

st.title('Linear Regression Model')

# create sidebar with input parameters
st.sidebar.header('Input Parameters')
x = st.sidebar.slider('X', 0.0, 10.0, 5.0, 0.1)

# use model to make prediction
prediction = model.predict(x)

y = model.prediction([[x]])

# prediction = model.predict(x)
# show prediction result
st.subheader('Prediction Result')
st.write('Y:', y[0])

# # 예측 함수 정의
# def predict(data):
#     result = model.predict(data)
#     return result

# # Streamlit 앱 구성
# def main():
#     st.title("머신러닝 모델 예측")
#     data = st.text_input("데이터를 입력하세요")
#     prediction = predict(data)
#     st.write("결과:", prediction)

# if __name__ == '__main__':
#     main()


# import streamlit as st
# import pickle

# # load saved linear regression model
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

# st.title('Linear Regression Model')

# # create sidebar with input parameters
# st.sidebar.header('Input Parameters')
# x = st.sidebar.slider('X', 0.0, 10.0, 5.0, 0.1)

# # use model to make prediction
# y = model.predict([[x]])

# # show prediction result
# st.subheader('Prediction Result')
# st.write('Y:', y[0])
