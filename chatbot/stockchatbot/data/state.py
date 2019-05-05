from iexfinance import Stock
from random import choice

#keys
STOCK_LIST='stock_list'
STOCK_NAME='stock_name'
START_TIME='start_time'
END_TIME='end_time'
USER='user'

#state
STATE_INIT=0
STATE_USER=1
STATE_SEARCH=2
STATE_FINISHED=3

#intent
INTENT_GREET='greet'
INTENT_GOODBYE='goodbye'
INTENT_SEARCH='search'
INTENT_SEARCH_VOLUME='search_volume'
INTENT_SEARCH_OPEN_PRICE='search_open'
INTENT_SEARCH_CLOSE_PRICE='search_close'
INTENT_SEARCH_INTEREST='search_interest'
INTENT_SEARCH_HISTORY='search_history'
INTENT_SPECIFY_TIME='specify_time'
INTENT_AFFIRM='affirm'
INTENT_DENY='deny'
INTENT_CANCEL='cancel'
INTENT_ADD_FAVORATE='add_favorate'
INTENT_GET_FAVORATE='get_favorate'
INTENT_LOGIN='login'
INTENT_LOGOUT='logout'
INTENT_ADD_STOCK='add_stock'

#name
ENTITY_COMPANY='company'
ENTITY_STOCK='stock'

def handler_init(keys):
    templates=[]

def hander_greet(keys):
    template=[
        'Hello! ',
        'Hi.',
        'How are you. '
    ]
    text=choice(template)
    text+='You can ask me for stock information, such as price, volume, interest. '
    return text

def handler_login(keys):
    raise NotImplementedError

def handler_logout(keys):
    template=[
        'Log out. Bye.'
    ]
    return choice(template)


def handler_get_history(keys):
    raise NotImplementedError

def handler_get_price(keys):
    template=[
        'The real-time price of {0} is {1}. ',
        '{0}\' price is {1} now. '
    ]
    text=""
    for stock_name in keys[STOCK_LIST]:
        value=Stock(stock_name).get_price()
        text+=choice(template).format(stock_name,value)
    text+='I also know volume, open price or interest. :)'
    return text

def handler_get_volume(keys):
    template=[
        'The volume of {0} is {1}. ',
        'Current volume of {0} is {1}. ',
        '{0} is {1}. ',
        '{0}\' volume is {1}. '
    ]
    text=""
    if len(keys[STOCK_LIST])==1:
        template.append('{1}.')
    for stock_name in keys[STOCK_LIST]:
        value=Stock(stock_name).get_volume()
        text+=choice(template).format(stock_name,value)
    return text

def handler_get_open_price(keys):
    template=[
        'The open price of {0} is {1}. ',
        'Today\'s open price of {0} is {1}. ',
        '{0}\' open price is {1}. ',
    ]
    text=""
    if len(keys[STOCK_LIST])==1:
        template.append('{1}.')
        template.append( 'Today is {1}. ')
    for stock_name in keys[STOCK_LIST]:
        value=Stock(stock_name).get_open()
        text+=choice(template).format(stock_name,value)
    return text
    

def handler_get_interest(keys):
    template=[
        'The short interest of {0} is {1}. ',
        'Today\'s short interest of {0} is {1}. ',
        '{0}\' short interest is {1}. ',
    ]
    text=""
    if len(keys[STOCK_LIST])==1:
        template.append('{1}.')
    for stock_name in keys[STOCK_LIST]:
        value=Stock(stock_name).get_short_interest()
        text+=choice(template).format(stock_name,value)
    return text

def handler_get_close_price(keys):
    raise NotImplementedError

def handler_deny(keys):
    return "OK."

def handler_affirm(keys):
    return "OK."


# precondition,handler
PROPERTY_OF_ACTION={
    INTENT_LOGIN:([USER],handler_login),
    INTENT_SEARCH_HISTORY:([STOCK_LIST,START_TIME,END_TIME],handler_get_history),
    INTENT_SEARCH:([STOCK_LIST,],handler_get_price),
    INTENT_SEARCH_VOLUME:([STOCK_LIST,],handler_get_volume),
    INTENT_SEARCH_OPEN_PRICE:([STOCK_LIST,],handler_get_open_price),
    INTENT_SEARCH_CLOSE_PRICE:([STOCK_LIST,],handler_get_close_price),
    INTENT_SEARCH_INTEREST:([STOCK_LIST,],handler_get_interest),
    INTENT_GREET:([],hander_greet),
    INTENT_LOGOUT:([],handler_logout),
    INTENT_DENY:([],handler_deny),
    INTENT_AFFIRM:([],handler_affirm)
}

ASK_FOR_INFORMATION={
    STOCK_LIST:['Which stock do you want to know?',],
    START_TIME:['Start from when?',],
    END_TIME:['End to when?',],
    USER:['You need to input your USERNAME for further operation.',]
}


POLICY={
    (STATE_INIT,INTENT_GREET):STATE_INIT,
    (STATE_INIT,INTENT_LOGIN):STATE_USER,
    (STATE_INIT,INTENT_LOGIN):STATE_USER,
    (STATE_USER,INTENT_SEARCH):STATE_SEARCH

}