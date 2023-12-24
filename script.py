from telethon.sync import TelegramClient
from telethon.tl import types
import time
import os

api_id = "22420244"
api_hash = "6b3c34d32dd4156f5c159470190fb1cc"

grupo_origem = -1001276169293
grupo_destino = -4040633986

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
            escreverCache(msg.id)
            # Envia apenas se houver um tipo de midia anexado
            if not isinstance(msg, types.MessageService) and hasattr(msg, 'media') and (isinstance(msg.media, types.MessageMediaDocument) or isinstance(msg.media, types.MessageMediaPhoto)):
                usuario.forward_messages(grupo_destino, msg)
                print(msg.id)
    except Exception as erro:
        print(f"ERRO: {erro}")
        time.sleep(120)