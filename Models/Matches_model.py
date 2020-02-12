from Models.sql_helper import insert_to_DB


def add_match(match_id,team_one ,start_time):
    query = "insert into today_matches (match_id,start_time) values ({},{})".format(match_id,start_time)
    insert_to_DB(query)





