import streamlit as st

import streamlit as st

def main():
    st.set_page_config(
        page_title="My Custom Page Title",
        page_icon=":smiley:",
        layout="wide",
        # 배경색을 검은색으로 설정합니다.
        background_color="#000000"
    )

    # Streamlit 애플리케이션 내용 작성하기
    st.write("Hello, world!")

if __name__ == "__main__":
    main()
