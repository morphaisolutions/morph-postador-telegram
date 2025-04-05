import os
import requests
import openai
from dotenv import load_dotenv

load_dotenv()

# Variáveis de ambiente
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Ex: @canaldamorph
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# Gera conteúdo com IA (ajuste o prompt como quiser)
def gerar_conteudo():
    resposta = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é uma IA que gera frases inspiradoras sobre inovação, automação e tecnologia."},
            {"role": "user", "content": "Crie uma frase curta e impactante para o canal da Morph."}
        ]
    )
    return resposta['choices'][0]['message']['content'].strip()

# Posta no Telegram
def postar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": mensagem
    }
    response = requests.post(url, json=payload)
    print(f"Resposta do Telegram: {response.text}")

# Executa
if __name__ == "__main__":
    conteudo = gerar_conteudo()
    postar_telegram(conteudo)