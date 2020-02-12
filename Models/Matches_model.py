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
    query = "delete from match_subscription where match_subscription.user_id = {} and match_subscription.match_id = {}".format(
        int(user_id), int(match_id))
    insert_to_DB(query)


def get_subscription_list():
    lis_of_match_details = []
    match_sub = {}
    current_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    get_id_query = "select match_subscription.match_id from match_subscription,matches,match_status where " \
                   "matches.start_time <= \"{}\" " \
                   "and matches.match_id = match_subscription.match_id and matches.match_id = match_status.match_id " \
                   "and match_status.`CHANGED` = {} GROUP BY match_subscription.match_id".format(current_date, True)
    live_matches = get_data_from_DB(get_id_query)
    if live_matches:
        for match in live_matches:
            match_sub["match_id"] = match["match_id"]

            match_details_query = "select matches.home_team,matches.visitor_team,match_status.home_team_score,match_status.visitor_team_score FROM" \
                                  " matches, match_status WHERE matches.match_id = {}  AND match_status.match_id = {}".format(
                match["match_id"], match["match_id"])

            match_details = get_data_from_DB(match_details_query)

            for matches in match_details:
                match_sub["home_team"] = matches["home_team"]
                match_sub["visitor_team"] = matches["visitor_team"]
                match_sub["home_team_score"] = matches["home_team_score"]
                match_sub["visitor_team_score"] = matches["visitor_team_score"]

            users_list = []
            get_users_query = "SELECT match_subscription.user_id from match_subscription WHERE match_subscription.match_id = {}".format(
                match["match_id"])

            users = get_data_from_DB(get_users_query)
            for user in users:
                users_list.append(user["user_id"])
            match_sub["users"] = users_list
            lis_of_match_details.append(match_sub)
        update_query = "UPDATE `match_status` SET `CHANGED` = {}".format(False)
        insert_to_DB(update_query)
    return lis_of_match_details


def get_live_matches():
    query = 'SELECT * FROM `matches` WHERE `start_time` < "{}" AND `match_status` = {} AND EXISTS (' \
            'SELECT 1 from `match_subscription` where `match_subscription`.`match_id` = `matches`.`match_id`) ' \
            ''.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 0)
    return get_data_from_DB(query)


def update_score(match_status):
    query = "SELECT * FROM match_status WHERE match_id = {}".format(match_status["match_id"])
    result = get_data_from_DB(query)[0]
    if result["home_team_score"] != match_status["home_team_score"] \
            or result["visitor_team_score"] != match_status["visitor_team_score"]:
        update_query = 'UPDATE `match_status` SET `home_team_score` = {}, ' \
                       '`visitor_team_score` = {}, `last_updated` = "{}", `CHANGED` = {} WHERE `match_id` > 0'. \
            format(match_status["home_team_score"], match_status["visitor_team_score"], datetime.now(), True)
        insert_to_DB(update_query)


match_details = {"match_id": 10, "home_team": "sokor", "visitor_team": "sho3la",
                 "start_time": datetime.today().strftime('%Y-%m-%d %H:%M'),
                 "day_date": datetime.today().strftime('%Y-%m-%d'), "match_status": 0}

# add_matches(match_details)
# get_today_matches()


match_details2 = {"match_id": 40, "home_team": "Wathba", "visitor_team": "Al_sa7a",
                  "start_time": "2020-02-12 20:30:30",
                  "day_date": datetime.today().strftime('%Y-%m-%d'), "match_status": 0}

# get_today_matches()
# print(match_details2)

# add_match(match_details2)
# add_match(match_details)
# add_match_subscription(10, 50)
# add_match_subscription(10, 100)
# add_match_subscription(40,30)
# print(get_subscription_list())
