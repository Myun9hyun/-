# 버튼을 누르면 결과가 출력되는 함수
def open_box():
    with st.spinner("결과를 계산하는 중입니다..."):
        time.sleep(3)  # 3초간 로딩 중임을 표시
        selected_values = random_values(values, probabilities, n)
        if '코젬' in selected_values or '경뿌' in selected_values or '반파별4개' in selected_values or '수에큐3개' in selected_values or '소경축비' in selected_values:
            for i in range(min(n, len(selected_values))):
                st.warning(f"아쉽습니다.. {selected_values[i]}(이)가 나왔습니다..")
        elif '명큡' in selected_values or '앱상' in selected_values or '강환불' in selected_values or '미코젬' in selected_values or '주흔_한묶음' in selected_values:
            for i in range(min(n, len(selected_values))):
                st.balloons()
                st.success(f"상자에서 {selected_values[i]}(이)가 나왔습니다!")
        else:
            for i in range(min(n, len(selected_values))):
                st.success(f"축하드립니다! {selected_values[i]}(이)가 당첨되었습니다!")
# Streamlit 앱을 실행합니다.
st.title("🐻아기자기 랜덤박스🎁")
st.write()
'''
##### 랜덤박스🎁 내 물품은 다음과 같습니다

| 구분 |  구성품 | 확률 | 
|:---: | :---: | :---: | 
| 꽝💣 | 코젬, 경뿌, 반파별4개, 수에큐3개, 소경축비 | 7.4% |
| 대박🎊 | 명큡, 앱솔상자, 강환불, 미코젬, 주흔 한묶음 | 6% |
| 일반💰 | 반빨별, 재획비, 경축비, 고보킬, 고대비, 명훈, 장큐, 거코젬 | 3% | 
'''
# 출력을 원하는 개수를 입력받습니다.
n = st.number_input("상자를 오픈하실 개수를 입력하세요:", min_value=1, max_value=10, step=1, value=1)

# '상자 열기' 버튼을 눌렀을 때 결과가 출력되도록 합니다.
if st.button("상자 열기"):
    open_box()
