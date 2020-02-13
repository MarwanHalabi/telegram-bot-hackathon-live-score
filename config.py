import pymysql
import datetime

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Mh081263",
    db="league",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

keyboard = [
    ["List today matches"], ["Subscribe for match"],["Subscribe future matches"], ["Unsubscribe"]
    , ["List all teams"], ["Add to favorite"], ["My favorite teams"], ["Help\U00002753"], ["Cancel"]
]

this_week = [[str((datetime.datetime.today() + datetime.timedelta(days=i)))[0:10]]for i in range(7)]

print(this_week)
port_number = 5002

TOKEN = '1090092876:AAFsH_CxLromgssfNqHMIVt27uQmqTRD_gA'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://dea76ff0.ngrok.io/message' \
    .format(TOKEN)

start_msg = "Hi!! I'm Sport Bee \U0001F41D, How are you doing today? \n" \
            "I'll try to make your live easier by sending you minute by minute updates for game score \n" \
            "To start just type \"menu\"! easy enough right \U0001F609"

help = "Hello, Need help? just type \"menu\" and start talking to me" \
       "\nor else you can check these following commands " \
       "\n\n- \"Hi\": Say hi to me and I'll say it back \U0001F600 " \
       "\n\n- \"menu\": Get a friendly list of my commands instead of typing them" \
       "\n\n- \"List today matches\": Displays all NBA games for today. " \
       "\n\n- \"Subscribe for match\": Enable notifications for a certain game during the day scores. " \
       "\n\n- \"Subscribe future matches\": Enable notifications for a game in the next week." \
       "\n\n- \"Unsubscribe\": Disable notifications for a certain game scores. " \
       "\n\n- \"List all teams\": Show a list of all teams we track." \
       "\n\n- \"Add to favorite\": Add a team to your favorite list." \
       "\n\n- \"Cancel\": Exit the selection list. "


subscribe = "you just subscribed to {} match"
unsubscribe = "you just unsubscribed to {} match"
