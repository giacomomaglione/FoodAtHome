import certifi
import pymongo

class Database(object):
    URI = "mongodb+srv://foodathome:UniParthenope@cluster0.fkbq2.mongodb.net/test"

    DATABASE = None


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI, tlsCAFile = certifi.where())
        Database.DATABASE = client['foodathome']


    #cliente = DATABASE["Customer"]
    #rider = DATABASE["Rider"]
    #negozio = DATABASE["Store"]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
