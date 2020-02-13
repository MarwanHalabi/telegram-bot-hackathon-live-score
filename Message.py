#!/usr/bin/python3

from config import *
import requests
from Models import Matches_model
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove


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
            print(x)
        if command.lower().startswith("hi") or command == "/start":
            parse(TOKEN, user_message, start_msg)
        elif command == "List_today_matches":
            print("into list")
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
            print(listOfMatches)
            x = ReplyKeyboardMarkup(listOfMatches, one_time_keyboard=True, resize_keyboard=True)
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

        elif command == "/choose sub type":
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



# commands = {
#     "/start": parse
#     , "/list": parse
#     , "/subscribe": parse
# }


# ###########    here we start    #########
#
# def start(bot, update):
#     update.message.reply_text(main_menu_message(),
#                               reply_markup=main_menu_keyboard())
#
#
# def main_menu(bot, update):
#     query = update.callback_query
#     bot.edit_message_text(chat_id=query.message.chat_id,
#                           message_id=query.message.message_id,
#                           text=main_menu_message(),
#                           reply_markup=main_menu_keyboard())
#
#
# def first_menu(bot, update):
#     query = update.callback_query
#     bot.edit_message_text(chat_id=query.message.chat_id,
#                           message_id=query.message.message_id,
#                           text=first_menu_message(),
#                           reply_markup=first_menu_keyboard())
#
#
# def second_menu(bot, update):
#     query = update.callback_query
#     bot.edit_message_text(chat_id=query.message.chat_id,
#                           message_id=query.message.message_id,
#                           text=second_menu_message(),
#                           reply_markup=second_menu_keyboard())
#
#
# # and so on for every callback_data option
# def first_submenu(bot, update):
#     pass
#
#
# def second_submenu(bot, update):
#     pass
#
#
# ############################ Keyboards #########################################
# def main_menu_keyboard():
#     keyboard = [[InlineKeyboardButton('Option 1', callback_data='m1')],
#                 [InlineKeyboardButton('Option 2', callback_data='m2')],
#                 [InlineKeyboardButton('Option 3', callback_data='m3')]]
#     return InlineKeyboardMarkup(keyboard)
#
#
# def first_menu_keyboard():
#     keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
#                 [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
#                 [InlineKeyboardButton('Main menu', callback_data='main')]]
#     return InlineKeyboardMarkup(keyboard)
#
#
# def second_menu_keyboard():
#     keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
#                 [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
#                 [InlineKeyboardButton('Main menu', callback_data='main')]]
#     return InlineKeyboardMarkup(keyboard)
#
#
# ############################# Messages #########################################
# def main_menu_message():
#     return 'Choose the option in main menu:'
#
#
# def first_menu_message():
#     return 'Choose the submenu in first menu:'
#
#
# def second_menu_message():
#     return 'Choose the submenu in second menu:'
#
#
# ############################# Handlers #########################################
# updater = Updater('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
# updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
# updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
# updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
#                                                     pattern='m1_1'))
# updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
#                                                     pattern='m2_1'))
#
# updater.start_polling()
# ################################################################################
