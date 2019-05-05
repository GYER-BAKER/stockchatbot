from rasa_nlu.model import Interpreter
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from wechat import wechat_server
from chatbot import symbol_load
import sys


def main():
    interpreter = Interpreter.load("./models/current/nlu")
    symbol_load()
    print('Model successfully loaded.')
   
    wechat_server(interpreter)



if __name__ == '__main__':
    main()
    