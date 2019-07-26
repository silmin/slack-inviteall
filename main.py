import sys
import json
import requests

import mytoken
from getchannels import getChannels
from getallusers import getAllUsers
from invite import invite

token = mytoken.token

if __name__ == "__main__" :
    channels = getChannels(token, sys.argv[1])
    users = getAllUsers(token)
    result = invite(token, channels, users)
    
    print(result)
