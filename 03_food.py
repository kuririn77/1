import streamlit as st
import random

# 페이지 설정 (파일 최상단에 위치)
st.set_page_config(
    page_title="오늘 뭐 먹지? 🍽️✨",
    page_icon="🍱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------------------------------------
# 스타일 헬퍼 (간단 CSS)
HEADER_HTML = """
<div style='text-align: center;'>
  <h1 style='margin:0; color: #ff6fb5;'>🌞 오늘의 날씨 + 💖 기분 = 🍴 메뉴 추천</h1>
  <p style='margin:0; color: #666;'>이모지 팡팡 ✨ 화려하고 예쁘게 추천해드려요!</p>
</div>
"""
CARD_STYLE = """
border-radius: 20px; padding: 24px; margin-top: 16px;
box-shadow: 0 6px 18px rgba(0,0,0,0.12);
background: linear-gradient(135deg, #fff0f6 0%, #f0f7ff 100%);
text-align:center;
"""
# -----------------------------------------
