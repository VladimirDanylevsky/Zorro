# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:58:15 2017

@author: Valder
"""

import requests
import time
import dateutil.parser
import pymongo


DB_NAME = "prozorro"
TENDERS_CHUNKS = 'tenders_chunks'
TENDERS_ID = 'tenders'
TENDERS_DETAILS = 'tenders_details'
TENDERS_INFO = 'tender_info'
NOTLOADED = 'notloaded'
API_URL = 'https://public.api.openprocurement.org/api/2.3/tenders'
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

client = pymongo.MongoClient()
db = client[DB_NAME]
tender = db[TENDERS_ID]
tenders_chunks = db[TENDERS_CHUNKS]
try:
    check_from_db = tenders_chunks.find().sort('timestamp', pymongo.DESCENDING)[1]['next_page']
except:
    check_from_db = None
print(check_from_db)
entry_url = (check_from_db or API_URL)
print('starting from:', entry_url)
while entry_url:
    try:
        r = requests.get(entry_url)
        if r.status_code == 200:
            chunk = findchunk(r)
            timestamp = findtimestamp(r)
            from_page = entry_url
            next_page = nextp(r)
            print('next:',next_page)
        else:
            raise EnvironmentError
        entry_url = next_page
        print('inserted:', from_page)
        to_insert = {'from_page': from_page, 'next_page': next_page, 'chunk_of_id': chunk, 'timestamp': timestamp}
        tenders_chunks.insert_one(to_insert)
        time.sleep(0.2)
    except:
        EnvironmentError

