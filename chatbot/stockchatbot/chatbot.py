from iexfinance import get_available_symbols
from data.state import *
import re

avai_symbol=[]
ENTITY='entity'
VALUE='value'
PENDING='pending'
INTENT='intent'
NAME='name'
CONFIDENCE='confidence'
ENTITIES='entities'
HANDLER='handler'
PRECONDITION='precondition'


def symbol_load():
    global avai_symbol
    stocks=get_available_symbols()
    for stock in stocks:
        avai_symbol.append(stock['symbol'])
    print('Symbols successfully loaded.')


def symbol_var(symbols):
    va=[]
    inva=[]
    for symbol in symbols:
        if symbol in avai_symbol:
            va.append(symbol)
        else:
            inva.append(symbol)
    return va, inva

class Chatbot:
    def __init__(self,interpreter):
        print('New chatbot created.')
        self.interpreter=interpreter
        self.state=STATE_INIT
        self.keys={
            PENDING:False
            }

    def respond(self,msg):
        print('User: {}'.format(msg))
        reply_msg=self.normal_nlp(msg)
        print('Bot : {}'.format(reply_msg))
        return reply_msg

    def get_state(self):
        self.state

    def process(self,msg):
        self.normal_nlp(msg)


    def normal_nlp(self,msg):
        nlp_result=self.interpreter.parse(msg)
        u_intent=nlp_result[INTENT][NAME]        
        user_stocks=[]
        for enti in  nlp_result[ENTITIES]:
            if enti[ENTITY]==ENTITY_STOCK:
                user_stocks.append(enti[VALUE])
            else:
                self.keys[enti[ENTITY]]=str(enti[VALUE])
        
        re_stock=re.findall("[-|A-Z]{2,8}",msg)
        user_stocks.extend(re_stock)
        precondition,handler=PROPERTY_OF_ACTION[u_intent]
        va,inva=symbol_var(user_stocks)
        if len(inva)>0:
            if (not self.keys[PENDING]):
                    self.keys[PENDING]=True
                    self.keys[HANDLER]=handler
                    self.keys[PRECONDITION]=precondition
            return "The {} seems inva. Please give me the right symbol.".format(" ".join(inva))

        if len(va)>0:
            self.keys[STOCK_LIST]=user_stocks

        if self.keys[PENDING]:
            precondition=self.keys[PRECONDITION]
            handler=self.keys[HANDLER]

        for key in precondition:
            if not key in self.keys:
                if (not self.keys[PENDING]):
                    self.keys[PENDING]=True
                    self.keys[HANDLER]=handler
                    self.keys[PRECONDITION]=precondition
                return choice(ASK_FOR_INFORMATION[key])
        
        self.keys[PENDING]=False

        return handler(self.keys)



    def greet():
        return "Welcome, I am a finance-chatbot. What can I do for you?"

        
        
        