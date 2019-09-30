import sys
import json
import ast
import configparser
import urllib3
import requests

r = requests.get("http://www.google.com")
print(r.status_code)

config = configparser.ConfigParser()
config.read("config")

print(config["test"])

test=sys.argv[1]
print("Argument: " + test)
