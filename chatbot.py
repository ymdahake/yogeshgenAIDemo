from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq



#load environment variables

load_dotenv()

st.set_page_config(page_title="Generative AI chatbot Yogesh", page_icon="🤖", layout="centered")

st.title("🤖 Generative AI Chatbot with Groq API")

#intialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
#show chat history

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
#LLM INSTIANTIATION
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.0)

#inputbox
userprompt=st.chat_input("Ask Chatbot")
if userprompt:
    #display user message
    st.chat_message("user").markdown(userprompt)
    
    #add user message to chat history
    st.session_state.chat_history.append({"role":"user", "content":userprompt})
    
    #get response from LLM
    response=llm.invoke(
        input=[
            {"role":"system", "content":"You are a helpful assistant."},
            *st.session_state.chat_history,
          
        ]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role":"assistant", "content":assistant_response})    
    

    
    with st.chat_message("assistant"):
        st.markdown(assistant_response)