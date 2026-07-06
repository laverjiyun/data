import streamlit as st

# 질문 4: 아이돌 노래 선호도 (드롭다운 선택)
st.markdown("#### **Q4. 솔직히 차 안에서 아이돌(K-POP) 노래 나오는 거 어때?**")

# 선택지 정의
kpop_options = [
    "🥳 완전 환영! 안무까지 쌉가능",
    "🎵 유명한 대중적인 곡이면 오케이",
    "🤔 굳이? 팝송이나 힙합이 나음",
    "❌ 절대 반대, 내 귀를 지켜줘"
]

# selectbox 컴포넌트 생성
kpop_preference = st.selectbox(
    label="K-POP에 대한 너의 솔직한 생각은?",
    options=kpop_options,
    index=None,
    placeholder="본인의 성향을 골라줘!"
)

if kpop_preference:
    st.write(f"너의 선택: {kpop_preference}")
