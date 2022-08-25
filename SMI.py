#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message
import time
#arts names
n1 = '╔═╗╔═╦╗╔╗╔╗╔═╗'
n2 = '║╬║║║║║╚╗╔╝║╬║' 
n3 = '║╗╣║║║║╔╝╚╗║╔╝'
n4 = '╚╩╝╚╩═╝╚╝╚╝╚╝─ '
#colors

BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
    #vars
print(YELLOW)
nmr = int(input('Digite A Quantidade  Ininity '))
    
#tela carregamento
print('\033[1;93m')
print('╔═╗────╔╗╔╗───  ')
print('║╬║╔═╦╗╚╗╔╝╔═╗  ')
print('║╗╣║║║║╔╝╚╗║╬║  ')
print('╚╩╝╚╩═╝╚╝╚╝║╔╝  ')
print('───────────╚╝─  ')
print('\033[1;91m')
print('─────█─▄▀█──█▀▄─█──')
time.sleep(0.3)
print('────▐▌──────────▐▌──')
time.sleep(0.3)
print('────█▌▀▄──▄▄──▄▀▐█──')
time.sleep(0.3)
print('───▐██──▀▀──▀▀──██▌──')
time.sleep(0.3)
print('──▄████▄──▐▌──▄████▄─')

time.sleep(1)
print('\033[1;92m')
def enviar_email():  
    corpo_email = """
    <p>┏━┓ ┏━┓
┏┯┯┯┯┯┓
┠┼┼┼┼┼┨
┗┷┷┷┷┷┛
hahahahaha<p>─────█─▄▀█──█▀▄─█──
────▐▌──────────▐▌──
────█▌▀▄──▄▄──▄▀▐█──
───▐██──▀▀──▀▀──██▌──
──▄████▄──▐▌──▄████▄─</p>
    """
    msg = email.message.Message()
    msg['Subject'] = '° ᭄° ᭄𝑨𝑻𝑨𝑪𝑲 𝑺𝑷𝑨𝑴 𝑩𝑨𝑵 ㄔ𖤍𖠂𖠄𒀱° ᭄𒀱𒋨𓅂𒁂𒁂° ᭄𐂡𒈞𒈒𒁂𒅒'
    msg['From'] = 'rnmailfrom.dev' #< Seu email aqui
    print(RED)
    msg['To'] = 'emailexample@rn.dev' #< email pra quem deseja enviar
    print(CYAN)
    print('┈┈┈╭━━╮┈┈┈┈┈┈',n1)
    time.sleep(0.2)
    print('┈┈╭╯┊◣╰━━━━╮┈┈',n2)
    time.sleep(0.2)
    print('┈┈┃┊┊┊╱▽▽▽┛┈┈',n3)
    time.sleep(0.2)
    print('┈┈┃┊┊┊▏┈┈┈┈┈┈',n4)
    time.sleep(0.2)
    print('━━╯┊┊┊╲△△△┓┈┈')
    time.sleep(0.2)
    print('┊┊┊┊╭━━━━━━╯┈┈')
    password = 'kozkteqlohrzgfyw' #< digite aq a senha do seu email
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(GREEN, '🔴Email enviado', YELLOW, 'Para', msg['To'])
    print(CYAN, '🔴Email Numero 👉', n)
    print(MAGENTA, '🔴QUANTIDADE DE EMAILS A SEREM ENVIADOS🔵', nmr)

# In[ ]:


for n in range(0, nmr):
 enviar_email()
