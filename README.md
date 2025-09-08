# Ambient Weather Discord Bot
A simple weather bot using the Ambient Weather API in Python

## Setup

1. Create the .env file with the following syntax, and set the variables:
```
DISCORD_TOKEN=
AMBIENT_WEATHER_API_KEY=
AMBIENT_WEATHER_APP_KEY=
AMBIENT_WEATHER_MAC_ADDRESS=
```

2.1: Create a virtual environment for python and activate it (optional)
```bash
# Create the environment with the name "bot-env"
python -m venv bot-env
# Activate the environment using the activate script
./bot-env\Scripts\activate
```
2.2: Install the requirements:
```
pip3 install -r requirements.txt
```
3. Create the discord bot:
Go to [the discord bot developer website](https://discord.com/developers/applications) and make a bot.

3.1. Give the bot [all intents](https://i.imgur.com/cU09rZn.png)

3.2 Invite the bot to your server by [creating an install link](https://i.imgur.com/ELIu1IU.png)

4. Start the bot 
```
python main.py
```


