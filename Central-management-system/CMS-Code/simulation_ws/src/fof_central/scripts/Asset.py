H()""

class Asset:
    assetId = NULL
    location = NULL
    status_main = "Available"
    status_conveyorIN = "Available"
    status_conveyorOUT = "Available"

#make sure variable names line up

    def __init__(self, type, location):
        self.assetId =  generateNewID(type, "Asset")
        self.location = location

    def uploadNewAssetToDatabase():
        #function to automatically insert asset into the database
        queryStatement = "{"assetId":{},"status_main":{},"status_conveyorIN":{},"status_conveyorOUT":{},"location":{}}".format(assetId, status_main, status_conveyorIN, status_conveyorOUT, location)
        Query("Insertion", "Assets", queryStatement)
        if


