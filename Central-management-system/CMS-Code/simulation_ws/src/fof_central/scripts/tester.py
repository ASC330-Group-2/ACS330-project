# prerequisits
# for the following code to work you will need to make sure that you have listed your ip list in the database
# you will need to have created a user for the databse
# you need the packages pymongo and pymongo[srv] through pip





def main():
    import pymongo
    from pymongo import MongoClient
    from datetime import datetime
    from scripts import Query
    #setting up the database to connect to our MongoDB server
    cluster = pymongo.MongoClient("mongodb+srv://Password:Password@cluster0.56sgz.mongodb.net/CMS_Database?retryWrites=true&w=majority")
    #mydb = myclient[database] maybe look into what this does
    db = cluster["CMS_Database"]
    collectionName = "AMRTask"
    collection = db[collectionName]
    

    
    #AMRTaskId = {'1'{'IdPrefix':'AMT'}, {'IdSuffix':1001}} # Removed quotations as it is dictonary not string.
    tolocation = "NDT1001"
    fromLocation = "EM1002"
    status = "available"
    workpieceId = "1001"
    queryStatement = {"tolocation":tolocation,"fromLocation":fromLocation,"status":status,"DateTime":datetime.now(),"workpieceId":workpieceId}
    first = Query(self.insertion,"AMRTask", queryStatement)


if __name__ == "__main__":
    main()