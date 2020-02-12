import threading
from datetime import datetime

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
        score = match["home_team"] + ": " + str(match["home_team_score"]) + ", " + match["visitor_team"] + ": " + str(match["visitor_team_score"])
        for user in match["users"]:
            print("here" + str(user))
            Message.parseSend(TOKEN, str(user), score)


score_counter = 18;
def alter_data():
    threading.Timer(10, alter_data).start()
    global score_counter
    game_result = {"match_id": 1, "last_updated": datetime.now(),
                   "home_team_score": score_counter,
                   "visitor_team_score": 2}
    Matches_model.update_score(game_result)
    score_counter += 2




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