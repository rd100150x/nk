import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKN = info['CHANNEL_ACCESS_TOKN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text="Guten Morgen! \n Wie gehts dir?")
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()