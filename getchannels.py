import json
import requests

def getChannels(token, name):
    url = "https://slack.com/api/channels.list"
    payload = {"token": token}

    # res: ["channels"][idx]["name"] -> [#]name
    res = requests.get(url, params=payload).json()

    # 欲しいchannelを抽出してname:idのdictを作成
    targets = {idx["name"]:idx["id"] for idx in res["channels"] if idx["name"] == name}

    return targets

