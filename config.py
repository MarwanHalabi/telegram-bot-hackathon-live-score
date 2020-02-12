import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="league",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


port_number = 5002
TOKEN = '1090954125:AAHA-WX4zsCnVr9pcm2nRXuwuuXDqaM1cQA'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://55a6e4fa.ngrok.io/message' \
    .format(TOKEN)
