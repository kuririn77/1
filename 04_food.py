import streamlit as st
import random

# 🌈 페이지 설정
st.set_page_config(
    page_title="오늘 뭐 먹지? 🍽️✨",
    page_icon="🍱",
    layout="centered",
)

# 🎨 타이틀
st.markdown("""
<div style='text-align: center;'>
  <h1 style='color:#ff6fb5;'>🌞 오늘의 날씨 + 💖 기분 = 🍴 메뉴 추천</h1>
  <h3 style='color:#666;'>당신의 하루에 어울리는 메뉴를 찾아드려요 🌈</h3>
</div>
""", unsafe_allow_html=True)

# ☀️ 선택 파트
weather = st.selectbox(
    "☁️ 오늘의 날씨를 선택하세요!",
    ["☀️ 맑음", "🌧️ 비", "⛅ 흐림", "❄️ 눈", "🌪️ 바람", "🌈 기타"]
)

mood = st.selectbox(
    "😊 오늘의 기분은 어떤가요?",
    ["😆 신남", "😴 피곤함", "🥰 행복함", "😢 슬픔", "😡 화남", "🤔 평온함"]
)

# 🍱 메뉴 데이터 (간략 버전)
menu_data = {
    "☀️ 맑음": {
        "😆 신남": [("냉모밀 🍜", 450, "시원하고 깔끔하게!")],
        "😴 피곤함": [("치킨 🍗", 870, "기운 내기 딱 좋아!")],
        "🥰 행복함": [("스테이크 🥩", 760, "행복한 한 끼!")],
        "😢 슬픔": [("케이크 🍰", 430, "달콤한 위로 한 조각!")],
        "😡 화남": [("불닭볶음면 🔥", 700, "스트레스 날려버리자!")],
        "🤔 평온함": [("비빔밥 🥗", 560, "균형 잡힌 한 끼!")]
    },
    "🌧️ 비": {
        "😆 신남": [("부침개 🥞", 600, "비 오는 날엔 역시!")],
        "😴 피곤함": [("라면 🍜", 500, "뜨끈한 한입!")],
        "🥰 행복함": [("수제버거 🍔", 680, "든든한 행복!")],
        "😢 슬픔": [("초콜릿 케이크 🍫🍰", 550, "달콤한 위로!")],
        "😡 화남": [("불족발 🌶️", 850, "매운 걸로 풀자!")],
        "🤔 평온함": [("우동 🍲", 480, "부드럽고 따뜻하게!")]
    },
}

# 🎯 메뉴 추천
if st.button("🍽️ 오늘의 추천 메뉴 보기!"):
    selected_menu = random.choice(menu_data[weather][mood])
    name, kcal, desc = selected_menu

    # 추천 카드
    st.markdown(f"""
    <div style='text-align:center;
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        border-radius: 20px;
        padding: 30px;
        margin-top: 25px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.25);'>
        <h2 style='color:white;'>✨ 오늘의 추천 메뉴 ✨</h2>
        <h1 style='color:white; font-size:2.5em;'>🍱 {name}</h1>
        <p style='color:white; font-size:1.2em;'>🔥 칼로리: {kcal} kcal</p>
        <p style='color:white; font-size:1.1em;'>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

    # 💬 만족도 설문 추가
    st.markdown("### 😋 오늘 추천 메뉴는 어땠나요?")
    satisfaction = st.radio(
        "만족도 선택:",
        ["😍 최고예요!", "😊 괜찮아요!", "😐 그냥 그래요", "😢 별로였어요..."],
        index=None,
        horizontal=True
    )

    if satisfaction:
        st.markdown(f"""
        <div style='text-align:center; margin-top:20px;'>
            <h3>💌 소중한 의견 감사합니다!</h3>
            <p>당신의 반응: <b>{satisfaction}</b></p>
        </div>
        """, unsafe_allow_html=True)

# 💬 푸터
st.markdown("""
---
<div style='text-align:center; color:gray;'>
  Made with 💖 by ChatGPT | 오늘도 맛있고 행복한 하루 보내세요 🍀
</div>
""", unsafe_allow_html=True)
