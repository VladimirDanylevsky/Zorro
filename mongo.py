import pymongo
import requests
import pprint


client = pymongo.MongoClient()
db = client['prozorro']
r = requests.get('https://public.api.openprocurement.org/api/2.3/tenders?offset=2016-11-04T22%3A56%3A44.710451%2B02%3A00')
print(r.json())
print(db.collection_names(include_system_collections=False))
posts = db.posts
pprint.pprint((posts.find_one()))
