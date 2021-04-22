#presets available are chair, table and stand
# chair contains 4 legs, 1 square, 1 rectangle
# table contains 4 legs, 1 rectangle
# stand contains 1 leg, 1 square, 1 rectangle


class Order:

    orderId = ""
    orderPreset = "" 
    dateTime = 
    status = 
    
    # this will look through a order preset collection and get the list of workpiece presets needed for that order



    def __init__(self, orderId, workpieces):
        self.orderId = orderId
        self.workpieces = workpieces

        #function to automatically insert order into the database
        queryStatement = "INSERT into Orders, OrderId = {}, orderPreset = {}".format(orderId, orderPreset)
        Query("Insertion", "Assets", queryStatement)

    def createWorkpieces(orderPreset)
        #Query collection for the last ID to increment the new Workpiece ID
        #LatestID = QueryResult

        #Return Order preset
        #Query orderPreset collection for id = orderPreset. This returns an array of workpiece presets.
        


       
        #queryStatement = "SELECT Presets"

        


        #for i = 0 to :
            #NewNum = LatestID[2:5] + (i + 1)
            #NewWorkpieceID = "WP" & NewNum #New ID is created
            #workpiece(workpieceId, workpiecePreset)

    def createUniqueId(idPrefix): 
        if idPrefix = "AMR": 
            queryStatement = "SELECT from assets "
            newestAMR = Query("selection", "asset", queryStatement )
            sting id = idPrefix + strnumber+1
        if idPrefix = "NDT": 

        if idPrefix = "WP": 
        if idPrefix = "OR": 
        if idPrefix = "EM": 
        if idPrefix = "AMR": 
        

        