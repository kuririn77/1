import streamlit as st

# 🌈 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 직업 추천 🎯",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 💖 타이틀
st.markdown("""
<div style='text-align: center;'>
    <h1 style='color:#ff69b4;'>🌟 MBTI 기반 진로 추천 💼</h1>
    <h3>너의 성격에 딱 맞는 직업을 찾아보자! ✨</h3>
</div>
""", unsafe_allow_html=True)

# 🧠 MBTI별 직업 추천 데이터
jobs = {
    "INTJ": ("전략가 🧩", ["데이터 분석가 📊", "정책기획자 🏛️", "UX 디자이너 🎨"]),
    "INTP": ("사색가 💭", ["연구원 🔬", "개발자 💻", "철학자 📚"]),
    "ENTJ": ("지도자 👑", ["CEO 💼", "기획팀장 🗂️", "변호사 ⚖️"]),
    "ENTP": ("도전자 ⚡", ["창업가 🚀", "마케팅 디렉터 📣", "광고기획자 🎬"]),
    "INFJ": ("옹호자 🌿", ["상담사 💬", "작가 ✍️", "사회운동가 🕊️"]),
    "INFP": ("중재자 🌈", ["예술가 🎭", "심리상담가 🧠", "교사 🍎"]),
    "ENFJ": ("선도자 🌟", ["강사 🎤", "인사담당자 🧾", "홍보전문가 📢"]),
    "ENFP": ("활동가 🔥", ["크리에이터 🎥", "광고홍보 🎨", "기획자 💡"]),
    "ISTJ": ("현실주의자 🧱", ["공무원 🏛️", "회계사 📘", "엔지니어 ⚙️"]),
    "ISFJ": ("수호자 💐", ["간호사 💉", "교사 🍀", "행정직원 🗃️"]),
    "ESTJ": ("관리자 🏗️", ["팀장 👔", "경영자 💰", "군인 🪖"]),
    "ESFJ": ("사교가 💞", ["간호사 💊", "사회복지사 🕊️", "이벤트플래너 🎈"]),
    "ISTP": ("장인 ⚙️", ["정비사 🔧", "엔지니어 🔩", "파일럿 🛫"]),
    "ISFP": ("예술가 🎨", ["디자이너 🪡", "사진작가 📷", "플로리스트 🌷"]),
    "ESTP": ("사업가 🚀", ["세일즈맨 💳", "스포츠 매니저 🏆", "기업가 💼"]),
    "ESFP": ("연예인 🌟", ["배우 🎬", "방송인 🎤", "이벤트기획자 🎉"])
}

# 🎯 MBTI 선택
selected_mbti = st.selectbox("👇 너의 MBTI를 선택해보자!", list(jobs.keys()))

if selected_mbti:
    title, recommended_jobs = jobs[selected_mbti]

    st.markdown(f"""
    <div style='text-align: center; background: linear-gradient(135deg, #f9c5d1 0%, #9795ef 100%);
        border-radius: 20px; padding: 30px; margin-top: 30px; box-shadow: 0px 5px 15px rgba(0,0,0,0.2);'>
        <h2 style='color: white;'>✨ {selected_mbti} - {title} ✨</h2>
        <h3>이런 직업이 잘 어울려요 💖</h3>
        <ul style='list-style: none; color: white; font-size: 1.3em;'>
            {''.join([f"<li>👉 {job}</li>" for job in recommended_jobs])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 💬 푸터
st.markdown("""
---
<div style='text-align:center; color:gray;'>
    Made with 💕 by <b>진로MBTI</b> | 즐겁게 너의 길을 찾아봐 🌈
</div>
""", unsafe_allow_html=True)
