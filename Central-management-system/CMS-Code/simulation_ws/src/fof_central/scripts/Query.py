

class Query:
    import pymongo
    import datetime 
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
        
        if querytype == "updation"
            queryType(queryStatement, secondQueryStatement)
        else
            queryType(queryStatement) #QueryTypes : selection, updation, insertion, deletion


# Selection returns the JSON entry in mongoDb
# Example of selection: query = Query("Assest", "selection", {"satus":"available"})
   
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

# Example of deletion queryStatement
# Query("Assest", "deletion", {"satus":"notAvailable"})

    
#   #bear in mind you can have nested dictionaries in python  
#     def searchForHighestIdSuffix(idPrefix):
#         if idPrefix == "AMR" or "NDT" or "EM":
#             DataWithGighestIdSuffix = Query("selection", "asset", "Id", )

#             return highestIdSuffix
#         if idPrefix == "WP"

#         if idPrefix == "OR"

#         if idPrefix == "AMT"
    
    
# # the following method is used to create the unique ids that stick to our nameing style

#     def createUniqueId(idPrefix): # idPrefix is the first half of the naming style i.e. AMR
#         if idPrefix = "AMR": 
#             queryStatement = "SELECT from assets "
#             newestAMR = Query("selection", "asset", queryStatement )
#             sting id = idPrefix + strnumber+1
#         if idPrefix = "NDT": 

#         if idPrefix = "WP": 

#         if idPrefix = "OR": 
            
#         if idPrefix = "EM": 
#         if idPrefix = "AMR": 
            


   
   
