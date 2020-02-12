import threading

import requests

import Message
from config import *
from Models import Matches_model


def open_tele():
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)


def send_game_data():
    threading.Timer(10, send_game_data).start()
    active_matches = Matches_model.get_subscription_list()
    for match in active_matches:
        score = match["home_team"] + ": " + match["home_team_score"] + ", " + match["visitor_team"] + ": " + match["visitor_team_score"]
        for user in match["users"]:
            Message.parse(TOKEN, user, score)




#
# def fill_database():
#     Matches_model.add_match({"match_id": "123", "home_team": "Al sokor", "visitor_team": "team2"
#                                 , "start_time": "11/12/2020 12:00", "day_date": "11/12/2020", "match_status": 1})
#     Matches_model.add_match({"match_id": "111", "home_team": "name1", "visitor_team": "team2"
#                                 , "start_time": "11/12/2020 12:00", "day_date": "11/12/2020", "match_status": 1})
#     Matches_model.add_match({"match_id": "435", "home_team": "name1", "visitor_team": "team2"
#                                 , "start_time": "11/12/2020 12:00", "day_date": "11/12/2020", "match_status": 1})
#     Matches_model.add_match({"match_id": "911", "home_team": "name1", "visitor_team": "team2"
#                                 , "start_time": "11/12/2020 12:00", "day_date": "11/12/2020", "match_status": 1})