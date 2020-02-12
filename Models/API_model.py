from datetime import datetime, date
import requests
from Models import Matches_model

# json_response = {"api": {"status": 200, "message": "GET games\/date\/2020-02-13", "results": 11,
#                          "filters": ["seasonYear", "league", "gameId", "teamId", "date", "live"], "games": [
#         {"seasonYear": "2019", "league": "standard", "gameId": "7196", "startTimeUTC": "2020-02-13T00:00:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "1", "shortName": "ATL", "fullName": "Atlanta Hawks", "nickName": "Hawks",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/e\/ee\/Hawks_2016.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "7", "shortName": "CLE", "fullName": "Cleveland Cavaliers", "nickName": "Cavaliers",
#                    "logo": "", "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7197", "startTimeUTC": "2020-02-13T00:00:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "10", "shortName": "DET", "fullName": "Detroit Pistons", "nickName": "Pistons",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/en\/thumb\/1\/1e\/Detroit_Pistons_logo.svg\/1200px-Detroit_Pistons_logo.svg.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "26", "shortName": "ORL", "fullName": "Orlando Magic", "nickName": "Magic",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/b\/bd\/Orlando_Magic_logo_2010.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7198", "startTimeUTC": "2020-02-13T00:30:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "38", "shortName": "TOR", "fullName": "Toronto Raptors", "nickName": "Raptors",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/8\/89\/Raptors2015.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "4", "shortName": "BKN", "fullName": "Brooklyn Nets", "nickName": "Nets",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/commons\/thumb\/4\/44\/Brooklyn_Nets_newlogo.svg\/130px-Brooklyn_Nets_newlogo.svg.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7199", "startTimeUTC": "2020-02-13T00:30:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "21", "shortName": "MIL", "fullName": "Milwaukee Bucks", "nickName": "Bucks",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/3\/34\/Bucks2015.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "15", "shortName": "IND", "fullName": "Indiana Pacers", "nickName": "Pacers",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/c\/cf\/Pacers_de_l%27Indiana_logo.svg\/1180px-Pacers_de_l%27Indiana_logo.svg.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7200", "startTimeUTC": "2020-02-13T00:30:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "41", "shortName": "WAS", "fullName": "Washington Wizards", "nickName": "Wizards",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/archive\/d\/d6\/20161212034849%21Wizards2015.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "24", "shortName": "NYK", "fullName": "New York Knicks", "nickName": "Knicks",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/d\/dc\/NY_Knicks_Logo_2011.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7201", "startTimeUTC": "2020-02-13T01:00:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled", "vTeam": {"teamId": "29", "shortName": "POR", "fullName": "Portland Trail Blazers",
#                                               "nickName": "Trail Blazers",
#                                               "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/en\/thumb\/2\/21\/Portland_Trail_Blazers_logo.svg\/1200px-Portland_Trail_Blazers_logo.svg.png",
#                                               "score": {"points": ""}},
#          "hTeam": {"teamId": "19", "shortName": "MEM", "fullName": "Memphis Grizzlies", "nickName": "Grizzlies",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/en\/thumb\/f\/f1\/Memphis_Grizzlies.svg\/1200px-Memphis_Grizzlies.svg.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7202", "startTimeUTC": "2020-02-13T01:00:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "5", "shortName": "CHA", "fullName": "Charlotte Hornets", "nickName": "Hornets",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/f\/f3\/Hornets_de_Charlotte_logo.svg\/1200px-Hornets_de_Charlotte_logo.svg.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "22", "shortName": "MIN", "fullName": "Minnesota Timberwolves", "nickName": "Timberwolves",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/d\/d9\/Timberwolves_du_Minnesota_logo_2017.png\/200px-Timberwolves_du_Minnesota_logo_2017.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7203", "startTimeUTC": "2020-02-13T01:30:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "30", "shortName": "SAC", "fullName": "Sacramento Kings", "nickName": "Kings",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/9\/95\/Kings_de_Sacramento_logo.svg\/1200px-Kings_de_Sacramento_logo.svg.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "8", "shortName": "DAL", "fullName": "Dallas Mavericks", "nickName": "Mavericks",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/b\/b8\/Mavericks_de_Dallas_logo.svg\/150px-Mavericks_de_Dallas_logo.svg.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7204", "startTimeUTC": "2020-02-13T02:00:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "11", "shortName": "GSW", "fullName": "Golden State Warriors", "nickName": "Warriors",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/d\/de\/Warriors_de_Golden_State_logo.svg\/1200px-Warriors_de_Golden_State_logo.svg.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "28", "shortName": "PHX", "fullName": "Phoenix Suns", "nickName": "Suns",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/5\/56\/Phoenix_Suns_2013.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7205", "startTimeUTC": "2020-02-13T02:00:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "20", "shortName": "MIA", "fullName": "Miami Heat", "nickName": "Heat",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/1\/1c\/Miami_Heat_-_Logo.svg\/1200px-Miami_Heat_-_Logo.svg.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "40", "shortName": "UTA", "fullName": "Utah Jazz", "nickName": "Jazz",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/3\/3b\/Jazz_de_l%27Utah_logo.png",
#                    "score": {"points": ""}}},
#         {"seasonYear": "2019", "league": "standard", "gameId": "7206", "startTimeUTC": "2020-02-13T03:00:00.000Z",
#          "endTimeUTC": "", "arena": "", "city": "", "country": "", "clock": "", "gameDuration": "",
#          "currentPeriod": "0\/4", "halftime": "", "EndOfPeriod": "", "seasonStage": "2", "statusShortGame": "1",
#          "statusGame": "Scheduled",
#          "vTeam": {"teamId": "17", "shortName": "LAL", "fullName": "Los Angeles Lakers", "nickName": "Lakers",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/commons\/thumb\/3\/3c\/Los_Angeles_Lakers_logo.svg\/220px-Los_Angeles_Lakers_logo.svg.png",
#                    "score": {"points": ""}},
#          "hTeam": {"teamId": "9", "shortName": "DEN", "fullName": "Denver Nuggets", "nickName": "Nuggets",
#                    "logo": "https:\/\/upload.wikimedia.org\/wikipedia\/fr\/thumb\/3\/35\/Nuggets_de_Denver_2018.png\/180px-Nuggets_de_Denver_2018.png",
#                    "score": {"points": ""}}}]}}


def get_today_games(day_date: date = date.today().strftime("%y-%m-%d")):
    api_response = requests.get('https://api-nba-v1.p.rapidapi.com/games/date/{}'.format(day_date))
    if api_response.status_code == 200:
        json_response = api_response.json()
    games_response = json_response["api"]["games"]
    for game in games_response:
        game_details = {"home_team": game["hTeam"]["fullName"], "visitor_team": game['vTeam']["fullName"],
                        "start_time": game["startTimeUTC"], "match_id": game["gameId"],
                        "day_date": datetime.date()}
        Matches_model.add_match(game_details)


def get_live_score():
    live_games = Matches_model.get_live_matches()
    if live_games and live_games.len():
        api_response = requests.get('https://api-nba-v1.p.rapidapi.com/games/live/')
        if api_response.status_code == 200:
            json_response = api_response.json()
    games_response = json_response["api"]["games"]
    for game in games_response:
        if game['game_id'] in live_games:
            game_result = {"match_id": game["gameId"], "last_updated": datetime.now(),
                           "home_team_score": game["hTeam"]["score"]["points"],
                           "visitor_team_score": game["vTeam"]["score"]["points"]}
            Matches_model.update_score(game_result)
