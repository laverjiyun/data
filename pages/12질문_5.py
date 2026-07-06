import streamlit as st

st.title("🎵 음악 취향 설문조사")

# 7번 문항 독립 구성
st.subheader("7번. 너의 음악 스펙트럼은 어느 세대에 멈춰 있어? (시대별 취향)")
st.caption("※ 중복 선택이 가능합니다.")

# 선택지 정의 (클래식, 재즈 시대 추가)
options_7 = {
    "retro_2000": "라떼는 말이야~ 추억의 2000~2010년대 싸이월드 감성",
    "modern_pop": "2010 후반~현재 최신 차트 팝 & 아이돌",
    "old_pop": "세대 상관없이 해외 올드팝이나 레트로",
    "classic_era": "바흐부터 쇼팽까지, 고전적이고 우아한 클래식 시대",
    "jazz_era": "1920~50년대 낭만 가득한 재즈(Jazz) 시대"
}

# 체크박스 생성 및 결과 저장
selected_7 = {}
for key, value in options_7.items():
    selected_7[key] = st.checkbox(value, key=f"ch7_{key}")

# 선택된 항목 확인 버튼 (선택 사항)
if st.button("7번 문항 결과 확인"):
    final_selected_7 = [value for key, value in options_7.items() if selected_7[key]]
    if final_selected_7:
        st.info(f"선택한 취향: {', '.join(final_selected_7)}")
    else:
        st.warning("선택된 항목이 없습니다.")
