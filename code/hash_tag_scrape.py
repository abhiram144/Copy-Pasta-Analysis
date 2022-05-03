import snscrape.modules.twitter as sntwitter
import pandas
import os
os.system("snscrape --jsonl --max-results 100000 --since 2021-12-01 twitter-hashtag BravePmModi > ./hash_tags_tweets/BravePmModi.json")