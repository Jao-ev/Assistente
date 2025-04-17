# 📚 **Assistente de IA - Google Gemini**  

**Chatbot utilizando API do Google Gemini!**  

---

## 🚀 **Funcionalidades**  

✔️ **Conversa interativa** com um modelo avançado de IA  
✔️ **Configuração simples** usando variáveis de ambiente  
✔️ **Suporte a diferentes modelos** (Gemini 1.5 Flash, Pro, etc.)  
✔️ **Controle de criatividade** (ajustável via `temperatura`)  
✔️ **Tratamento de erros** robusto  

---

## 📦 **Pré-requisitos**  

- Python 3.8+  
- Conta no [Google AI Studio](https://aistudio.google.com/) (para obter a chave de API)  
- Bibliotecas `google-generativeai`, `python-dotenv`  


---

## ⚙️ **Instalação e Configuração**  

### **1. Clone o repositório**  
```bash
git clone https://github.com/Jao-ev/Assistente.git
cd assistente-gemini
```

### **2. Instale as dependências**  
```bash
pip install google-generativeai python-dotenv
```

### **3. Configure sua chave de API**  
Crie um arquivo `.env` e adicione sua chave:  
```env
GEMINI_API_KEY=sua_chave_aqui
```
🔑 *Obtenha sua chave em [Google AI Studio → API Keys](https://aistudio.google.com/)*  

### **4. Execute o assistente**  
```bash
python main.py
```

---

## 🛠 **Uso Avançado**  

### **Alterando o modelo**  
Edite a função `consultar_gemini` em `main.py`:  
```python
resposta = consultar_gemini(pergunta, modelo="gemini-1.5-pro")  # Modelo avançado
```

### **Ajustando a criatividade**  
Mude a `temperatura` (0 = preciso, 1 = criativo):  
```python
resposta = consultar_gemini(pergunta, temperatura=0.5)  # Equilíbrio entre precisão e criatividade
```

---

## ✨ **Contribuições**  
Contribuições são bem-vindas! Abra uma **issue** ou envie um **PR**.  

---
