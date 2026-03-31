import streamlit as st

st.title('사용자 입력 폼')

# 제출 후 버튼 스타일 변경을 위한 CSS
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

with st.form('customer_form'):
    name = st.text_input('이름')
    age = st.number_input('나이', min_value=1, value=1, step=1)
    agree = st.checkbox('약관에 동의합니다')
    
    submitted = st.form_submit_button('제출')
    
if submitted:
    st.session_state.submitted = True
    st.write(f'이름: {name}, 나이: {age}')
    
    if agree:
        st.success('약관에 동의하셨습니다.')
    else:
        st.error('약관에 동의하셔야합니다.')