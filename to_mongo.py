import pymongo
import mqmachine
import ast
import time

chunk_of_data = mqmachine.getChunk()
client = pymongo.MongoClient()
db = client['prozorro']
rows = chunk_of_data.fetchall()
tender = db.tenders
not_unique = db.nuniques
i = 0

for row in rows:
    try:
        row_to_split = ast.literal_eval(row[0].replace('id', '_id'))
        for element in row_to_split:
            try:
                result = tender.insert_one(element)
            except:
                result = not_unique.insert_one(element)
                continue
    except:
        continue





