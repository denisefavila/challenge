import argparse
import sys
import pandas as pd

from crawler.reddit_crawler import RedditCrawler
from telegram_bot.reddit_bot import updater
from tabulate import tabulate


def main():

    text = 'This is a program to get the top threads on reddit.\n' \
           'We provide a bot on telegram with results.\n' \
           'If you want to access debug mode you just need to specify ' \
           '--debug/-d with desired subreddits separated by semicolons.' \
           'ex. --debug \'cats,dogs\' '

    parser = argparse.ArgumentParser(description=text)
    parser.add_argument("--debug", "-d", help="debug mode")

    argss = vars(parser.parse_args())
    debug_mode = argss["debug"]

    if debug_mode:
        categories = debug_mode
        all_posts = list()

        for subreddit in categories.split(";"):
            top_posts = RedditCrawler(subreddit=subreddit,
                                      limit=5000).get_top_threads()

            all_posts += top_posts

        all_posts_dataframe = pd.DataFrame(all_posts)

        print(tabulate(all_posts_dataframe, headers='firstrow'))

    else:
        # Initialize telegram bot
        updater.start_polling()

        updater.idle()


if __name__ == "__main__":
    main()
