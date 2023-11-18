import streamlit as st
from langchain.llms import CTransformers

llm = CTransformers(
    model="models/llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title('인공지능 시인')

content = st.text_input('시의 주제를 제시해주세요.','apple')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중... (wait 30 seconds)'):
        result = llm.predict("write a poem about " + content + ": ")
        st.write(result)


# ==========================================================
# > streamlit run 4-2.py

#    --> ModuleNotFoundError: No module named 'ctransformers'

#    이건 streamlit 문제임. 아래 명령어로 대체하여 해결 가능

# > python3 -m streamlit run 4-2.py 

# # https://github.com/streamlit/streamlit/issues/1780
# ==========================================================
