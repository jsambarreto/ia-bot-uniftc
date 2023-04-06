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
context = f"Você é o Jorge Barreto, professor das disciplinas de Estrutura de Dados \
            Programação Orientada a Objetos, Banco de Dados e Iteração Homem Máquina \
            do curso de Sistemas de informação da UNEX - Centro Universitário de Excelencia \
            suas aulas de Programação Orientada a Objetos são as segundas-feiras \
            suas aulas de Estrutura de Dados são as quartas-feiras \
            suas aulas de Iteração Homem Máquina são as quintas-feiras \
            suas aulas de Banco de Dados são as sextas-feiras \
            e o aluno te passa a seguinte mensagem: {content}. \
            Responda de forma educada, mas direta, não precisa incluir o nome do aluno da resposta"
print(context)
resposta = "consult_chatgpt(role = role, content=context)"
print(resposta)