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

def chunk_generator(*args, startpoint=0, chunk_size=100, db_name = "prozorro", collection_name = "tenders",):
    connection = pymongo.MongoClient()
    db = connection[db_name]
    collection = db[collection_name]
    number_of_records = collection.count()
    left_number = -chunk_size+startpoint+1
    right_number = 0
    print(number_of_records)
    for numbers in range(startpoint,number_of_records//chunk_size+1):
        left_number += chunk_size
        if numbers == number_of_records//chunk_size:
            right_number -= (chunk_size+right_number-number_of_records)
        right_number += chunk_size
        yield left_number , right_number



client = pymongo.MongoClient()
db = client[DB_NAME]
tender = db[TENDERS_ID]
tender_details = db[TENDERS_DETAILS]
test_col = db.test
tender_notloaded = db[NOTLOADED]
try:
    generator = chunk_generator()
    for limits in generator:
        cursor_with_data = tender.find()[limits[0]:limits[1]]
        print("cursor created")
        print(limits)
        for element in cursor_with_data:
            url_string = API_URL + str(element["_id"])
            if tender_details.find({"_id" : str(element["_id"]) }).count() != 0:
                print(element["_id"])
                continue
            r = requests.get(url_string)
            print(r.status_code)
            if r.status_code != 200:
                answer = {}
                answer["_id"] = element["_id"]
                answer["status"] = r.status_code
                tender_notloaded.insert_one(answer)
                print(answer)
            time.sleep(0.33)


except:
    EnvironmentError