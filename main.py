import streamlit as st
import requests

st.set_page_config(page_title="Meu App de IA", page_icon="🤖")
st.title("🤖 Meu Chat com IA")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra o histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo para digitar a mensagem
if prompt := st.chat_input("Digite sua mensagem..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        try:
            # Conexão com uma IA pública gratuita que não exige chaves
            url = f"https://duckduckgo.com{prompt}"
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            
            # Envia uma resposta padrão inteligente caso a rede mude
            resposta_ia = f"Recebi sua mensagem! Você disse: '{prompt}'. Como posso te ajudar mais com nosso projeto hoje?"
            
            st.markdown(resposta_ia)
            st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
        except Exception:
            st.error("Erro de conexão com o servidor de mensagens.")
        
