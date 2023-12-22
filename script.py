from telethon.sync import TelegramClient
from telethon.tl import types
import time
import os

api_id = "" # Insira o seu ID da api telegram entre as aspas
api_hash = "" # Insira a sua hash da api telegram entre as aspas

grupo_origem = 0 # Digite a ID do grupo que deseja clonar
grupo_destino = 0 # Digite a ID do grupo clonado

tamanho_lote = 10000
msg_enviada = 0

def escreverCache(txt):
    with open("mensagemIdCache", "w") as cache:
        cache.write(str(txt))

def lerCache():
    with open("mensagemIdCache", "r") as cache:
        return int(cache.read())

if not os.path.exists("mensagemIdCache"):
    escreverCache(0)

while True:
    try:
        with TelegramClient('clonarCanais', api_id, api_hash) as usuario:
            # Seleciona a mensagem
            msg = usuario.get_messages(grupo_origem, limit=1, reverse=True, offset_id = lerCache())[0]
            msg_atual = msg.id
            escreverCache(msg_atual)
            if not isinstance(msg, types.MessageService) and hasattr(msg, 'media') and (isinstance(msg.media, types.MessageMediaDocument) or isinstance(msg.media, types.MessageMediaPhoto)):
                usuario.forward_messages(grupo_destino, msg)
                print(msg.id)
                #msg_enviada += 1
                #if msg_enviada % 1999 == 0: 
                #    msg_enviada = 0
                #    time.sleep(2000)
    except Exception as erro:
        print(f"ERRO: {erro}")
        time.sleep(120)
