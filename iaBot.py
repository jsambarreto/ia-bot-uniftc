import telebot
#import config
import os
from datetime import date, datetime
from unidecode import unidecode
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import random

FB = json.loads(os.environ.get('FIREBASE_CREDENTIALS', None))

cred = credentials.Certificate(FB)
firebase_admin.initialize_app(cred)

db = firestore.client()
inc = 0
tk = os.environ.get('token', None)
if __name__ == "__main__":
    bot = telebot.TeleBot(tk, parse_mode=None) 
    def saudacao():
        hora = datetime.now().strftime('%H:%M')
        if '00:00' <= hora <= '12:00':
            saudacao = "Bom dia!"
        elif '12:01' <= hora <= '18:00':
            saudacao = "Boa tarde!"
        else: 
            saudacao = "Boa noite!"
        return saudacao
    
    def incremento():
        inc =+ 1
        return inc

    def verifica_acc():
        data_acc_1 = datetime.strptime("23/08/2021",'%d/%m/%Y')#.strftime('%d/%m/%Y')
        data_acc_2 = datetime.strptime("06/09/2021",'%d/%m/%Y')#.strftime('%d/%m/%Y')
        if data_acc_1 <= datetime.now() <= data_acc_2:
            return 'ACC 1 disponivel'
        else:
            return 'ACC 1 nao disponivel'
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Olá!")
            
    @bot.message_handler(func=lambda m: True)
    def echo(message):
        sauda = saudacao()
        acc_resposta = verifica_acc()
        # Para facilitar a utilizacao do Bot remova espaços, acentos e coloque toda a frase em uppercase
        #Bloco de saudacao
        if message.text.upper().find('OLA')!=-1:
            bot.reply_to(message, sauda)
        elif message.text.upper().find('OI')!=-1:
            bot.reply_to(message, sauda)
        elif message.text.upper().replace(' ','').find('BOMDIA')!=-1:
            bot.reply_to(message, sauda)    
        elif message.text.upper().replace(' ','').find('BOATARDE')!=-1:
            bot.reply_to(message, sauda) 
        elif message.text.upper().replace(' ','').find('BOANOITE')!=-1:
            bot.reply_to(message, sauda)    
        elif unidecode(message.text).replace(' ','').upper().find('QUEMEVOCE')!=-1:
            bot.reply_to(message, sauda +' Sou o bot em treinamento dos alunos de IA da UniFTC turma 2021.2')
        
        #Bloco de zoeira    
        elif message.text.upper().find('JAVA')!=-1:
            bot.reply_to(message, 'Java é lento!')
        elif message.text.upper().find('PYTHON')!=-1:
            bot.reply_to(message, 'Python é vida!')
        elif message.text.upper().find('NOTA')!=-1:
            bot.reply_to(message, 'Sua nota eh voce quem faz!')
        elif message.text.upper().find('GABARITO')!=-1:
            bot.reply_to(message, 'Isso nao eh uma boa ideia jovem.')
        elif message.text.upper().find('PESCA')!=-1:
            bot.reply_to(message, 'Pesca so de peixe!.')
        elif message.text.upper().find('COLA')!=-1:
            bot.reply_to(message, 'Cola so para grudar coisas.')
        elif message.text.upper().find('PHP')!=-1:
            bot.reply_to(message, 'Ai, ai... Nem digo nada sobre isso.')
        
        #Bloco de respostas aos alunos
        elif message.text.upper().find('PROVA') and message.text.upper().find('DATA')!=-1:
            bot.reply_to(message, sauda + ' A data de nossa prova será 04/10/21')
        elif message.text.upper().find('PROVA') and message.text.upper().find('ASSUNTO')!=-1:
            bot.reply_to(message, sauda + ' Os assuntos da VA1 serão: Conceitos de IA, Sistemas Especialistas e Estatistica para IA')
        elif message.text.upper().find('PROVA') and message.text.upper().find('CAI')!=-1:
            bot.reply_to(message, sauda + ' Os assuntos da VA1 serão: Conceitos de IA, Sistemas Especialistas e Estatistica para IA')
        elif message.text.upper().find('PROVA') and message.text.upper().find('HORARIO')!=-1:
            bot.reply_to(message, sauda + ' A prova estara disponivel a partir das 18:50 do dia 04/10 ate as 18:50 do dia 05/10.')
        elif message.text.upper().find('DISPOSICAO') and message.text.upper().find('BAIXA')!=-1:
            bot.reply_to(message, sauda + ' Tome um cafe, veja um programa de 20 minutos do que voce gosta, depois venha estudar!')
        elif message.text.upper().find('PROVA')!=-1:
            bot.reply_to(message, sauda + ' Qual a duvida sobre a prova?')
        #Respostas acc
        elif (message.text.upper().find('ACC'))!=-1:
            bot.reply_to(message, acc_resposta)
            
        #Bloco sem respostas
        else:
            inc = random.randint(0, 999999999)
            print(unidecode(message.text).upper())
            doc_ref = db.collection(u'naorespondidas').document(u'palavra')
            doc_ref.set({
                str(inc):message.text
            })
            
            bot.reply_to(message, sauda + ' Estou em fase de treinamento, ainda não sei responder sobre isso, passe mensagem para o professor!')   

    bot.polling()
