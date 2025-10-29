import streamlit as st

# 🌈 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천 💼✨",
    page_icon="🧠",
    layout="wide",
)

# 🌟 제목
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-size: 3em; color: #ff66b2;'>🌸 MBTI별 완벽한 직업 찾기 💼</h1>
    <p style='font-size: 1.3em;'>너의 성격 유형에 딱 맞는 직업을 추천해줄게! 🌈</p>
</div>
""", unsafe_allow_html=True)

# 🎨 사이드바
st.sidebar.markdown("## 🔮 나의 MBTI 선택하기")
mbti = st.sidebar.selectbox(
    "MBTI 유형을 골라주세요 👇",
    [
        "ISTJ 🧩", "ISFJ 🧸", "INFJ 🌿", "INTJ 🧠",
        "ISTP 🛠️", "ISFP 🎨", "INFP 🌈", "INTP 📚",
        "ESTP 🚀", "ESFP 🎉", "ENFP 🔥", "ENTP ⚡",
        "ES
