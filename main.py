import sys
import json
import requests

import mytoken

token = mytoken.token

def isUser(idx):
    return not(idx["deleted"] or idx["is_bot"] or idx["is_app_user"])

def getChannels(name):
    url = "https://slack.com/api/channels.list"
    payload = {"token": token}

    # res: ["channels"][idx]["name"] -> [#]name
    res = requests.get(url, params=payload).json()

    # 欲しいchannelを抽出してname:idのdictを作成
    targets = {idx["name"]:idx["id"] for idx in res["channels"] if idx["name"] == name}

    return targets

def getUsers():
    url = "https://slack.com/api/users.list"
    payload = {"token": token}

    # res: ["members"][idx]["name"] -> [@]name
    res = requests.get(url, params=payload).json()
    
    # userを抽出してname:idのdictを作成
    users = {idx["name"]:idx["id"] for idx in res["members"] if isUser(idx)}

    return users


if __name__ == "__main__" :
    channels = getChannels(sys.argv[1])
    users = getUsers()
    
