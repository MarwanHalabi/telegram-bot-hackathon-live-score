import requests
from config import *
from Models import Matches_model


def open_tele():
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)

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