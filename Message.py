from config import *
import requests


def message(user_message):
    messageL = user_message['text'].split()
    print(messageL)
    command = messageL[0]
    if command == "/start":
        # msg = parse(messageL[1])
        res = requests.get(
            "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                .format(TOKEN, user_message['chat']['id'], start_msg))
    elif command == "/list":
        res = requests.get(
            "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                .format(TOKEN, user_message['chat']['id'], list_of_matches_msg))
    elif command == "/subscribe":
        res = requests.get(
            "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
                .format(TOKEN, user_message['chat']['id'], subscribe_msg(messageL[1])))


def parse(parse_input):
    return parse_input
