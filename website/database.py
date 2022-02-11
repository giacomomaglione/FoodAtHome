import certifi
import pymongo



class Database(object):
    URI = "mongodb+srv://foodathome:UniParthenope@cluster0.fkbq2.mongodb.net/test"

    DATABASE = None


    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI, tlsCAFile = certifi.where())
        Database.DATABASE = client['foodathome']



