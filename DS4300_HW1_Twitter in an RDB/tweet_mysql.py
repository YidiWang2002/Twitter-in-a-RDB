"""
Tweet Database API for MySQL
"""

from dbutils import DBUtils
from tweet_objects import Tweet

class TweetAPI:

    def __init__(self, user, password, database, host="localhost"):
        self.dbu = DBUtils(user, password, database, host)
    
    def postTweet(self, tweet):
        sql = "INSERT INTO tweet (tweet_id, user_id, tweet_ts, tweet_text) VALUES (%s, %s, %s, %s) "
        val = (tweet.tweet_id, tweet.user_id, tweet.tweet_ts, tweet.tweet_text)
        self.dbu.insert_one(sql, val)
        
    def getTimeline(self, user_id):
        query = f"""SELECT TWEET.tweet_id, TWEET.user_id, TWEET.tweet_ts, TWEET.tweet_text
FROM TWEET
JOIN FOLLOWS ON TWEET.user_id = FOLLOWS.follows_id
WHERE FOLLOWS.user_id = {user_id}
ORDER BY TWEET.tweet_ts DESC
LIMIT 10;
"""
        tweets = self.dbu.execute(query)
        return tweets
