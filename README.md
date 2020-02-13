# Sport Bee

Telegram bot to keep you up to date with your favorite sport events

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

- Install mysql database
- Install Ngrok in your pc
- Optional: Install git to get a copy of the project easily


### Running the bot

- Clone this repo
- Get your url from the Ngrok
- Modify the config.py file with your db info and your Ngrock url
- Run API_model.get_teams() once to get all teams into your database ( you can just uncomment it in events_scheduler file in your first run then comment it again )
- Run both App.py and events_scheduler.py
- Enjoy the bot
#### if you want to make your own version of the bot you can make a new telegram bot and replace the token in the config.py file too

## Built With

* [Python](https://www.python.org/) - Programming Language
* [Telegram API](https://core.telegram.org/) - Bot API
* [Rapid APi](https://rapidapi.com/) - Live Data API

## Authors

* **Mahran Abbasi** - *Initial work*
* **Marwan Halabi** - *Initial work*
* **Yazan Abbasi** - *Initial work*


## License

This project is licensed under the MIT License

## Acknowledgments

* Hat tip to anyone whose code was used from so many google searches
* Inspiration by Excellenteam hackathon to build a telegram bot
* Huge thanks to the awesome constructors and staff of the Excelleteam program for all their help and support
