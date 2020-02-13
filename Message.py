from config import *
import requests
from Models import Matches_model, API_model
from telegram import ReplyKeyboardMarkup


def message(user_message):
    try:
        general_teams_list = [sub['team_name'] for sub in Matches_model.get_teams()]
        messageL = user_message['text'].split()
        print(messageL)
        command = messageL[0]
        user_id = user_message['chat']['id']
        print(user_id)
        if user_message['text'].lower() == "menu":
            x = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "What do you like to do\U00002753", x.to_json()))

        if command.lower().startswith("hi") or command == "/start":
            parse(TOKEN, user_message, start_msg)

        elif user_message['text'].lower() == "list today matches":
            list_of_matches = Matches_model.get_today_matches()
            parse(TOKEN, user_message, match_show(list_of_matches))

        elif user_message['text'].lower() == "list all teams":
            list_of_teams = Matches_model.get_teams()
            parse(TOKEN, user_message, teams_show(list_of_teams))

        elif user_message['text'].lower() == "add to favorite":
            fav_teams = [[item["team_name"]] for item in Matches_model.get_teams()]
            x = ReplyKeyboardMarkup(fav_teams, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "please choose your selection", x.to_json()))

        elif user_message['text'] in general_teams_list:
            Matches_model.add_to_favorite(user_id, user_message['text'])
            parse(TOKEN, user_message, "favorite list updated")

        elif command == "remove_from_favorite":
            Matches_model.remove_from_favorite(user_id, messageL[1:])
            parse(TOKEN, user_message, "favorite list updated")

        elif user_message['text'].lower() == "my favorite teams":
            result = "\n".join(Matches_model.get_user_favorite(user_id))
            parse(TOKEN, user_message, "Here are your current favorite teams: \n" + result)

        elif user_message['text'].lower() == "subscribe for match":
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

        elif user_message['text'].lower() == "subscribe future matches":
            x = ReplyKeyboardMarkup(this_week, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "Unsubscribe to match", x.to_json()))

        elif len(command.split("-")) == 3:
            API_model.get_today_games(command)
            listOfMatches = [[str(item['match_id']) + "    " + item["home_team"] + "  VS  " + item["visitor_team"]]
                             for item in Matches_model.get_today_matches(command)]
            x = ReplyKeyboardMarkup(listOfMatches, one_time_keyboard=True, resize_keyboard=True)
            requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&reply_markup={}"
                         .format(TOKEN, user_id, "subscribe to match", x.to_json()))

        elif command.lower().startswith("help"):
            parse(TOKEN, user_message, help)

        elif "VS" in messageL:
            parse(TOKEN, user_message, subscribe_msg(messageL[0]))
            Matches_model.add_match_subscription(messageL[0], user_id)

        elif "Vs" in messageL:
            Matches_model.remove_match_subscription(messageL[0], user_id)
            parse(TOKEN, user_message, unsubscribe_msg(messageL[0]))

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
    return "Game: " + str(item["match_id"]) + "\n" + item["home_team"] + "   \U0001F19A   " + item["visitor_team"] \
           + "\n" + "start at: " + item["start_time"].strftime("%H:%M") + "\n\n"


def get_winning_team(obj):
    if obj["home_team_score"] > obj["visitor_team_score"]:
        return obj["home_team"]
    else:
        return obj["visitor_team"]


def send_final_scores_msg(data):
    for obj in data:
        winning = get_winning_team(obj)
        score = "\U0001F3C0 " + obj["home_team"] + ": " + str(obj["home_team_score"]) + ", " + obj[
            "visitor_team"] + ": " + \
                str(obj["visitor_team_score"]) + " \U0001F3C0"
        if winning == obj["team_name"]:
            score += "\n\U0001F973 " + obj["team_name"] + "HAS WON!!!! \U0001F973"
        else:
            score += "\n\U0001F624 well... you can't win them all \U0001F624"
        parseSend(TOKEN, obj["user_id"], score)
