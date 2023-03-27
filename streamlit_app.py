from email.policy import default
from multiprocessing.connection import answer_challenge
import os
import openai
import streamlit as st

from streamlit_chat import message
from Bot import mises, session_prompt
from Sentiment import sentiment

openai.api_key = os.getenv('OPENAI_API_KEY')

start_sequence = "\nAI:"
restart_sequence = "\n\Humano:"

st.set_page_config(
    page_icon='🏢',
    page_title='Chat Bot de Leyes de Guatemala',
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'About': "This is a chatbot created using OPENAI's Advance GPT-3 model",
        'Get Help': 'mailto:mpolanco@feylibertad.org',
        'Report a bug': "mailto:mpolanco@feylibertadd.org",
    }
)

st.title("Chat Bot de Leyes de Guatemala")
st.sidebar.title("🏢 Chat Bot de Leyes de Guatemala")
st.sidebar.markdown(""" **Feedback/Questions**: [ARIN](https://arin.website) """)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'chat_log' not in st.session_state:
    st.session_state['chat_log'] = session_prompt

chat_log = st.session_state['chat_log']

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

question = st.text_input("Pregunta sobre leyes de Guatemala:", value='¿Qué es el Código Civil?')
message(question, is_user=True)

answer = mises(question, chat_log)
chat_log = append_interaction_to_chat_log(question, answer, chat_log)
message(answer)

with st.expander("¿No está seguro de qué preguntar?"):
    st.markdown(""" Pruebe con alguna de estas preguntas:
    

1. ¿Cuál es la diferencia entre el Código Penal y el Código Civil?
2. ¿Qué es la Constitución Política de la República de Guatemala?
3. ¿Cuáles son los derechos fundamentales en Guatemala?

    """)
