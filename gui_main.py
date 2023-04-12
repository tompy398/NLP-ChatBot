import sys
from chatbot.Chatbot import Chatbot
from chatbot.YoutubeToolkit import YoutubeToolkit
from chatbot.NLPTechniques import NLPTechniques
from User import User
import pickle
import re
import textwrap
import html
from urllib.parse import urlparse, parse_qs
import os
import streamlit as st
from streamlit_chat import message

# An observation is that the st.session_state is saved somehow regardless of continuous reruns of the invoked python file
# This implies that when a program is rerun, the memory is not saved yet this is a contradiction to that reasoning.

# This is for a new run of streamlit, so we have to initialize all the variables here



def get_text(user_name):
    input_text = st.text_input(user_name + ":", key="input")
    return input_text


def main():
    message("Test")
    message("Tester")
    if 'state' not in st.session_state:
        st.session_state['state'] = ['New Instance']
        st.session_state['checked_history'] = None
        st.session_state['prev_user_log'] = None
        st.session_state['user_name'] = None
        #st.session_state['YT_OBJ'] = YoutubeToolkit() # Error Here Perhaps?
        #st.session_state['NLP_OBJ'] = NLPTechniques()

    match st.session_state['state']:
        case 'New Instance':
            if not check_if_history_exists():
                message("What's your name?")
                st.session_state['user_name'] = get_text('User')
            message("testeing12")


def check_if_history_exists():
    files_list = os.listdir('./')
    for file in files_list:
        if file.endswith('.p'):
            st.session_state['prev_user_log'] = file
        return True
    return False

if __name__ == '__main__':
    main()