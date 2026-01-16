# 🤖 FátimaAI Chatbot

**FátimaAI Chatbot** é um chatbot inteligente desenvolvido em **Python** como parte da **Jornada Python da Hashtag Treinamentos**. O projeto utiliza **Streamlit** para criação da interface conversacional e integração com **IA generativa (Google Gemini)**, proporcionando uma experiência de chat moderna, interativa e intuitiva.

---

## ✨ Funcionalidades

* 💬 Interface de chat interativa com Streamlit
* 🧠 Integração com IA generativa (Google Gemini)
* 🗂️ Histórico de conversas com `session_state`
* 🎨 Interface personalizada em tons de rosa e branco
* 🚀 Execução simples e rápida

---

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Streamlit**
* **Google Generative AI (Gemini)**
* **HTML/CSS (customização via Streamlit)**

---

## 📂 Estrutura do Projeto

```text
fatima-ai-chatbot/
│
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação
```

---

## ▶️ Como Executar o Projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/alvesmariadefatima/fatima-ai-chatbot.git
cd fatima-ai-chatbot
```

### 2️⃣ Crie e ative um ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure sua API Key

No arquivo `app.py`, substitua:

```python
genai.configure(api_key="SUA_API_KEY_AQUI")
```

Por sua chave da API do Google Gemini.

---

### 5️⃣ Execute a aplicação

```bash
streamlit run app.py
```

Acesse no navegador:
👉 `http://localhost:8501`

---

## 🎯 Objetivo do Projeto

Este projeto tem como objetivo praticar e consolidar conhecimentos em:

* Desenvolvimento de aplicações com **Python**
* Criação de interfaces com **Streamlit**
* Consumo de **APIs de IA generativa**
* Organização de projetos para **portfólio profissional**

---

⭐ Se você gostou do projeto, não esqueça de deixar uma estrela no repositório!
