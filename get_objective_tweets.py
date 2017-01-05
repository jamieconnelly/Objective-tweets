import csv
import config as c
from tweepy import API, Cursor, AppAuthHandler

accounts = ['NASA', 'guardiannews', 'Independent', 'csmonitor', 'bpolitics',
            'BBCWorld', 'FinancialTimes', 'BBCNews', 'NBCNews', 'CNN',
            'Reuters', 'AFP', 'WSJ', 'Jerusalem_Post', 'nytimes', 'business',
            'nypost', 'TIME', 'Newsweek', 'AJEnglish', 'haaretzcom',
            'nytimesworld', 'washingtonpost', 'YonhapNews', 'BuzzFeedUK',
            'Newsweek', 'LANow', 'bpolitics', 'nytimesworld', 'BuzzFeedNews',
            'AsiaPacNews', 'NewZealandNews_', 'itn_news', 'FOX16news', 'wbir',
            'brisbanetimes', 'DailyMirror', 'UAENews', 'SBSNews', 'euronews',
            'NYTLive', 'abc7newsBayArea', 'VOA_News', 'ChannelNewsAsia',
            'rtenews', 'TelegraphNews', 'htTweets', 'msnbc', 'usweekly',
            'ENews']

auth = AppAuthHandler(c.CONSUMER_KEY, c.CONSUMER_SECRET)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

for account in accounts:
    count = 0
    c = Cursor(api.search, q='from:'+account, lang='en').items(1500)

    with open('neutral_tweets.csv', 'a') as csvfile:
        wr = csv.writer(csvfile)
        for tweet in c:
            if (not tweet.retweeted) and ('RT' not in tweet.text):
                count += 1
                wr.writerow([0, tweet.id, tweet.created_at, 'NO_QUERY',
                             tweet.author.name.encode('utf-8'),
                             tweet.text.encode('utf-8')])

    print('{} tweets collected from account: @{}'.format(count, account))

print('finished collecting tweets.')
