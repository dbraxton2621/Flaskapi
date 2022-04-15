#!/usr/bin/env python3
import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/"

resp = requests.get(URL).json()

# pretty-print the response back from our POST request
# pprint(resp.json)
print(f"""Devin's favorite sport is : {resp['sport']}""")
