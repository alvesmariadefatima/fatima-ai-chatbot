import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import NotFound

# =============================
# CONFIGURAÇÃO DA API
# =============================
genai.configure(api_key="SUA_API_CHAVE_AQUI")

# =============================
# FUNÇÃO: obter modelo válido
# =============================
def obter_modelo_gemini():
    for model in genai.list_models():
        if "generateContent" in model.supported_generation_methods:
            return genai.GenerativeModel(model.name)
    return None

modelo_gemini = obter_modelo_gemini()

if not modelo_gemini:
    st.error("Nenhum modelo Gemini disponível para generateContent.")
    st.stop()

# =============================
# INTERFACE
# =============================
st.title("🤖 FátimaAI")

# =============================
# HISTÓRICO
# =============================
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibe histórico
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# =============================
# INPUT DO USUÁRIO
# =============================
mensagem_usuario = st.chat_input("Digite sua mensagem")

if mensagem_usuario:
    # Salva mensagem do usuário
    st.session_state["lista_mensagens"].append({
        "role": "user",
        "content": mensagem_usuario
    })

    st.chat_message("user").write(mensagem_usuario)

    # Histórico somente como texto (Gemini aceita lista)
    historico = [m["content"] for m in st.session_state["lista_mensagens"]]

    try:
        resposta = modelo_gemini.generate_content(historico)
        resposta_texto = resposta.text

    except NotFound:
        resposta_texto = "⚠️ Modelo indisponível no momento. Tente novamente."

    except Exception as e:
        resposta_texto = f"⚠️ Erro ao gerar resposta: {e}"

    # Salva resposta da IA
    st.session_state["lista_mensagens"].append({
        "role": "assistant",
        "content": resposta_texto
    })

    st.chat_message("assistant").write(resposta_texto)