import tweepy

# 認証に必要なキーとトークン
API_KEY = 'N5M9V9lRTbzlrYYZYWDsUAq4D'
API_SECRET = '7zbFLofkfY5Tk88hhpXS7n7DblB9onxrBLq0Gsog0sYFMQWKyo'
ACCESS_TOKEN = '2928718626-INo2ONeSTLerv3ZuGrcZOOFMX3oDEm8PRNn3Nv1'
ACCESS_TOKEN_SECRET = '7ZkTlzssuNmbFHoJINYke9JIWvqO5RZBWzt8lBUMiX9IQ'

# APIの認証
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# キーワードからツイートを取得
api = tweepy.API(auth)
tweets = api.search_tweets(q=['Python'], count=10)

for tweet in tweets:
    print('-----------------')
    print(tweet.text)
