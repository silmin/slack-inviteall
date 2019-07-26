import json
import requests

def invite(token, channels, users):
    url = "https://slack.com/api/channels.invite"
    payload = {"token": token}

    result = {}
    
    # channelリストを一つ選ぶ
    for key, val in channels.items():
        payload["channel"] = val
        ch_name = key
        real_names = []
        # userを全部そのchannelに追加
        for key, val in users.items():
            payload["user"] = val
            res = requests.post(url, params=payload).json()
            if res["ok"]: real_names.append(key)
            print(res)
        
        # {channel: [users]}
        result[ch_name] = real_names

    return result
