-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS db_tweet;

-- Use the created database
USE db_tweet;

-- Create the TWEET table
CREATE TABLE IF NOT EXISTS TWEET (
    tweet_id INT PRIMARY KEY,
    user_id INT,
    tweet_ts DATETIME,
    tweet_text VARCHAR(255)
);

-- Create the FOLLOWS table
CREATE TABLE IF NOT EXISTS FOLLOWS (
    user_id INT,
    follows_id INT,
    PRIMARY KEY (user_id, follows_id)
);
