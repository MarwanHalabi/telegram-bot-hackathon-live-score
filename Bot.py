
from datetime import datetime

import requests

import Message
from Models import Matches_model
from config import *


def open_tele():
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)



def send_game_data():
    active_matches = Matches_model.get_subscription_list()
    for match in active_matches:
        score = match["home_team"] + ": " + str(match["home_team_score"]) + ", " + match["visitor_team"] + ": " + str(match["visitor_team_score"])
        for user in match["users"]:
            print("here" + str(user))
            Message.parseSend(TOKEN, str(user), score)


score_counter = 18;
def alter_data():
    global score_counter
    game_result = {"match_id": 1, "last_updated": datetime.now(),
                   "home_team_score": score_counter,
                   "visitor_team_score": 2}
    Matches_model.update_score(game_result)
    score_counter += 2
