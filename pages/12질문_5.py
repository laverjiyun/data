import streamlit as st

st.title("🎵 나만의 음악 취향 설문 웹앱")

st.markdown("---")

# 7번 문항: 슬라이더 형태
st.subheader("Q7. 너의 음악 스펙트럼은 어느 세대에 멈춰 있어? (시대별 취향)")

# 슬라이더에 들어갈 시대 순서 정의
era_timeline = [
    "클래식 시대 (고전/낭만)",
    "오리지널 재즈 시대 (1920~50s)",
    "해외 올드팝/레트로",
    "싸이월드 감성 (2000~2010s)",
    "최신 차트 팝&아이돌 (2010후반~현재)"
]

# 슬라이더 구현
selected_era_slider = st.select_slider(
    "슬라이더를 움직여 네 취향의 중심축을 찾아봐!",
    options=era_timeline,
    value="싸이월드 감성 (2000~2010s)" # 기본값 설정
)

# 결과 확인용 출력
st.write(f"**나의 음악 스펙트럼 중심지:** `{selected_era_slider}`")
