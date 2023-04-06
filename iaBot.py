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
        #chat_id = message['message']['chat']['id']
        content = message
        context = f"Você é o Jorge Barreto, professor de uma turma de alunos do curso de sistemas de informação da \
                    UNEX - Centro Universitário de Excelencia e o aluno te passa a seguinte mensagem: {message}. \
                    Responda de forma educada, mas direta, não precisa incluir o nome do aluno da resposta"
        resposta =  consult_chatgpt(role = role, content=context)
        bot.reply_to(message,resposta)
          
    bot.polling()
