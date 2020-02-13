

from flask import Flask, request, Response
from Message import *
import Bot

app = Flask(__name__)

Bot.open_tele()


@app.route('/message', methods=["POST"])  # /check
def handle_message():
    print("got message")
    user_message = request.get_json()['message']
    message(user_message)
    return Response("success")


if __name__ == '__main__':
    app.run(port=port_number)

