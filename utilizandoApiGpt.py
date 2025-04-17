"""

chatGPT:
https://openai.com/index/chatgpt/ -> Login; Buscar="API-Keys" e criar uma nova chave. 

api_key = ""

API referencia Doc = https://platform.openai.com/docs/api-reference/introduction; 

# Alguns tipos de requisições: post(enviar info.), get(pegar info.)

# ERRO 401: Falha na solicitação por falta de autenticação.
# EROO 400: Solicitação inválida. 
# ERRO 429: Usuário fez muitas solicitações em pouco tempo
"""

import requests #(pip install) - para fazer requisições
import json #() permite formatar as informações da maneira correta. (linguagem das respostas e requerimentos)

try:
    senha = ""
    #----------------------------------------------------------------------------------------------------------
    # Autentication 
    # link = "https://api.openai.com/v1/models" # Lista de modelos de requisição disponíveis da openia;
    # headers = {"Authorization": f"Bearer {senha}"} # insira a apikey para autenticar; 
    # requisicao = requests.get(link, headers=headers) #Faz a requisição em si. 
    # print(requisicao) # Codigo de requisição; 200 = ok;
    # print(requisicao.text) # printa todos os modelos de IA disponíveis. 
   
    #----------------------------------------------------------------------------------------------------------
    headers = {"Authorization": f"Bearer {senha}", "Content-Type":"application/json"}
    link = "https://api.openai.com/v1/chat/completions" 
    id_modelo_ia = "gpt-4.1"

    body_mensagens = {

        "model":id_modelo_ia,   
        "messages":[{"role": "user", "content": "Me entregue seuquencia de fibonacci" }]

    }

    body_mensagens = json.dumps(body_mensagens) # Conversão do dicionário criado em json. 
    requisicao = requests.post(link, headers=headers, data=body_mensagens)#

    print(requisicao)

except:
    print("ERRO!")




