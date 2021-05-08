#TODO: finish off AMRTASk so that it uploads itself upon creation


class AMRTask:
from datetime import datetime


    fromLocation = ""
    toLocation = ""
    status = 
    dateTime = 
    workpieceId =

    # may need to include a extra vairable for indexing and identifying the order
    
    def __init__(self, fromLocation, toLocation, workpieceId, AMRTaskId):
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.workpieceId = workpieceId
        self.dateTime = datetime.now()
        #Adds new AMRTask to the database.
        queryStatement = {"AMRTaskId":AMRTaskId,"tolocation":toLocation,"fromLocation": fromLocation,"status":status,"DateTime":datetime.now(),"workpieceId":workpieceId}
        Query("Insertion", "Assets", queryStatement)
        return 



    