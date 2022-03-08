import snscrape.modules.twitter as sntwitter
import pandas
import os

df = pandas.read_excel('userData.xlsx', sheet_name="user_data")

for user in df["username"].values:
    os.system(f"snscrape --jsonl twitter-search 'from:{user}'> UsersTweets/{user}.json")