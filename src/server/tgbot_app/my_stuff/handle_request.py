from src.server.setupConfig import bot

def handle(request_body):
    chat_id = request_body['message']['chat']['id']
    bot.sendMessage(chat_id, 'hello')