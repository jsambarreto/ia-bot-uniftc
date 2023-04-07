import telebot
#import config
import os
from datetime import date, datetime,tzinfo,timedelta
from unidecode import unidecode
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore
import json
import random
from consult_chatgpt import consult_chatgpt
from utils.zone import Zone as zn
from senha import token

tk = token
if __name__ == "__main__":
    bot = telebot.TeleBot(tk, parse_mode=None) 

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Olá!")
            
    @bot.message_handler(func=lambda m: True)
    def echo(message):
        role = "user"
        chat_id = message.from_user.username
        content = message
        context = f"Você é o Jorge Barreto, professor das disciplinas de Estrutura de Dados \
            Programação Orientada a Objetos, Banco de Dados e Iteração Homem Máquina \
            do curso de Sistemas de informação da UNEX - Centro Universitário de Excelencia \
            as aulas de Programação Orientada a Objetos são as segundas-feiras \
            e usamos a linguagem Java \
            as aulas de Estrutura de Dados são as quartas-feiras \
            e usamos a linguagem Javascript \
            as aulas de Iteração Homem Máquina são as quintas-feiras \
            as aulas de Banco de Dados são as sextas-feiras \
            e o aluno te passa a seguinte mensagem: {content}. \
            Responda de forma educada, mas direta, não precisa incluir o nome do aluno na resposta."
        resposta =  consult_chatgpt(role = role, content=context)
        bot.reply_to(message,resposta)
          
    bot.polling()
