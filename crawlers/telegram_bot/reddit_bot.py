import redis
import telegram
import configparser
import logging
import pandas as pd
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tabulate import tabulate

from const import DEFAULT

# Enable logging
from crawler.reddit_crawler import RedditCrawler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    # Welcome message
    msg = "Hey you, I'm {0}!\n".format(me.first_name)
    msg += "I can show you which are the top threads on Reddit now. \n"
    msg += "You just need to call the command /NadaPraFazer with " \
           "desired subreddits separated by semicolons. \n\n"
    msg += "Ex. /NadaPraFazer programming;dogs;brazil.\n"

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


def nada_pra_fazer(bot, update):
    message = update.message.text.split()
    if len(message) != 2:
        msg = "Sorry, looks like you write something wrong. \n" \
              "Remember you should pass the subredits separated " \
              "by semicolons."
        bot.send_message(chat_id=update.message.chat_id,
                         text=msg)
    else:
        categories = update.message.text.split()[1]
        all_posts = list()

        for subreddit in categories.split(";"):
            top_posts = RedditCrawler(subreddit=subreddit,
                                      limit=DEFAULT_POINTS).get_top_threads()

            all_posts += top_posts
            if len(top_posts) == 0:
                msg = "Sorry, I couldn't find any top post for {}".format(subreddit)
                bot.send_message(chat_id=update.message.chat_id,
                                 text=msg)

        for post in all_posts:
            text = '******************************** \n'
            text += ('<b>Subreddit = {subreddit}, \n'
                     'Votes: {votes}, \n'
                     'Title: {thread_name}</b>\n\n'
                     'Link: \n{comments_link}').format(subreddit=post["subreddit"],
                                                       votes=post['votes'],
                                                       thread_name=post['thread_name'],
                                                       comments_link=post['comments_link'])
            text += '\n\n'


            # Send the message
            bot.send_message(chat_id=update.message.chat_id,
                             text=text,
                             parse_mode=ParseMode.HTML)


def unknown(bot, update):
    """
        Placeholder command when the user sends an unknown command.
    """
    msg = "Sorry, I don't know what you're asking for."
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)


# Connecting to Telegram API
# Updater retrieves information and dispatcher connects commands
updater = Updater(token=DEFAULT['token'])
dispatcher = updater.dispatcher

# log all errors
dispatcher.add_error_handler(error)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

nada_pra_fazer_handler = CommandHandler('NadaPraFazer', nada_pra_fazer)
dispatcher.add_handler(nada_pra_fazer_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)






