import os
from dotenv import load_dotenv
import google.generativeai as genai
 
def consultar_gemini(prompt, modelo="gemini-1.5-flash", temperatura=0.7):
    """
    Consulta o Google Gemini usando a API
    
    Gere sua API KEY:
        https://aistudio.google.com/apikey
    Adicione a key no .env
        GEMINI_API_KEY=AIzaAsddzDhb...
    Instale as libs:
        pip install google-generativeai python-dotenv
    """
    try:
        # Carrega variáveis de ambiente
        load_dotenv()
        
        # Obter chave API do ambiente
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            return "Erro: Configure GEMINI_API_KEY no arquivo .env"
        
        # Configura o cliente Gemini
        genai.configure(api_key=api_key)
        
        # Configuração do modelo
        generation_config = {
            "temperature": temperatura,
            "max_output_tokens": 2048,
        }
        
        model = genai.GenerativeModel(
            model_name=modelo,
            generation_config=generation_config
        )
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"Erro na consulta: {str(e)}"
 
def main():
    print("Olá, sou seu assistente virtual pessoal, me pergunte o que quiser e lhe darei a resposta!")
    print("Digite 'sair' para encerrar.\n")
    
    while True:
        pergunta = input("Digite sua pergunta: ").strip()
        
        if not pergunta:
            continue
            
        if pergunta.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando o programa...")
            break
            
        resposta = consultar_gemini(pergunta)
        print("\nGemini:", resposta, "\n")
 
if __name__ == "__main__":
    main()