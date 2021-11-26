from pymongo import MongoClient


def get_database(DB):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb://localhost:27017"
    CONNECTION_STRING = "mongodb+srv://admin:root@cluster0.u1hsn.mongodb.net/learning?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client[DB]
    
db_name = get_database('short_url')

collection = db_name["all_urls_data"]


# new_item = {
#     "_id" : 2,
# "short_url" : "hello",
# "long_url": "abc"
# }


# collection.insert_one(new_item)


for item in collection.find():
    print(item['short_url'])

# for item in shorturl_db.list_collection_names():
#     print(item)