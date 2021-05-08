#presets available are chair, table and stand
# chair contains 4 legs, 1 square, 1 rectangle
# table contains 4 legs, 1 rectangle
# stand contains 1 leg, 1 square, 1 rectangle

import datetime from datetime
class Order:

    orderId = ""
    orderPreset = "" 
    dateTime = 
    status = 
    
    # this will look through a order preset collection and get the list of workpiece presets needed for that order



    def __init__(self,orderPreset workpieces):
        self.workpieces = workpieces
        self.orderPreset = orderPreset
        self.orderId = generateNewID("OR", "Order")

        #function to automatically insert order into the database
        queryStatement = {"orderId":orderId,"orderPreset":orderPreset,"dateTimeInitialised":datetime.now(),"status":status}
        Query("Insertion", "Assets", queryStatement)

    def createWorkpieces(orderPreset)
        
        #Query Orderpresets for workpeices:
        queryStatement = {"orderPreset":orderPreset}
        listOfPresets = Query("Selection","OrderPreset",queryStatement)

        for i =0 : length(listOfPresets):
            #Query collection for the last ID to increment the new Workpiece ID
    
            
            #Create workpiece object which automatically adds it to the database.format
            Workpiece(listOfPresets(i),orderId)


    