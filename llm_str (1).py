import streamlit as st
from groq import Groq

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        225deg,
        #2bc4ff 0%,
        #2bffff 20%,
        #2bffff 40%,
        #2bb3ff 60%,
        #2b2bff 80%,
        #2b00ff 100%
    ) !important;
}
/* Smooth transition */
[data-testid="stAppViewContainer"] {
    transition: background 0.3s ease;
}

[data-testid="stHeader"] {
    background: transparent !important;
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
