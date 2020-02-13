#!/usr/bin/python3

from config import *
import requests
from Models import Matches_model
from telegram import ReplyKeyboardMarkup


def message(user_message):
    try:
        messageL = user_message['text'].split()
        print(messageL)
        command = messageL[0]
        user_id = user_message['chat']['id']
        print(user_id)
        if command == "start":
            x = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "please choose your selection", x.to_json()))

        if command.lower().startswith("hi") or command == "/start":
            parse(TOKEN, user_message, start_msg)

        elif command == "List_today_matches":
            list_of_matches = Matches_model.get_today_matches()
            parse(TOKEN, user_message, match_show(list_of_matches))

        elif command == "subscribe_for_match":
            listOfMatches = [[str(item['match_id']) + "    " + item["home_team"] + "  VS  " + item["visitor_team"]]
                             for item in Matches_model.get_today_matches()]
            x = ReplyKeyboardMarkup(listOfMatches, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "subscribe to match", x.to_json()))

        elif command == "Unsubscribe":
            matches = Matches_model.get_user_matches(user_id)
            listOfMatches = [[str(item['match_id']) + "    " + item["home_team"] + "  Vs  " + item["visitor_team"]]
                             for item in matches]
            x = ReplyKeyboardMarkup(listOfMatches, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "Unsubscribe to match", x.to_json()))
        elif command == "Subscribe_future_matches":
            x = ReplyKeyboardMarkup(this_week, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "Unsubscribe to match", x.to_json()))
        elif command == "Help":
            parse(TOKEN, user_message, help)

        elif messageL[3] == "VS":
            parse(TOKEN, user_message, subscribe_msg(messageL[0]))
            Matches_model.add_match_subscription(messageL[0], user_id)

        elif messageL[3] == "Vs":
            Matches_model.remove_match_subscription(messageL[0], user_id)
            parse(TOKEN, user_message, unsubscribe_msg(messageL[0]))

        elif command == "choose sub type":
            pass
    except:
        pass


def parse(token, user_message, parse_input):
    res = requests.get(
        "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
            .format(token, user_message['chat']['id'], parse_input))


def parseSend(token, user_message, parse_input):
    res = requests.get(
        "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
            .format(token, user_message, parse_input))


def subscribe_msg(match_id):  # unsubscribe
    return subscribe.format(match_id)


def unsubscribe_msg(match_id):
    return unsubscribe.format(match_id)


def match_show(list_of_matches: list):
    matchList = ""
    for item in list_of_matches:
        matchList += make_match(item)
    matchList += ""
    return matchList


def make_match(item: dict):
    return "Game: " + str(item["match_id"]) + "\n" + item["home_team"] + "   \U0001F19A   " + item["visitor_team"] \
           + "\n" + "start at: " + item["start_time"].strftime("%H:%M") + "\n\n"
