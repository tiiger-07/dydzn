import streamlit as st
import os
import streamlit.components.v1 as components # components 모듈을 st.components.v1로 임포트합니다.

# 현재 스크립트의 디렉토리를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
html_folder = os.path.join(current_dir, "htmls")

# 렌더링할 HTML 파일들을 정의하고 페이지 이름을 지정합니다.
pages = {
    "3D 구성 모형 연구 계획서": "index.html",
    "관심사 기반 조 편성 프로그램": "index2.html",
    "100에 가까운 숫자 만들기 게임": "index3.html",
    "맞춤 경로 추천 시뮬레이션 계획서": "index4.html",
    "주차장 최단 경로 탐색 시뮬레이션": "index5.html"  # 동적 빈 공간 시뮬레이션 추가
}

# Streamlit 앱의 제목과 레이아웃을 설정합니다.
st.set_page_config(page_title="페이지 이동 가능한 연구 계획서", layout="wide")

def main():
    """
    사용자가 선택한 HTML 파일을 Streamlit 앱에 표시하는 함수
    """
    st.sidebar.title("페이지 이동")
    
    # 사이드바에 페이지 선택을 위한 드롭다운 메뉴를 만듭니다.
    selected_page = st.sidebar.selectbox("보고 싶은 페이지를 선택하세요:", list(pages.keys()))

    st.title(f"{selected_page}")
    st.markdown("---")
    
    # 선택된 페이지에 해당하는 HTML 파일 경로를 가져옵니다.
    file_name = pages[selected_page]
    
    # 가정: 모든 HTML 파일은 'htmls' 폴더 내에 존재합니다.
    html_file_path = os.path.join(html_folder, file_name)
    
    try:
        # HTML 파일을 읽어옵니다.
        # 주의: 실제 환경에서는 'htmls' 폴더를 생성하고 필요한 HTML 파일들을 넣어주셔야 합니다.
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # st.components.v1.html을 사용하여 HTML 코드를 렌더링합니다.
        components.html(html_content, height=1200, scrolling=True)

    except FileNotFoundError:
        st.error(f"HTML 파일을 찾을 수 없습니다: {html_file_path}")
    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
