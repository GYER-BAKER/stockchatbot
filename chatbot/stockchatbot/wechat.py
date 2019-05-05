from wxpy import *
from chatbot import Chatbot
chatbots={}

def start_wechat_server(interpreter):
    bot=Bot()
    
    @bot.register()
    def reply_messages(msg):
        print(msg)
        sender=msg.sender
        global chatbots
        if sender in chatbots:
            sender.send(chatbots[sender].respond(msg.text))
        else:
            chatbot=Chatbot(interpreter)
            chatbots[sender]=chatbot
            sender.send(chatbot.greet())
        
    @bot.register(msg_types=FRIENDS)
    def auto_accept_friends(msg):
        new_friend = msg.card.accept()
        new_friend.send('I am a finance-chatbot. What can I do for you?')

    bot.join()


if __name__ == '__main__':
    start_wechat_server(None)