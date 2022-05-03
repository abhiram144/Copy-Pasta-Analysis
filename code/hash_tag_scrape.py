import snscrape.modules.twitter as sntwitter
import pandas
import os
os.system("snscrape --jsonl --max-results 50000 --since 2021-12-01 twitter-hashtag HijabRow > ../hash_tags_tweets/HijabRow.json")