#VSCode plugin for highlighting TODOs and FIXMEs within code
#
#TODO:
# find out what the data type is returned when making selection queries 
# playing around with sending functions as parameters. still not completed



class Query:
    import pymongo
    from pymongo import MongoClient
    from datetime import datetime
    #setting up the database to connect to our MongoDB server
    cluster = pymongo.MongoClient("mongodb+srv://Password:Password@cluster0.56sgz.mongodb.net/CMS_Database?retryWrites=true&w=majority")
    #mydb = myclient[database] maybe look into what this does
    db = cluster["CMS_Database"]
    collectionName = "AMRTask"
    collection = db[collectionName]

    #queryType is not a string so make sure parameter is not a string

    def __init__(self, queryType, collectionName, queryStatement, secondQueryStatement):
        Query.collectionName = collectionName
        self.queryType = queryType
        self.queryStatement = queryStatement
        self.secondQueryStatement = secondQueryStatement
        self.queryType(self)
        

    def __init__(self, queryType, collectionName, queryStatement):
         Query.collectionName = collectionName
         self.queryType = queryType
         self.queryStatement = queryStatement
         self.queryType(self)


    # Selection returns the JSON entry in mongoDb
    # Example of selection: query = Query("Assest", "selection", "{"satus":"available"}")
   
    def selection(self):
        Query.collection.find({}, passedQuery.queryStatement) # datafield:dataValue needs to be replaced with queryStatement
        for result in results:
            print(result)
        return results


    # Example of updation queryStatement    
    # Query("Asset", "updation", "{"satus":"available"}", "{"$set":{satus":"completed"}"})

    def updation(self):
        Query.collection.update(passedQuery.queryStatement, passedQuery.secondQueryStatement)

    # Example of insertion queryStatement
    # Query("Order", "insertion", "{"orderId":"OR1001","orderPreset":"chair", "dateTime":"2017-11-23 23:55:59", "status":"complete"}")
    # Be sure to fill out all values

    def insertion(self):
        Query.collection.insert_one(self.queryStatement)


    # Example of deletion queryStatement
    # Query("Assest", "deletion", {"satus":"notAvailable"})

    def deletion(self):
        Query.collection.delete_one(self.queryStatement)


    # The following method returns the highest in suffix
    # This can be simplified if the suffix is stored as an integer as opposed to a string
    def generateNewID(idPrefix, collectionName):
        queryStatement = {}
        data = Query("selection", collectionName, queryStatement)
        stringList = storeAttributeAsArray(data, idSuffix)                              # Storing the the values as a list of stings
        intList = list(map(int, stringList))                                            # Converting the strings into integers
        newID = "idPrefix" + (max(intList) +1)
    
    
    def storeAttributeAsArray(data,attribute):
        array = []
        for entry in data:
            array.append(result.attribute)
        return array 
        
    

def main():
    import pymongo
    from pymongo import MongoClient
    from datetime import datetime
    #setting up the database to connect to our MongoDB server
    cluster = pymongo.MongoClient("mongodb+srv://Password:Password@cluster0.56sgz.mongodb.net/CMS_Database?retryWrites=true&w=majority")
    #mydb = myclient[database] maybe look into what this does
    db = cluster["CMS_Database"]
    collectionName = "AMRTask"
    collection = db[collectionName]
    
    #testing the query class
    
    #AMRTaskId = {'1'{'IdPrefix':'AMT'}, {'IdSuffix':1001}} # Removed quotations as it is dictonary not string.
    tolocation = "NDT1001"
    fromLocation = "EM1002"
    status = "available"
    workpieceId = "1001"
    queryStatement = {"tolocation":tolocation,"fromLocation":fromLocation,"status":status,"DateTime":datetime.now(),"workpieceId":workpieceId}
    first = Query(Query.insertion,"AMRTask", queryStatement)


if __name__ == "__main__":
    main()
