from config import *
import requests
from Models import Matches_model



# import telegram


def message(user_message):
    try:
        messageL = user_message['text'].split()
        print(messageL)
        command = messageL[0]
        user_id = user_message['chat']['id']
        print(user_id)
        if command == "/start":
            parse(TOKEN, user_message, start_msg)
        elif command == "/list":
            print("into list")
            list_of_matches = Matches_model.get_today_matches()
            parse(TOKEN, user_message, match_show(list_of_matches))
        elif command == "/subscribe":
            Matches_model.add_match_subscription(messageL[1], user_id)
            parse(TOKEN, user_message, subscribe_msg(messageL[1]))
        elif command == "/unsubscribe":
            Matches_model.remove_match_subscription(messageL[1], user_id)
            parse(TOKEN, user_message, unsubscribe_msg(messageL[1]))
        elif command == "/list_all_teams":
            list_of_teams = Matches_model.get_teams()
            parse(TOKEN, user_message, teams_show(list_of_teams))
        elif command == "/add_to_favorite":
            Matches_model.add_to_favorite(user_id,messageL[1:])
            parse(TOKEN, user_message, "favorite list updated")
        elif command == "/remove_from_favorite":
            Matches_model.remove_from_favorite(user_id, messageL[1:])
            parse(TOKEN, user_message, "favorite list updated")
        elif command == "/show_favorite_teams":
            teams_list = Matches_model.get_user_favorite(user_id)
            parse(TOKEN, user_message, fav_teams(teams_list))
        elif command == "/choose sub type":
            pass
    except:
        pass





# def UI():
#     button_list = [
#         InlineKeyboardButton("col1", callback_data=...),
#         InlineKeyboardButton("col2", callback_data=...),
#         InlineKeyboardButton("row 2", callback_data=...)
#     ]
#     reply_markup = InlineKeyboardMarkup(util.build_menu(button_list, n_cols=2))
#     bot.send_message(..., "A two-column menu", reply_markup=reply_markup)


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


def fav_teams(list_of_teams):
    teamList = ''
    for item in list_of_teams:
        teamList += item
        teamList += '\n'
    teamList += ""
    return teamList


def teams_show(list_of_teams: list):
    teamList = ""
    for item in list_of_teams:
        teamList += item["team_name"]
        teamList += '\n'
    teamList += ""
    return teamList


def make_match(item: dict):
    return str(item["match_id"]) + "    " + item["home_team"] + "  VS  " + item["visitor_team"] \
           + "   start time: " + item["start_time"].strftime("%m/%d/%Y, %H:%M:%S") + "\n"

# commands = {
#     "/start": parse
#     , "/list": parse
#     , "/subscribe": parse
# }
