import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Mh081263",
    db="league",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

keyboard = [
    ["List_today_matches"], ["subscribe_for_match"], ["Unsubscribe"], ["Mute"], ["Help"], ["Cancel"]
]

port_number = 5002
TOKEN = '1090092876:AAFsH_CxLromgssfNqHMIVt27uQmqTRD_gA'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://55a6e4fa.ngrok.io/message' \
    .format(TOKEN)

start_msg = "Hi!! I'm Sport Bee \U0001F41D, How are you doing today? \n" \
            "I'll try to make your live easier by sending you minute by minute updates for game score \n" \
            "To start just type \"start\"! easy enough right \U0001F609"

help = "Hello, Need help? " \
       "\ncheck the following commands " \
       "\n\"Hi\": say hi to me and I'll say it back :) " \
       "\n\"start\": get a friendly list of my commands instead of typing them" \
       "\n\"list_all_matches\": Displays all NBA games for today. " \
       "\n\"Subscribe_for_match\": Enable notifications for a cretain game scores. " \
       "\n\"Unsubscribe\": disable notifications for a cretain game scores. " \
       "\n\"Cancel\": exit the services window. "

# list_of_matches_msg = "id<123> BHC vs RMA\nid<432> INR vs IMC\nid<432> ROM vs NFC"

subscribe = "you just subscribed to {} match"
unsubscribe = "you just unsubscribed to {} match"

