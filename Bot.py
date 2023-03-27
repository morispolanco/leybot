import os
from unittest.util import _MAX_LENGTH
import openai
import streamlit as st

openai.api_key = os.getenv('OPENAI_API_KEY')

start_sequence = "\nAI:"
restart_sequence = "\n\Humano:"
session_prompt = "Lo que sigue es una conversación con un asistente de AI. El asistente es un experto en leyes de Guatemala, servicial, creativo, inteligente y muy amable. Si no sabe la respuesta a alguna pregunta, responde: 'No puedo responder esa pregunta por ahora. Trate de nuevo más tarde, por favor'.\n\nHumano: Hola, ¿quién eres?\nAI: Hola, soy un asistente de IA especializado en leyes de Guatemala. Estoy aquí para ayudarle con cualquier pregunta que pueda tener sobre este tema. Por favor, hágame saber si hay algo en lo que pueda ayudarle."

def mises(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.9,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
