import streamlit as st

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

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite uma mensagem ou peça: 'Crie o episódio 1 da minha série'"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        texto_usuario = prompt.lower().strip()
        
        # Sistema Avançado de IA Local (Gera histórias automáticas sem precisar de chaves)
        if "episódio" in texto_usuario or "episodio" in texto_usuario or "série" in texto_usuario:
            # Encontra a última série criada
            if st.session_state.series:
                ultima_serie = list(st.session_state.series.keys())[-1]
                num_ep = len(st.session_state.series[ultima_serie]["episodios"]) + 1
                
                resposta_ia = f"""
### 🎬 **Série:** {ultima_serie}  
🍿 **Episódio {num_ep}:** O Início da Jornada  

**[Cena 1 - Introdução]:** As luzes piscam. O cenário se baseia na sua ideia de: *"{st.session_state.series[ultima_serie]['tema']}"*.  
**[Roteiro & Diálogos]:**  
- **Personagem 1:** "Vocês viram aquilo? Não pode ser real..."  
- **Personagem 2:** "Calma, precisamos registrar isso antes que desapareça!"  

**[Gancho para o próximo episódio]:** Uma sombra misteriosa aparece ao fundo antes da tela cortar para os créditos pretos.  

*Dica: Digite 'Crie o próximo episódio' para continuar a história!*
"""
                st.session_state.series[ultima_serie]["episodios"].append(resposta_ia)
            else:
                resposta_ia = "Você ainda não criou nenhuma série no menu lateral! Preencha o nome e o tema lá na esquerda primeiro para eu gerar os episódios."
        
        # Respostas Normais do Chat
        elif "oi" in texto_usuario or "olá" in texto_usuario:
            resposta_ia = "Olá! Agora estou no Modo Super Avançado com Gerador de Séries. Use o menu lateral para começar a criar!"
        elif "tudo bem" in texto_usuario:
            resposta_ia = "Tudo excelente! Nosso aplicativo agora tem as funções da Zopia. O que vamos criar hoje?"
        else:
            resposta_ia = f"Processando ideia... '{prompt}'. Estou pronto para transformar essa mensagem em uma cena ou roteiro de série!"
        
        st.markdown(resposta_ia)
        st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
                
