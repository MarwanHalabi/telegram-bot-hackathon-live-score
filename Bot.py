import requests
from config import *


def open_tele():
    requests.get(TELEGRAM_INIT_WEBHOOK_URL)


