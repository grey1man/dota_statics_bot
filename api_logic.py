import requests
import time
import db_logic
import json
proxy = {
    'http': '192.168.112.3:8080',
    'https': '192.168.112.3:8080'
}
#while True :
 #   if time.ctime[0:3] = 'Wed'
pro_matches = requests.get('https://api.opendota.com/api/proMatches',  proxies = proxy)  
pro_players = requests.get(' https://api.opendota.com/api/proPlayers', proxies = proxy)   
 


print(pro_matches.json())
print(time.ctime())
db_logic.out(pro_matches.json())

