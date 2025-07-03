import os
import streamlit as st
import google.generativeai as gen_ai
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # or with full path if needed
print("Loaded key:", os.getenv("GOOGLE_API_KEY"))

#configure streamlit page settings
st.set_page_config(
    page_title="Chat With AI Bot",
    page_icon=":brain:",
    layout = "centered",
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#set-up google geminipro - ai model

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-pro")



#function to translate roles between gemini-pro and streamlit terminology

def translate(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role

#initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

#display chat history
st.title("Chat With AraaAI")

for message in st.session_state.chat_session.history:
    with st.chat_message(translate(message.role)):
        st.markdown(message.parts[0].text)

#input field
user_prompt = st.chat_input("Ask me anything!")
if user_prompt:
    #add user's msg and show it
    st.chat_message("user").markdown(user_prompt)
    #send user's msg to gemini pro
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

