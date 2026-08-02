import streamlit as st

st.set_page_config(page_title="Meu App de IA", page_icon="🤖")
st.title("🤖 Meu Chat com IA")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra o histórico de conversas na tela
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de texto para digitar
if prompt := st.chat_input("Digite sua mensagem..."):
    # Mostra o texto que o usuário enviou
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Resposta inteligente instantânea sem precisar de chaves ou internet externa
    with st.chat_message("assistant"):
        texto_usuario = prompt.lower().strip()
        
        # O próprio app escolhe a melhor resposta
        if "oi" in texto_usuario or "olá" in texto_usuario:
            resposta_ia = "Olá! Eu sou a Inteligência Artificial do seu aplicativo próprio. Como posso te ajudar hoje?"
        elif "tudo bem" in texto_usuario:
            resposta_ia = "Tudo ótimo por aqui! E com você? É muito bom ver nosso aplicativo funcionando direto do celular!"
        elif "nome" in texto_usuario:
            resposta_ia = "Eu sou o seu assistente virtual pessoal, criado por você no seu Moto G82!"
        else:
            resposta_ia = f"Entendi perfeitamente o que você disse! Você escreveu: '{prompt}'. Estou pronto para continuar desenvolvendo esse app com você!"
        
        st.markdown(resposta_ia)
        st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
        
