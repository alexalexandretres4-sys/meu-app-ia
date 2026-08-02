import streamlit as st
import os
import requests

st.set_page_config(page_title="Meu App de IA", page_icon="🤖")
st.title("🤖 Meu Chat com IA")

# Cole a sua chave da Groq que começa com gsk_ aqui dentro das aspas
api_key = "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"

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
            # Conexão direta via API para evitar erros de instalação
            url = "https://groq.com"
            headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
            data = {
                "model": "llama-3.3-70b-specdec",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            response = requests.post(url, json=data, headers=headers).json()
            resposta_ia = response["choices"][0]["message"]["content"]
            
            st.markdown(resposta_ia)
            st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
        except Exception:
            st.error("Erro ao conectar com a IA.")
            
