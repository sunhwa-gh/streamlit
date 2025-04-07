import streamlit as st
import os
from groq import Groq

# Streamlit UI
st.title('Groq API 데모')

# 사용자 입력
user_input = st.text_input("질문을 입력해주세요:")

# Grog키 입력받아 *문자로 대체하기
st.sidebar.header('입력')
api_key = st.sidebar.text_input('groq key를 입력해주세요', type='password')

if not api_key:
 #   st.error("API Error")
    st.stop()

# Groq 클라이언트 초기화
client = Groq(api_key=api_key)

def get_response(question):
    """ Groq API 함수 """
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": question}
        ],
        #model="llama3-70b-8192",
        model="qwen-qwq-32b",
    )
    return chat_completion.choices[0].message.content

if st.button('회신'):
    with st.spinner('회신중...'):
        response = get_response(user_input)
        st.write(response)

