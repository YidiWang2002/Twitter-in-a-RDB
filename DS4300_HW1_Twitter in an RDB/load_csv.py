import time

from dbutils import DBUtils
from tweet_objects import User, Tweet

# Authenticate
user = 'root'
password = '100*100'
database = 'db_tweet'

dbu = DBUtils(user, password, database)

with open('follows.csv') as f:
    f.readline()
    for line in f.readlines():
        user_id, follows_id = line.strip().split(',')
        
        sql = "INSERT INTO follows (user_id, follows_id) VALUES (%s, %s) "
        val = (user_id, follows_id)
        dbu.insert_one(sql, val)
    print('import follows done!')
    

