import streamlit as st
import os

# 현재 스크립트의 디렉토리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# htmls 폴더에 있는 index.html 파일의 전체 경로를 만듭니다.
html_file_path = os.path.join(current_dir, "htmls", "index.html")

# Streamlit 앱의 제목을 설정합니다.
st.set_page_config(page_title="3D 구성 모형 연구 계획서", layout="wide")

def main():
    """
    HTML 파일을 읽어와서 Streamlit 앱에 표시하는 함수
    """
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # st.components.v1.html을 사용하여 HTML 코드를 렌더링합니다.
        # height와 scrolling 속성을 조절하여 웹 페이지가 잘 보이도록 합니다.
        st.components.v1.html(html_content, height=1200, scrolling=True)

    except FileNotFoundError:
        st.error(f"HTML 파일을 찾을 수 없습니다: {html_file_path}")
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
