import streamlit as st

st.header('드롭다운')

option = st.selectbox(
     '가장 좋아하는 과목은 무엇인가요?',
     ('국어', '영어', '수학','사회','과학'))

st.write('당신이 좋아하는 과목은 ', option)
