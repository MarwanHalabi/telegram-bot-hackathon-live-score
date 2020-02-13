from datetime import datetime, date
import requests
from Models import Matches_model
import dateutil.parser


def get_today_games(day_date: date = date.today().strftime("%Y-%m-%d")):
    api_response = requests.get('https://api-nba-v1.p.rapidapi.com/games/date/{}'.format(day_date),
                                headers={"x-rapidapi-host": "api-nba-v1.p.rapidapi.com",
                                         "x-rapidapi-key": "5c516b2a70msh137afc3cb1fbc89p1b4a45jsndc2d8a4ec944"})
    if api_response.status_code == 200:
        json_response = api_response.json()
        games_response = json_response["api"]["games"]
        for game in games_response:
            game_details = {"home_team": game["hTeam"]["fullName"], "visitor_team": game['vTeam']["fullName"],
                            "start_time": dateutil.parser.parse(game["startTimeUTC"]).strftime("%Y-%m-%d %H:%M:%S"), "match_id": game["gameId"],
                            "day_date": dateutil.parser.parse(game["startTimeUTC"]).strftime("%Y-%m-%d"), "match_status": 0}
            Matches_model.add_match(game_details)


def get_live_score():
    live_games = Matches_model.get_live_matches()
    if live_games and len(live_games):
        api_response = requests.get('https://api-nba-v1.p.rapidapi.com/games/live/',
                                    headers={"x-rapidapi-host": "api-nba-v1.p.rapidapi.com",
                                             "x-rapidapi-key": "5c516b2a70msh137afc3cb1fbc89p1b4a45jsndc2d8a4ec944"})
        if api_response.status_code == 200:
            json_response = api_response.json()
            games_response = json_response["api"]["games"]

            for curr_game in live_games:
                found = False
                for game in games_response:
                    if str(game['gameId']) == str(curr_game['match_id']):
                        game_result = {"match_id": game["gameId"], "last_updated": datetime.now(),
                                       "home_team_score": game["hTeam"]["score"]["points"],
                                       "visitor_team_score": game["vTeam"]["score"]["points"]}
                        Matches_model.update_score(game_result)
                        found = True

                if not found:
                    api_response = requests.get(
                        'https://api-nba-v1.p.rapidapi.com/games/gameId/{}'.format(str(curr_game['match_id'])),
                        headers={"x-rapidapi-host": "api-nba-v1.p.rapidapi.com",
                                 "x-rapidapi-key": "5c516b2a70msh137afc3cb1fbc89p1b4a45jsndc2d8a4ec944"})
                    if api_response.status_code == 200:
                        json_response_game = api_response.json()
                        one_game_response = json_response_game["api"]["games"][0]
                        game_end_result = {"match_id": one_game_response["gameId"], "last_updated": datetime.now(),
                                           "home_team_score": one_game_response["hTeam"]["score"]["points"],
                                           "visitor_team_score": one_game_response["vTeam"]["score"]["points"]}
                        Matches_model.update_score(game_end_result)
                        Matches_model.end_game(curr_game['match_id'])
                        Matches_model.send_final_score(curr_game['match_id'])


def get_teams():
    leagues_list = ["standard", "africa", "sacramento", "vegas", "utah", "orlando"]
    for league in leagues_list:
        api_response = requests.get('https://api-nba-v1.p.rapidapi.com/teams/league/{}'.format(league),
                                    headers={"x-rapidapi-host": "api-nba-v1.p.rapidapi.com",
                                             "x-rapidapi-key": "5c516b2a70msh137afc3cb1fbc89p1b4a45jsndc2d8a4ec944"})
        if api_response.status_code == 200:
            json_response = api_response.json()
            teams = json_response["api"]["teams"]
            for t in teams:
                team_data = {"team_id": t["teamId"], "team_name": t["fullName"],
                             "team_nickname": t["nickname"],
                             "team_logo": t["logo"]}
                Matches_model.add_team(team_data)
