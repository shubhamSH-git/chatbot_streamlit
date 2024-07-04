import streamlit as st
import time

st.title("Talk Back to me!")

if "messages" not in st.session_state:
	st.session_state.messages=[]

for message in st.session_state.messages:
	with st.chat_message(message["role"]):
		st.markdown(message["content"])

if prompt:=st.chat_input("What is up?"):
	response=f"{prompt}"
	time.sleep(1)	
	with st.chat_message("assistant"):
		st.markdown(response) 
		
	st.session_state.messages.append({"role":"assistant","content":response})
