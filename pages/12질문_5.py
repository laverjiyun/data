import streamlit as st

st.title("🎵 나만의 음악 취향 설문조사")
st.write("당신의 음악적 취향을 알아보기 위한 간단한 설문입니다.")

st.markdown("---")

# 7번 문항: 음악 스펙트럼 (체크박스 형식)
st.subheader("7번. 너의 음악 스펙트럼은 어느 세대에 멈춰 있어? (시대별 취향)")
st.caption("※ 중복 선택이 가능합니다.")

# 추가 요청하신 클래식, 재즈 시대를 포함한 선택지 구성
options_7 = {
    "retro_2000": "라떼는 말이야~ 추억의 2000~2010년대 싸이월드 감성",
    "modern_pop": "2010 후반~현재 최신 차트 팝 & 아이돌",
    "old_pop": "세대 상관없이 해외 올드팝이나 레트로",
    "classic_era": "바흐부터 쇼팽까지, 고전적이고 우아한 클래식 시대",
    "jazz_era": "1920~50년대 낭만 가득한 재즈(Jazz) 시대"
}

# 사용자의 선택을 저장할 딕셔너리
selected_7 = {}
for key, value in options_7.items():
    selected_7[key] = st.checkbox(value, key=key)

st.markdown("---")

# 8번 문항: 불호 장르 (멀티셀렉트 또는 체크박스 형식 가능, 여기서는 깔끔하게 멀티셀렉트로 구현)
st.subheader("8번. \"이 장르만큼은 진짜 차 안에서 듣기 힘들다\" 하는 불호 장르는?")
st.caption("※ 중복 선택이 가능합니다.")

options_8 = [
    "시끄러운 메탈/헤비락",
    "정통 트로트",
    "너무 잔잔한 클래식/뉴에이지",
    "가사 없는 EDM"
]

selected_8 = st.multiselect("차 안에서 듣기 힘든 장르를 선택해주세요:", options_8)

st.markdown("---")

# 제출 버튼 및 결과 확인 (테스트용)
if st.button("설문 제출하기"):
    st.success("🎉 설문이 성공적으로 제출되었습니다!")
    
    # 7번 선택 결과 추출
    final_selected_7 = [value for key, value in options_7.items() if selected_7[key]]
    
    st.write("### 📝 당신의 선택 결과")
    st.write(f"**7번 문항 선택:** {', '.join(final_selected_7) if final_selected_7 else '선택 안 함'}")
    st.write(f"**8번 문항 선택:** {', '.join(selected_8) if selected_8 else '선택 안 함'}")
