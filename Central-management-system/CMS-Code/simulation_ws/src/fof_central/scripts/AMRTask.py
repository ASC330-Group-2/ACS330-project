()""

class AMRTask:
from datetime import datetime


    fromLocation = ""
    toLocation = ""
    status = 
    dateTime = 

    # may need to include a extra vairable for indexing and identifying the order
    
    def __init__(self, fromLocation, toLocation, workpieceId, AMRTaskId):
        self.fromLocation = fromLocation
        self.toLocation = toLocation
        self.workpieceId = workpieceId
        self.dateTime = datetime.now()
        return 



    