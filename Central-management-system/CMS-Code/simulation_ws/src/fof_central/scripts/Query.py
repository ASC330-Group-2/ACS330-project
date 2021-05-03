#VSCode plugin for highlighting TODOs and FIXMEs within code
#
#TODO:
# find out what the data type is returned when making selection queries 
#

class Query:
    import pymongo
    import datetime 
    import json
    #setting up the database to connect to our MongoDB server
    database = "CMS_Database"
    myclient - pymongo.MongoClient("mongodb+srv://Password:Password@cluster0.56sgz.mongodb.net/?retryWrites=true&w=majority")
    #mydb = myclient[database] maybe look into what this does
    db = cluster["cluster0"]
    collectionName = ""
    collection = db[collectionName]
    queryType = NULL  # selection, updation, insertion, deletion } these are the four types of queries
    queryStatement = ""

    def __init__(collectionName, queryType, queryStatement, secondQueryStatement):
        
        self.collectionName = collectionName
        self.queryType = queryType
        
        if querytype == "updation":
            queryType(queryStatement, secondQueryStatement)
        else:
            queryType(queryStatement) #QueryTypes : selection, updation, insertion, deletion


# Selection returns the JSON entry in mongoDb
# Example of selection: query = Query("Assest", "selection", "{"satus":"available"}")
   
    def selection(queryStatement):
        collection.find({}, queryStatement) # datafield:dataValue needs to be replaced with queryStatement
        for result in results:
            print(result)
        return results


# Example of updation queryStatement    
# Query("Asset", "updation", "{"satus":"available"}", "{"$set":{satus":"completed"}"})

    def updation(queryStatement, secondQueryStatement):
        collection.update(queryStatement, secondQueryStatement)

# Example of insertion queryStatement
# Query("Order", "insertion", "{"orderId":"OR1001","orderPreset":"chair", "dateTime":"2017-11-23 23:55:59", "status":"complete"}")
# Be sure to fill out all values

    def insertion(queryStatement):
        collection.insert_one(queryStatement)

# Example of deletion queryStatement
# Query("Assest", "deletion", {"satus":"notAvailable"})

    def deletion(queryStatement):
        collection.delete_one(queryStatement)


# The following method returns the highest in suffix
# This can be simplified if the suffix is stored as an integer as opposed to a string
    def searchForHighestIdSuffix(idPrefix, collectionName):
        data = Query("selection", collectionName, "idPrefix", idPrefix)
        stringList = storeAttributeAsArray(data, idSuffix)                              # Storing the the values as a list of stings
        intList = list(map(int, stringList))                                            # Converting the strings into integers
        return max(intList)
    
    def storeAttributeAsArray(data,attribute):
        array = []
        for entry in data:
            array.append(result.attribute)
        return array 
        
    

       
   
