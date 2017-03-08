# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:58:15 2017

@author: Valder
"""

import requests
import sqlite3
import time
import dateutil.parser
import mqmachine


DB_NAME = "raw_data.db"
MAIN_TABLE = 'raw_data_prozorro'
API_URL = 'http://api.openprocurement.org/api/2.3/tenders'
SITE_URL = 'https://prozorro.gov.ua/tender'


def nextp(*args):

    next_page = args[0].json()["next_page"]["uri"]
    return next_page


def findchunk(*args):
    raw_data = args[0]
    json_data = raw_data.json()
    return json_data["data"]


def findtimestamp(*args):
    to_parse = findchunk(args[0])[-1]["dateModified"]
    return dateutil.parser.parse(to_parse).timestamp()

#last url used
r = requests.get('https://public.api.openprocurement.org/api/2.3/tenders?offset=2017-02-22T01%3A39%3A03.995734%2B02%3A00')
r.encoding = 'UTF-8'
print("____________________")
print(findchunk(r))
print((findtimestamp(r)))
mqmachine.inNew(r.url, nextp(r), str(findchunk(r)), findtimestamp(r))
while nextp(r) is not None:
    time.sleep(2)
    print("Done, next page:", nextp(r))
    r = requests.get(nextp(r))
    mqmachine.inNew(r.url, nextp(r), str(findchunk(r)), findtimestamp(r))

