from config import *
import requests


def message(user_message):
    try:
        messageL = user_message['text'].split()
        print(messageL)
        command = messageL[0]
        if command == "/start":
            parse(TOKEN, user_message, start_msg)
        elif command == "/list":
            parse(TOKEN, user_message, match_show(list_of_matches))
        elif command == "/subscribe":
            parse(TOKEN, user_message, subscribe_msg(messageL[1]))
    except:
        pass


def parse(token, user_message, parse_input):
    res = requests.get(
        "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
            .format(token, user_message['chat']['id'], parse_input))


def subscribe_msg(match_id):
    return subscribe.format(match_id)


def match_show(list_of_matches: list):
    matchList = ""
    for item in list_of_matches:
        matchList += make_match(item)
    return matchList


def make_match(item: dict):
    return item["match_id"] + "    " + item["home_team"] + "  VS  " + item["visitor_team"] \
           + "   start time: " + item["start_time"] + "\n"
