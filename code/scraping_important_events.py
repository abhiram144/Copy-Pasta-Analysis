# import statements
import os
import json
import csv
import datetime
# This function is used to initialze important events dd-mm-yyyy format
def initialize(event_start, event_end):
    event_start["2014_general_elections"] = "01-01-2014"
    event_end["2014_general_elections"] = "30-06-2014"
    event_start["make_in_india"] = "01-09-2014"
    event_end["make_in_india"] = "31-10-2014"
    event_start["uri_attack"] = "01-09-2016"
    event_end["uri_attack"] = "31-10-2016"
    event_start["demonetization"] = "01-11-2016"
    event_end["demonetization"] = "31-01-2017"
    event_start["gst"] = "01-04-2017"
    event_end["gst"] = "31-08-2017"
    event_start["pulwama_attack"] = "01-02-2019"
    event_end["pulwama_attack"] = "28-02-2019"
    event_start["2019_elections"] = "01-03-2019"
    event_end["2019_elections"] = "30-06-2019"
    event_start["article_370"] = "01-08-2019"
    event_end["article_370"] = "31-10-2019"
    event_start["CAA_NRC"] = "01-12-2019"
    event_end["CAA_NRC"] = "31-01-2020"
    event_start["covid_first_wave"] = "01-03-2020"
    event_end["covid_first_wave"] = "31-05-2020"
    event_start["farmers_protest"] = "01-12-2020"
    event_end["farmers_protest"] = "28-02-2021"
    event_start["covid_second_wave"] = "01-04-2021"
    event_end["covid_second_wave"] = "31-05-2021"
    event_start["up_punjab_elections"] = "01-12-2021"
    event_end["up_punjab_elections"] = "28-02-2022"

def initialize_writer(event_start, csv_writer):
    for key in event_start.keys():
        data_file = open("../user_tweets/"+key+".csv",'w',newline='')
        csv_writer[key] = csv.writer(data_file)
    data_file = open("../user_tweets/user_details.csv",'w',newline='')
    csv_writer["user_details"] = csv.writer(data_file)

def populate_headers(event_start,csv_writer):
    user_details = ['username','id','displayname','followersCount','friendsCount','location']
    # write user keys
    csv_writer["user_details"].writerow(user_details)
    tweet_details = ['tweet_id','user_name','date','content','language','reply_count','retweet_count','like_count','hashtags']
    # populate tweet headers
    for key in event_start.keys():
        csv_writer[key].writerow(tweet_details)

# this module is used to populate csv files
def populate_user_details(csv_writer):
    dir_path = "/home/sai/IIITHYDERABADMTECH/Mtech_4th_semester/computational_social_science/UsersTweets"
    for filename in os.listdir(dir_path):
        with open(dir_path+"/"+filename) as file:
            for line in file:
                 temp_dict = json.loads(line)
                 get_user_details = temp_dict["user"]
                 write_user_details = {}
                 write_user_details["username"] = get_user_details["username"]
                 write_user_details["id"] = get_user_details["id"]
                 write_user_details["displayname"] = get_user_details["displayname"]
                 write_user_details["followersCount"] = get_user_details["followersCount"]
                 write_user_details["friendsCount"] = get_user_details["friendsCount"]
                 write_user_details["location"] = get_user_details["location"]
                 csv_writer["user_details"].writerow(write_user_details.values())
                 break




# this module is used to populate tweets
def populate_tweets(event_start,event_end,csv_writer):
    dir_path = "/home/sai/IIITHYDERABADMTECH/Mtech_4th_semester/computational_social_science/UsersTweets"
    for filename in os.listdir(dir_path):
        with open(dir_path+"/"+filename) as file:
            for line in file:
                temp_dict = json.loads(line)
                write_tweet_details={}
                write_tweet_details["tweet_id"]=temp_dict["id"]
                write_tweet_details["user_name"] = temp_dict["user"]["username"]
                write_tweet_details["date"] = temp_dict["date"]
                write_tweet_details["content"] = temp_dict["content"]
                write_tweet_details["language"] = temp_dict['lang']
                write_tweet_details["reply_count"] = temp_dict["replyCount"]
                write_tweet_details["retweet_count"] = temp_dict["retweetCount"]
                write_tweet_details["like_count"]=temp_dict["likeCount"]
                write_tweet_details["hashtags"] = temp_dict["hashtags"]
                # format date and compare
                split_date = write_tweet_details["date"].split("T")[0]
                formatted_date = datetime.datetime.strptime(split_date,'%Y-%m-%d')
                for key in event_start.keys():
                    start_date = datetime.datetime.strptime(event_start[key],'%d-%m-%Y')
                    end_date = datetime.datetime.strptime(event_end[key],'%d-%m-%Y')
                    if formatted_date >= start_date and formatted_date <= end_date:
                        csv_writer[key].writerow(write_tweet_details.values())
                        break

if __name__ == "__main__":
    # initialize important date events
    event_start = {}
    event_end = {}
    initialize(event_start, event_end)
    # initialize csv writer files
    csv_writer={}
    initialize_writer(event_start,csv_writer)
    # populate headers for csv files
    populate_headers(event_start,csv_writer)
    # populate user details
    populate_user_details(csv_writer)
    # populate tweets
    populate_tweets(event_start,event_end,csv_writer)
