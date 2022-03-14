import json
import pandas as pd
import tweepy
import sys

import time

with open("twitter_credentials.json", "r") as file:
    data = file.read()
    
credentials = json.loads(data)
client = tweepy.Client(bearer_token=credentials["BEARER_TOKEN"])

seed_account = sys.argv[1]
seed = client.get_user(username = seed_account)

def get_following(client, user_ids):
    following_list = []
    
    for user_id in user_ids:
        try:
            f = client.get_users_following(user_id, max_results = 1000).data
            if f:
                following_list.extend(f) # for more than 1000 results return, need to use pagination token
        except tweepy.TweepyException:
            print(str(user_id) + "error fetching following list")
            continue
            
    return following_list

f = get_following(client, [seed.data.id])

following_graph = pd.DataFrame(columns=['source','target'])

following_graph['target'] = [user.id for user in f]
following_graph['source'] = seed.data.id

starting_users = following_graph['target']

csv_name = "following_list_" + str(seed_account) + ".csv"

for user in starting_users:
    following = get_following(client, [user])
    
    temp = pd.DataFrame(columns=['source','target'])
    temp['target'] = [f.id for f in following]
    temp['source'] = user
    
    following_graph = following_graph.append(temp)
    following_graph.to_csv(csv_name, index=False)
    print(str(user) + " added")
    
    time.sleep(60)
