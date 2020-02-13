import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="league",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

keyboard = [
    ["List_today_matches"], ["subscribe_for_match"], ["Unsubscribe"], ["Mute"], ["Help"], ["Cancel"]
]

port_number = 5002
TOKEN = '1090954125:AAHA-WX4zsCnVr9pcm2nRXuwuuXDqaM1cQA'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://55a6e4fa.ngrok.io/message' \
    .format(TOKEN)

start_msg = "hello dear user.\n Sport league bot provides you important updates about your favorite matches " \
            "instantaneously as they occur (live).\nThe bot saves the data about users like favorite teams" \
            ", subscriptions etc in a database. \nEvery user can talk to the bot and ask for services" \
            ", by the following commands as described below.\n /list:\n /subscribe {match_id}\n/unsubscribe {match_id}"

# list_of_matches_msg = "id<123> BHC vs RMA\nid<432> INR vs IMC\nid<432> ROM vs NFC"

subscribe = "you just subscribed to {} match"
unsubscribe = "you just unsubscribed to {} match"

