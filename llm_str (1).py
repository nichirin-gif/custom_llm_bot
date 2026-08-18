import streamlit as st
from groq import Groq

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(
            90deg,
            rgba(131, 58, 180, 1) 0%,
            rgba(253, 29, 29, 1) 50%,
            rgba(252, 176, 69, 1) 100%
        );
    }
</style>
""", unsafe_allow_html=True)

st.title("Swapnil's Chat Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages: # 
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Type a message...")

if prompt:
    # this below line will append
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)


    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[ 
            {"role": "system", "content": "you are a funny sarcastic assistant"},
            *st.session_state.messages
        ]
    )
    reply = response.choices[0].message.content.strip()
    # this below line will append to msg []
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
