#!/usr/bin/env python
import os
import isodate
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from googleapiclient.discovery import build
import logging

load_dotenv()

service = build("youtube", "v3", developerKey=os.getenv("YT_KEY"))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    mess_t = update.message.text
    try:
        if mess_t.find("youtube.com/watch?v="):
            start_id = mess_t.find("v=")+2
            end_id = mess_t.find("&", start_id)
            id_v = mess_t[start_id:end_id]
            request = service.videos().list(part="snippet,contentDetails", id=id_v)
            response = request.execute()
            duration = response["items"][0]["contentDetails"]["duration"]
            duration = isodate.parse_duration(str(duration))
            title = response["items"][0]["snippet"]["title"]
            update.message.reply_text(F"{title} ({duration})")

    except Exception as e:
        print(e)
        pass


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater(os.getenv("TOKEN"), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()