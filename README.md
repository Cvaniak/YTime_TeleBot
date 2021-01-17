# YTime_TeleBot
Bot that sends you title and duration of YouTube Video! You can find this bot on Telegram [@duration_ytbot](https://web.telegram.org/#/im?p=%40duration_ytbot)!  

# Localy
---
First install ```pip install -r requirements.txt```  
Then add file ```.env``` with:
```
TOKEN="BOT TOKEN FROM TELEGRAM WEBSITE"
YT_KEY="KEY FROM GOOGLE CONSOLE"
```
Then run with ```python3 main.py```  

# Heroku
Just setup new Heroku project, create Variables with ```TOKEN``` and ```YT_KEY``` and push commit.

## Links
Template and first steps based on [codementor tutorial](https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq).  
Google staff [here](https://console.developers.google.com/) and here [here](https://developers.google.com/youtube/v3/quickstart/python).