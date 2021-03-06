#! /usr/bin/python 
import sys
import requests
import json

from QuoineApiSettings import Settings

api = Settings()

hdrs = {
   "user-agent": api.UserAgent,
   "X-Quoine-Device": api.DeviceName, 
   "X-Quoine-User-Id": api.UserId, 
   "X-Quoine-User-Token": api.UserToken
  }

try:
   url = api.BaseURL + api.GetAccountsURI 
   r = requests.get(url,headers=hdrs)
   data = json.loads(r.text)
   btc = data["bitcoin_account"]
   print "\n"
   print btc["id"], " ", btc["currency"]," ",btc["free_balance"], " ", btc["balance"]
   for account in data["fiat_accounts"]:
     print "\n================================="
     print account["id"], " ", account["currency"]," ",account["free_balance"], " ", account["balance"]
except requests.exceptions.HTTPError as e: 
   print "Error: \n"
   print e
print "\n"
