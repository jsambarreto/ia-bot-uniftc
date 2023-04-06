from senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type":"application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

def consult_chatgpt(role, content):
    body_message = {
        "model" : id_modelo,
        "messages":[{"role": role, "content": content}]
    }
    body_message = json.dumps(body_message)

    requisicao = requests.post(link, headers=headers, data = body_message)
    print(requisicao)
    resposta = requisicao.json()

    #mensagem = resposta["choices"][0]["message"]["content"]
    return resposta

role = "user"
content = "Ola"
context = f"Você é o Jorge Barreto, professor de uma turma de alunos do curso de sistemas de informação da \
                    UNEX - Centro Universitário de Excelencia e o aluno te passa a seguinte mensagem: {content}. \
                    Responda de forma educada, mas direta, não precisa incluir o nome do aluno da resposta"
print(context)
resposta = "consult_chatgpt(role = role, content=context)"
print(resposta)