import json
import requests

def isUser(idx):
    return not(idx["deleted"] or idx["is_bot"] or idx["is_app_user"])


def getAllUsers(token):
    url = "https://slack.com/api/users.list"
    payload = {"token": token}

    # res: ["members"][idx]["name"] -> [@]name
    res = requests.get(url, params=payload).json()
    
    # userを抽出してname:idのdictを作成
    users = {idx["name"]:idx["id"] for idx in res["members"] if isUser(idx)}

    return users


