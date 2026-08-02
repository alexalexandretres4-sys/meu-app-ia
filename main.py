import streamlit as st
import random

st.set_page_config(page_title="Meu App de IA Super Avançado", page_icon="🎬", layout="wide")

# Inicializa as variáveis na memória do celular
if "messages" not in st.session_state:
    st.session_state.messages = []
if "series" not in st.session_state:
    st.session_state.series = {}

# MENU LATERAL - MODO GERADOR DE SÉRIES (IGUAL À ZOPIA)
with st.sidebar:
    st.header("🎬 Criador de Séries")
    st.write("Crie sua própria série de TV com episódios!")
    
    nome_serie = st.text_input("Nome da sua Série:", placeholder="Ex: Os Viajantes do Tempo")
    tema_serie = st.text_area("Sobre o que é a série?", placeholder="Ex: Três amigos encontram um relógio antigo que abre portais...")
    
    if st.button("🚀 Criar Nova Série", use_container_width=True):
        if nome_serie and tema_serie:
            st.session_state.series[nome_serie] = {
                "tema": tema_serie,
                "episodios": []
            }
            st.success(f"Série '{nome_serie}' criada com sucesso! Agora peça os episódios no chat.")
        else:
            st.warning("Preencha o nome e o tema para criar a série!")

    if st.session_state.series:
        st.write("---")
        st.subheader("📺 Suas Séries Criadas:")
        for s_nome in st.session_state.series.keys():
            st.info(f"**{s_nome}** ({len(st.session_state.series[s_nome]['episodios'])} episódios)")

# TELA PRINCIPAL - CHAT DE IA AVANÇADO
st.title("🤖 Chat de IA & Criador de Histórias")

# Mostra o histórico de mensagens, roteiros, imagens e músicas na tela
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        
        # Garante a exibição correta dos elementos salvos no histórico
        if "image" in msg:
            st.write("---")
            st.subheader("🎬 Visualização da Cena (Estilo Cinema Realista)")
            st.image(msg["image"], caption="Cena do episódio gerada por Inteligência Artificial", use_container_width=True)
        if "audio" in msg:
            st.audio(msg["audio"])

# Campo de texto para enviar comandos
if prompt := st.chat_input("Digite uma mensagem ou peça: 'Crie o episódio 1 da minha série'"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        texto_usuario = prompt.lower().strip()
        
        # Sistema Avançado de Roteiro que força a imagem e música a aparecerem
        if "episódio" in texto_usuario or "episodio" in texto_usuario or "série" in texto_usuario:
            if st.session_state.series:
                ultima_serie = list(st.session_state.series.keys())[-1]
                num_ep = len(st.session_state.series[ultima_serie]["episodios"]) + 1
                
                resposta_texto = f"""
### 🎬 **Série:** {ultima_serie}  
🍿 **Episódio {num_ep}:** O Início da Jornada  

**[Cena 1 - Introdução]:** As luzes mudam para um tom dramático de cinema. O cenário se baseia na sua história: *"{st.session_state.series[ultima_serie]['tema']}"*.  
**[Roteiro & Diálogos]:**  
- **Moça Pobre:** "Eu não posso me casar com ele... meu coração pertence a outro!"  
- **Pai Autoritário:** "Você não tem escolha! Esse casamento vai salvar nossa família!"  

**[Gancho de Novela]:** A porta se abre bruscamente e o namorado secreto observa tudo escondido. A música sobe com força.  

*Dica: Digite 'Crie o próximo episódio' para continuar a história!*
"""
                # Links públicos e estáveis que funcionam direto no Android/Chrome
                semente = random.randint(1, 999999)
                link_foto = f"https://pollinations.ai{semente}"
                link_musica = "https://w3schools.com"
                
                st.markdown(resposta_texto)
                st.write("---")
                st.subheader("🎬 Visualização da Cena (Estilo Cinema Realista)")
                st.image(link_foto, caption="Cena do episódio gerada por Inteligência Artificial", use_container_width=True)
                st.audio(link_musica)
                
                # Salva tudo junto na memória do chat para não sumir ao atualizar
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": resposta_texto,
                    "image": link_foto,
                    "audio": link_musica
                })
                st.session_state.series[ultima_serie]["episodios"].append(resposta_texto)
            else:
                resposta_ia = "Você ainda não criou nenhuma série no menu lateral! Preencha o nome e o tema lá na esquerda primeiro."
                st.markdown(resposta_ia)
                st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
        
        # Respostas Normais do Chat
        elif "oi" in texto_usuario or "olá" in texto_usuario:
            resposta_ia = "Olá! Agora estou no Modo Cinema Avançado. Cadastre a série no menu lateral e depois peça o episódio aqui no chat!"
            st.markdown(resposta_ia)
            st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
        else:
            resposta_ia = f"Estou pronto para criar novas cenas! Ative o menu lateral para gerar roteiros completos."
            st.markdown(resposta_ia)
            st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
            
