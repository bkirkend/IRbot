import requests, json

def post_to_groupme_food(message):
    with open('group_food.txt') as r:
        info = r.readlines()
    
    bot_id = info[7]

    post_url = 'https://api.groupme.com/v3/bots/post'

    post_data = {"bot_id":bot_id, "text":message}

    requests.post(post_url,json=post_data)
