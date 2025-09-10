import streamlit as st
import os

# 현재 스크립트의 디렉토리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))

# 렌더링할 HTML 파일 경로 목록을 정의합니다.
# 'index.html'과 'index2.html' 파일이 htmls 폴더에 있다고 가정합니다.
html_file_paths = [
    os.path.join(current_dir, "htmls", "index.html"),
    os.path.join(current_dir, "htmls", "index2.html")
]

# Streamlit 앱의 제목을 설정합니다.
st.set_page_config(page_title="3D 구성 모형 연구 계획서", layout="wide")

def main():
    """
    여러 HTML 파일을 읽어와서 Streamlit 앱에 표시하는 함수
    """
    st.title("HTML 파일 목록")

    # 파일 경로 목록을 순회하며 파일을 읽고 렌더링합니다.
    for file_path in html_file_paths:
        file_name = os.path.basename(file_path)
        
        st.subheader(f"--- {file_name} ---")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # st.components.v1.html을 사용하여 HTML 코드를 렌더링합니다.
            st.components.v1.html(html_content, height=1200, scrolling=True)

        except FileNotFoundError:
            st.error(f"HTML 파일을 찾을 수 없습니다: {file_path}")
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
