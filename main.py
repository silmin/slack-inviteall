import slack

import mytoken

token = mytoken.token
client = slack.WebClient(token=token)

# res: ["member"][idx]["name"] -> @name
res = client.users_list()

