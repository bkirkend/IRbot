import requests

def add_bot():
    with open('group.txt') as r:
        info = r.readlines()

    groupid = info[1]
    access_token = info[4]

    groupme_url = 'https://api.groupme.com/v3/bots?token=' + access_token
    bot_data = {"bot":{"name":"IR_helper", "group_id": groupid}}

    response = requests.post(groupme_url, json=bot_data)

    bot_id = response.json()['response']['bot']['bot_id']

    return bot_id