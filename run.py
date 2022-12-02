import praw
import configparser
import random


config = configparser.ConfigParser()
config.read('conf.ini')
reddit_user = config['REDDIT']['reddit_user']
reddit_pass = config['REDDIT']['reddit_pass']
reddit_client_id = config['REDDIT']['reddit_client_id']
reddit_client_secret = config['REDDIT']['reddit_client_secret']
reddit_target_subreddit = config['REDDIT']['reddit_target_subreddit']

reddit = praw.Reddit(
    username=reddit_user,
    password=reddit_pass,
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    user_agent='Random Reddit Wiki Page Poster (by u/impshum)'
)

reddit.validate_on_submit = True


def get_random_wikipage():
    wikipages = [i.name for i in reddit.subreddit(reddit_target_subreddit).wiki]
    allowed_wikipages = [i for i in wikipages if 'config' not in i]
    return reddit.subreddit(reddit_target_subreddit).wiki[random.choice(allowed_wikipages)].content_md


def post_to_reddit(title, selftext):
    reddit.subreddit(reddit_target_subreddit).submit(title, selftext=selftext)


def main():
    random_wikipage = get_random_wikipage()
    print(random_wikipage)
    post_to_reddit('Random Wiki Post', random_wikipage)


if __name__ == '__main__':
    main()
