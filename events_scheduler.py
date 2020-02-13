import sched
import time
import Message
from Models import Matches_model, API_model
from config import TOKEN

# API_model.get_teams()
s = sched.scheduler(time.time, time.sleep)


def send_game_data():
    active_matches = Matches_model.get_subscription_list()
    for match in active_matches:
        score = "\U0001F3C0 " + match["home_team"] + ": " + str(match["home_team_score"]) + ", " + match["visitor_team"] + ": " + \
                str(match["visitor_team_score"]) + " \U0001F3C0"
        for user in match["users"]:
            print(str(user) + " " + str(match["match_id"]))
            Message.parseSend(TOKEN, str(user), score)
    print("here send")
    s.enter(60, 1, send_game_data, ())


# def alter_data():
#     global score_counter
#     game_result = {"match_id": 1, "last_updated": datetime.now(),
#                    "home_team_score": score_counter,
#                    "visitor_team_score": 2}
#     Matches_model.update_score(game_result)
#     game_result = {"match_id": 2, "last_updated": datetime.now(),
#                    "home_team_score": (score_counter + 4),
#                    "visitor_team_score": 6}
#     Matches_model.update_score(game_result)
#     score_counter += 2
#     print("here alter")
#     s.enter(30, 1, alter_data, ())
#

def schedual_api_calls():
    API_model.get_live_score()
    print("api call")
    s.enter(60, 1, schedual_api_calls, ())


# s.enter(0, 1, alter_data, ())
s.enter(0, 1, schedual_api_calls, ())
s.enter(10, 1, send_game_data, ())
s.run()
