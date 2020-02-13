from flask import Flask, request, Response
from Message import *
import Bot

app = Flask(__name__)

Bot.open_tele()


@app.route('/message', methods=["POST"])
def handle_message():
    print("got message")
    if 'message' in request.get_json().keys():
        user_message = request.get_json()['message']
        message(user_message)
        return Response("success")
    else:
        return Response("success")


if __name__ == '__main__':
    app.run(port=port_number)

