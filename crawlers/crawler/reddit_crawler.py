from const import DEFAULT_POINTS, DEFAULT_SORT, BASE_REDDIT_URL
from crawler.utils import get_soup


class RedditCrawler(object):

    def __init__(self, subreddit, limit=DEFAULT_POINTS, sort=DEFAULT_SORT):
        self.subreddit = subreddit
        self.limit = limit
        self.sort = sort

    def _get_composite_subreddit_page(self):
        return BASE_REDDIT_URL + "r/{}/{}/".format(self.subreddit, self.sort)

    def get_top_threads(self):
        status_code, soup = get_soup(self._get_composite_subreddit_page())
        print(status_code)
        if status_code != 200:
            pass
        
        else:
            top_posts = list()

            while True:
                sitetable = soup.find_all("div", {"id": "siteTable"})[0]
                children = sitetable.findChildren("div", recursive=False)

                for child in children:
                    if child.get("data-promoted") == 'false':
                        votes = child.find('div', {'class': 'score unvoted'}).get('title')
                        if votes and int(votes) < self.limit:
                            return top_posts

                        title = child.find('p', {'class': 'title'}).find("a")
                        thread_name = title.contents[0]
                        thread_link = title.get("href")

                        comments_link = child.find('li', {'class': 'first'}).find('a')['href']

                        top_posts.append({"subreddit": child["data-subreddit-prefixed"],
                                          "votes": votes,
                                          "thread_name": thread_name,
                                          "thread_link": thread_link,
                                          "comments_link": comments_link})

                next_button = soup.find("span", {'class': "next-button"})
                next_page_link = next_button.find("a").attrs['href']
                _, soup = get_soup(next_page_link)

            return top_posts
