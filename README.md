# Drapion

Drapion is a simple python library for parsing web API's

# Installation

```
python setup.py install
```

# Usage

Using Drapion with Telegram Bot API

```Python
from drapion import Drapion

bot = Drapion('https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/')

res = bot.getMe() # will create a object with the response from
                  # https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
                  # Let's say this is the response
                  # {
                  #   "ok":true,
                  #   "result":{
                  #     "id":111111111,
                  #     "is_bot":true,
                  #     "first_name":"examplebot",
                  #     "username":"examplebot"
                  #   }
                  # }

if res.ok:
  info = res.result
  
  info.id        # 111111111
  info.is_bot    # True
  info.first_name # 'examplebot'
  info.username  # 'examplebot'
  
bot.sendMessage(chat_id='@example', text='Sample') # calls /sendMessage?chat_id=@example&text=Sample
                                                   # returns a object from json response
```
