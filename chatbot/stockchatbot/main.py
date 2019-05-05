from rasa_nlu.model import Interpreter
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from wechat import start_wechat_server
from chatbot import load_symbols
import sys


def main():
    interpreter = Interpreter.load("./models/current/nlu")
    print('Model successfully loaded.')
    load_symbols()
   
    start_wechat_server(interpreter)



if __name__ == '__main__':
    main()
    