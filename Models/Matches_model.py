from Models.sql_helper import insert_to_DB, delete_from_DB, get_data_from_DB
from datetime import datetime, date
import Message


def add_match(match_details):
    query = "insert into matches (match_id,home_team,visitor_team,start_time,day_date,match_status) " \
            "values ({},\"{}\",\"{}\",\"{}\",\"{}\",{})".format(
        match_details["match_id"], match_details["home_team"],
        match_details["visitor_team"],
        match_details["start_time"],
        match_details["day_date"],
        match_details["match_status"])
    insert_to_DB(query)
    status_query = 'insert into match_status (match_id, home_team_score, visitor_team_score, last_updated, `CHANGED`)' \
                   ' VALUES ({},{},{},"{}",{})'.format(match_details["match_id"], 0, 0, datetime.now(), 0)
    insert_to_DB(status_query)


def get_today_matches(today_date: date = date.today().strftime("%Y-%m-%d")):
    # today_date = datetime.today().strftime('%Y-%m-%d')
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
            match_sub = {"match_id": match["match_id"]}

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


def send_final_score(match_id):
    query = "SELECT favorite_teams.user_id,matches.home_team, matches.visitor_team, match_status.home_team_score, match_status.visitor_team_score, favorite_teams.team_name FROM " \
            "match_status,matches,favorite_teams WHERE matches.match_id = {} AND match_status.match_id = matches.match_id AND ( favorite_teams.team_name =  matches.home_team" \
            " OR favorite_teams.team_name = matches.visitor_team )".format(match_id, match_id)
    print(query)
    Message.send_final_scores_msg(get_data_from_DB(query))


def update_score(match_status):
    query = "SELECT * FROM match_status WHERE match_id = {}".format(match_status["match_id"])
    result = get_data_from_DB(query)[0]
    if str(result["home_team_score"]) != str(match_status["home_team_score"]) \
            or str(result["visitor_team_score"]) != str(match_status["visitor_team_score"]):
        update_query = 'UPDATE `match_status` SET `home_team_score` = {}, ' \
                       '`visitor_team_score` = {}, `last_updated` = "{}", `CHANGED` = {} WHERE `match_id` = {}'. \
            format(match_status["home_team_score"], match_status["visitor_team_score"], datetime.now(), True,
                   match_status["match_id"])
        insert_to_DB(update_query)


def add_team(team_details):
    query = "INSERT INTO Teams(team_id,team_name,team_nickname,team_logo) values ({},\"{}\",\"{}\",\"{}\")".format(
        team_details["team_id"], team_details["team_name"], team_details["team_nickname"], team_details["team_logo"])
    insert_to_DB(query)


def get_teams():
    query = "Select team_name,team_nickname,team_logo from teams"
    return get_data_from_DB(query)


def add_to_favorite(user_id, team):
    query = "INSERT INTO favorite_teams(team_name,user_id) VALUES (\"{}\",{})".format(team, user_id)
    insert_to_DB(query)


def remove_from_favorite(user_id, team_list):
    for team in team_list:
        query = "DELETE FROM favorite_teams WHERE team_name = \"{}\" and user_id = {}".format(team, user_id)
        delete_from_DB(query)


def get_user_favorite(user_id):
    teams_list = []
    query = "SELECT team_name FROM favorite_teams WHERE user_id = {}".format(user_id)
    teams = get_data_from_DB(query)
    for team in teams:
        teams_list.append(team["team_name"])
    return teams_list


def get_user_matches(user_id):
    query = "select matches.match_id,matches.home_team,matches.visitor_team,matches.start_time,matches.day_date " \
            "FROM matches,match_subscription " \
            "where match_subscription.user_id = {} and matches.match_id = match_subscription.match_id".format(user_id)
    return get_data_from_DB(query)


def get_team_subscribers(team_name):
    users_id_list = []
    query = "SELECT user_id FROM favorite_teams WHERE team_name = \"{}\"".format(team_name)
    users = get_data_from_DB(query)
    for user in users:
        users_id_list.append(user["user_id"])
    return users_id_list


def end_game(match_id):
    update_query = 'UPDATE `matches` SET `matches`.`match_status` = {} ' \
                   'WHERE `match_id` = {}'.format(1, match_id)
    insert_to_DB(update_query)
