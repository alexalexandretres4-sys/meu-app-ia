import streamlit as st
from google import genai
import os

st.set_page_config(page_title="Meu App de IA", page_icon="🤖")
st.title("🤖 Meu Chat com IA")

# Colocamos a sua chave real direto no código para evitar erros de leitura
api_key = "AQ.Ab8RN6I3tONVEHEU1DKD5Q2vdFjjLK2bnfs8CDNKfAM3NOfdba"

if not api_key:
    st.error("Chave API não encontrada.")
else:
    # Conexão direta usando o código da sua chave
    client = genai.Client(api_key=api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Digite sua mensagem..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception:
                st.error("Erro ao conectar com a IA.")
                
