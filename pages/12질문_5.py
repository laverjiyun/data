import streamlit as st

st.title("🎵 나만의 음악 취향 설문 웹앱")

st.markdown("---")

# 7번 문항: 체크박스(멀티셀렉트) 형태
st.subheader("Q7. 너의 음악 스펙트럼은 어느 세대에 멈춰 있어? (시대별 취향)")

# 선택지 정의 (기존 선택지 + 클래식, 재즈 시대 추가)
options = [
    "☕ 라떼는 말이야~ 추억의 2000~2010년대 싸이월드 감성",
    "🔥 2010 후반~현재 최신 차트 팝 & 아이돌",
    "🌍 세대 상관없이 해외 올드팝이나 레트로",
    "🎻 바흐부터 쇼팽까지, 고전적이고 우아한 클래식 시대",
    "🎷 1920~50년대 낭만 가득한 스윙 & 재즈 시대"
]

# 사용자의 선택 저장
selected_eras = st.multiselect(
    "너의 음악적 취향을 모두 골라봐! (중복 선택 가능)",
    options
)

# 결과 확인용 출력
if selected_eras:
    st.write("**내가 선택한 음악 스펙트럼:**")
    for era in selected_eras:
        st.write(f"- {era}")
