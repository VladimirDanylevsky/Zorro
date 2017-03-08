import pymongo
import requests
import ast
import time

DB_NAME = "prozorro"
TENDERS_ID = 'tenders'
TENDERS_DETAILS = 'tenders_details'
TENDERS_INFO = 'tender_info'
NOTLOADED = 'notloaded'
API_URL = 'http://api.openprocurement.org/api/2.3/tenders/'
SITE_URL = 'https://prozorro.gov.ua/tender'

client = pymongo.MongoClient()
db = client[DB_NAME]
tender = db[TENDERS_ID]
tender_details = db[TENDERS_DETAILS]
test_col = db.test
tender_notloaded = db[NOTLOADED]

try:
    print(tender_details.find({"data.status" : "unsuccessful"}).count())


except:
    EnvironmentError