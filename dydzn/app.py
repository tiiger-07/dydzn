import streamlit as st
import os

# 현재 스크립트의 디렉토리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 렌더링할 HTML 파일 경로를 정의합니다.
html_file_path = os.path.join(current_dir, "htmls", "index2.html")

# Streamlit 앱의 제목을 설정합니다.
st.set_page_config(page_title="HTML 파일 목록 - index2.html", layout="wide")

def main():
    """
    단일 HTML 파일을 읽어와서 Streamlit 앱에 표시하는 함수
    """
    st.title("HTML 파일 목록 (index2.html)")

    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # st.components.v1.html을 사용하여 HTML 코드를 렌더링합니다.
        st.components.v1.html(html_content, height=1200, scrolling=True)

    except FileNotFoundError:
        st.error(f"HTML 파일을 찾을 수 없습니다: {html_file_path}")
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
