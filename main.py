import streamlit as st
from google import genai
import os

st.set_page_config(page_title="Meu App de IA", page_icon="🤖")
st.title("🤖 Meu Chat com IA")

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Chave API não encontrada.")
else:
    # Nova forma de conectar com a IA do Google
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
                # Comando moderno para gerar a resposta
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception:
                st.error("Erro ao conectar com a IA.")
                
