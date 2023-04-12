#from senha import API_KEY
import requests
import json
import os

headers = {"Authorization": f"Bearer {os.environ['API_KEY']}", "Content-Type":"application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

def consult_chatgpt(role, content):
    body_message = {
        "model" : id_modelo,
        "messages":[{"role": role, "content": content}]
    }
    body_message = json.dumps(body_message)

    requisicao = requests.post(link, headers=headers, data = body_message)
    #print(requisicao)
    resposta = requisicao.json()

    mensagem = resposta["choices"][0]["message"]["content"]
    return mensagem

