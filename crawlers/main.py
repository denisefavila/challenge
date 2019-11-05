import argparse
import sys
import pandas as pd
from crawler.reddit_crawler import RedditCrawler
from telegram_bot.reddit_bot import updater


def main():

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
