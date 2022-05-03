# import statements
import os
import json
import csv
import datetime
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
# This code is used to extract tweet content and time from json file and store in csv
def populate_filenames(dir_path):
    file_name_list = list()
    for filename in os.listdir(dir_path):
        #split filename
        hash_tag_name = filename.split(".")[0]
        file_name_list.append(hash_tag_name)

    return file_name_list

def initialize_writer(file_name_list, csv_writer):
    for f_name in file_name_list:
        print(f_name)
        f_path = "/home/sai/IIITHYDERABADMTECH/Mtech_4th_semester/computational_social_science/Copy-Pasta-Analysis/hash_tag_csv/"
        data_file = open(f_path+f_name+".csv",'w',newline='')
        csv_writer[f_name] = csv.writer(data_file)
    
def populate_header(file_name_list,csv_writer):
    tweet_details = ['tweet_id','user_name','date','content','language','reply_count','retweet_count','like_count','hashtags']
    for file_name in file_name_list:
        csv_writer[file_name].writerow(tweet_details)

def populate_tweets(file_name_list,csv_writer,dir_path,event_start,event_end):
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
                # write logic
                split_date = write_tweet_details["date"].split("T")[0]
                formatted_date = datetime.datetime.strptime(split_date,'%Y-%m-%d')
                start_date = datetime.datetime.strptime(event_start["up_punjab_elections"],'%d-%m-%Y')
                end_date = datetime.datetime.strptime(event_end["up_punjab_elections"],'%d-%m-%Y')
                if formatted_date >= start_date and formatted_date <= end_date:
                    csv_writer[filename.split(".")[0]].writerow(write_tweet_details.values())
                
                        



# initialize csv writers by json file_names
print("hello")
dir_path = "/home/sai/IIITHYDERABADMTECH/Mtech_4th_semester/computational_social_science/Copy-Pasta-Analysis/hash_tags_tweets"
file_name_list = populate_filenames(dir_path)
event_start = {}
event_end = {}
initialize(event_start, event_end)
# initialize csv writers
csv_writer = {}
initialize_writer(file_name_list,csv_writer)
# initialize headers
populate_header(file_name_list,csv_writer)
# populate tweets
populate_tweets(file_name_list, csv_writer, dir_path,event_start,event_end)
