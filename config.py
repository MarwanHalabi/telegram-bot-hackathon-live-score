import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    db="sql_intro",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

port_number = 5002
TOKEN = '1053257269:AAG_B9dQkWJFdI-1pDBlLSyScS9Y2QHHwIM'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=http://4d4b5a4c.ngrok.io/message' \
    .format(TOKEN)
