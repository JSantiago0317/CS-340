from pymongo import MongoClient
from bson.objectid import ObjectId

#Creates and reads to AAC database, animals collection
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    #Initializes with username and password passed as arguments
    def __init__(self, username, password):
        # Initializing the MongoClient. 
        self.client = MongoClient('mongodb://%s:%s@localhost:43304/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    #Inserts document passed as argument into DB
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
    #Reads data from DB and stores in pymongo cursor object
    def read(self, data):
        if data is not None:
            return self.database.animals.find_one(data, {"_id":False})
        else:
            return "Nothing to search, because data parameter is empty"
        
    #Reads all documents
    def readAll(self, data):
        if data is not None:
            return self.database.animals.find(data, {"_id":False})
        else:
            return "Nothing to search, because data parameter is empty"
        
        
    #Updates document with ID passed as argument with data passed as argument
    def update(self, animalId, data):
        if data is not None:
            return self.database.animals.update_one(animalId, {"$set": data})
        else:
            return "Update failed"
        
    #Deletes document passed as argument
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data)
        else:
            return "Delete failed"
            