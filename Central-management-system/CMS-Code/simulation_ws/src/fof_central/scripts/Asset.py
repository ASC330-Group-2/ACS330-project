()""

class Asset:
    assetId = NULL
    location = NULL
    status_main = "Available"
    status_conveyorIN = "Available"
    status_conveyorOUT = "Available"

#make sure variable names line up

    def __init__(self, aassetId, location):
        self. assetId

        #function to automatically insert asset into the database
        queryStatement = "INSERT into Assets, assetId = {}, location = {}, status_main = {}, status_conveyorIN ={}, status_conveyorOUT = {}".format(assetId, location, status_main, status_conveyorIN, status_conveyorOUT)
        Query("Insertion", "Assets", queryStatement)
        
    def uploadNewAssetToDatabase():
        newAsset = Query("insertion", "asset", )

        if


