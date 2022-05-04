from configuration import Configuration
import pymongo
client  = pymongo.MongoClient(Configuration.APP_MONGO_URI)
db = client.get_database(Configuration.APP_MONGO_DB)