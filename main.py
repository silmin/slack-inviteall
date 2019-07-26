import json
import requests

import mytoken

token = mytoken.token
url = "https://slack.com/api/users.list"
payload = {"token": token}

# res: ["members"][idx]["name"] -> [@]name
res = requests.get(url, params=payload).json()

# nameを抽出して@nameのみのlistを作成
users = ["@" + idx["name"] for idx in res["members"]]
