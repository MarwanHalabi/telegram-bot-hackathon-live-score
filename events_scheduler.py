from datetime import datetime
import sched
import time

import Message
from Models import Matches_model
from config import TOKEN


score_counter = 18;
s = sched.scheduler(time.time, time.sleep)


def send_game_data():
    active_matches = Matches_model.get_subscription_list()
    for match in active_matches:
        score = match["home_team"] + ": " + str(match["home_team_score"]) + ", " + match["visitor_team"] + ": " + str(match["visitor_team_score"])
        for user in match["users"]:
            Message.parseSend(TOKEN, str(user), score)
    print("here send")
    s.enter(30, 1, send_game_data, ())


def alter_data():
    global score_counter
    game_result = {"match_id": 1, "last_updated": datetime.now(),
                   "home_team_score": score_counter,
                   "visitor_team_score": 2}
    Matches_model.update_score(game_result)
    score_counter += 2
    print("here alter")
    s.enter(30, 1, alter_data, ())


s.enter(0, 1, alter_data, ())
s.enter(10, 1, send_game_data, ())
s.run()
