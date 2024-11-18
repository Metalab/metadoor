#!/usr/bin/env python3
import json
import requests
import config

ONSITE_STATUS_PATH = "/var/www/metadoor/webpage/status.json"
HASS_ENDPOINT = "http://10.20.30.97/api/states/input_boolean.lab_is_on"

HASS_API_KEY= os.getenv("HASS_API_KEY")

headers = {"Authorization": f"Bearer {HASS_API_KEY}"}
data = requests.get(HASS_ENDPOINT, headers=headers).json()
onsite_status = data["state"]
with open(ONSITE_STATUS_PATH, "w") as f:
    if(onsite_status =="on"):
        f.write('{ "status" : "open" }')
    elif(onsite_status =="off"):
        f.write('{ "status" : "closed" }')
    else:
        f.write('{ "status" : "unkown" }')