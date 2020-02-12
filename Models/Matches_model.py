from Models.sql_helper import insert_to_DB, delete_from_DB, get_data_from_DB
from datetime import datetime


def add_match(match_details):
    query = "insert into matches (match_id,home_team,visitor_team,start_time,day_date,match_status) values ({},\"{}\",\"{}\",\"{}\",\"{}\",{})".format(
        match_details["match_id"], match_details["home_team"],
        match_details["visitor_team"],
        match_details["start_time"],
        match_details["day_date"],
        match_details["match_status"])
    print(query)
    insert_to_DB(query)


def get_today_matches():
    today_date = datetime.today().strftime('%Y-%m-%d')
    query = "select match_id,home_team,visitor_team,start_time from matches where day_date = \"{}\"".format(today_date)
    return get_data_from_DB(query)


def add_match_subscription(match_id, user_id):
    query = "insert into match_subscription (user_id,match_id) values ({},{})".format(user_id, match_id)
    print(query)
    insert_to_DB(query)


def remove_match_subscription(match_id, user_id):
    query = "delete from match_subscription where match_subscription.user_id = {} and match_subscription.match_id = {}".format(user_id,match_id)
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



match_details = {"match_id": 10, "home_team": "sokor", "visitor_team": "sho3la",
                 "start_time": datetime.today().strftime('%Y-%m-%d %H:%M'),
                 "day_date": datetime.today().strftime('%Y-%m-%d'), "match_status": 0}

match_details2 = {"match_id": 40, "home_team": "Wathba", "visitor_team": "Al_sa7a",
                  "start_time": "2020-02-12 20:30:30",
                  "day_date": datetime.today().strftime('%Y-%m-%d'), "match_status": 0}

# print(match_details2)

# add_match(match_details2)
# add_match(match_details)
# add_match_subscription(10, 50)
# add_match_subscription(10, 100)
# add_match_subscription(40,30)
print(get_subscription_list())
