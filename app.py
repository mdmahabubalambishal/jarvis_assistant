import streamlit as st
from jarvis.assistant import JarvisAssistant

st.set_page_config(page_title="JARVIS AI", layout="centered")

jarvis = JarvisAssistant()

st.title("🤖 JARVIS – Personal AI Assistant")
st.write(jarvis.greet())

role = st.selectbox(
    "Select Role",
    ["General", "Tutor", "Coder", "Career"]
)

question = st.text_area("Ask something")

if st.button("Ask JARVIS"):
    if question.strip():
        answer = jarvis.chat(question, role)
        st.success(answer)
    else:
        st.warning("Please enter a question")