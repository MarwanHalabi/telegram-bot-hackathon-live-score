from Models.sql_helper import insert_to_DB, delete_from_DB, get_data_from_DB
from datetime import datetime


def add_match(match_details):
    query = "insert into matches (match_id,home_team,visitor_team,start_time,day_date,match_status) values ({},\"{}\",\"{}\",\"{}\",\"{}\",{})".format(
        match_details["match_id"], match_details["home_team"],
        match_details["visitor_team"],
        match_details["start_time"],
        match_details["day_date"],
        match_details["match_status"])
    insert_to_DB(query)


def get_today_matches():
    today_date = datetime.today().strftime('%Y-%m-%d')
    query = "select match_id,home_team,visitor_team,start_time from matches where day_date = \"{}\"".format(today_date)
    return get_data_from_DB(query)


def add_match_subscription(match_id, user_id):
    query = "insert into match_subscription (user_id,match_id) values ({},{})".format(int(user_id), int(match_id))
    insert_to_DB(query)


def remove_match_subscription(match_id, user_id):
    query = "delete from match_subscription where match_subscription.user_id = {} and match_subscription.match_id = {}".format(int(user_id), int(match_id))
    insert_to_DB(query)


def get_subscription_list():
    match_sub = {}
    current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    get_id_query = "select match_subscription.match_id from match_subscription,matches where matches.start_time <= \"{}\" " \
                   "and matches.match_id = match_subscription.match_id".format(
        current_date)
    live_matches = get_data_from_DB(get_id_query)
    for match in live_matches:
        users_list = []
        get_users_query = "SELECT match_subscription.user_id from match_subscription WHERE match_subscription.match_id =  \"{}\"".format(
            match["match_id"])
        users = get_data_from_DB(get_users_query)
        for user in users:
            users_list.append(user["user_id"])
        match_sub[match["match_id"]] = users_list

    return match_sub



def get_live_matches():
    query = 'SELECT * FROM `matches` WHERE `start_time` < "{}" AND `match_status` = {} AND EXISTS (' \
            'SELECT 1 from `match_subscription` where `match_subscription`.`match_id` = `matches`.`match_id`) ' \
            ''.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 0)
    return get_data_from_DB(query)


def update_score(match_status):
    query = "SELECT * FROM match_status WHERE match_id = {}".format(match_status["match_id"])
    result = get_data_from_DB(query)
    if result["home_team_score"] != match_status["home_team_score"] \
            or result["visitor_team_score"] != match_status["visitor_team_score"]:
        update_query = "UPDATE `match_status` SET `home_team_score` = '{}', " \
                       "`visitor_team_score` = '{}', `last_updated` = {}, `CHANGED` = {}".\
            format(match_status["home_team_score"], match_status["visitor_team_score"], datetime.now(), True)
    insert_to_DB(update_query)


