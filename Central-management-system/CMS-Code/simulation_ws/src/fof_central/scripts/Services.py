#VSCode plugin for highlighting TODOs and FIXMEs within code
#
#TODO:
# - change next_amr_task to hadle instance of multiple workpieces with the status available
# - complete the exception clause

from datetime import datetime
confiramtion = 1
    

def wp_info(workpieceId, stepIndex): #Don't think we need stepIndex here
    queryStatement = {"workpieceId":workpieceId} #I think a more complex search could make things easier here.
    infoWorkpiece = workpiece(Query("selection", "workpieces", queryStatement ))

    actionfile =  infoWorkpiece.actionList(2, infoWorkpiece.stepIndex)
    #send the action file to the requested asset. (Do we need a asset_ID?)

def ndt_result(assetId,workpieceId,result, failTestIndex):
    queryStatementSearch = {"workpieceId":workpieceId}
    queryStatementUpdate = {"$set":{"error":"TestFailed"}}
    Query("updation", "Workpiece",queryStatementSearch, queryStatementUpdate)  #Update asset conveyor as taken
    return confirmation 

def wp_moved(assetId, workpieceId, moveType):
    if moveType == 1
        queryStatementsearch = 
        queryStatementUpdate = 
        Query("updation", "Assets", queryStatementsearch, queryStatementUpdate)
        
        
    else:
# if assetId[0:3] == "EXM" OR "NDT":
    #if movetype == "offload":
        #Workpiece now on AMR
        #Update activity log : "AMR Recieved"
    #elseif movetype == "onload"
        #Workpiece recieved at destination and task marked complete
# if assetId[0:3] == "AMR"
    #if movetype == "offload"
        #Workpiece transferred to destination, waiting for machine Wp_moved
    #elseif movetype == "onload"
        #Workpiece recived from machine, travelling to destination
    
def asset_status(assetId, status_main, status_conveyorIN, status_conveyorOUT)
    queryStatementSearch = {"assetId":assetId}
    queryStatementUpdate = {"status_main":status_main,"status_conveyorIN":status_conveyorIN,"status_conveyorOUT":status_conveyorOUT}
    query("updation","Asset",querystatement,queryStatementUpdate)

#   Act on status chnages if they need action i.e. error...


def next_amr_task(assetId):
    try:
        AMRTasksWithTheStatusAvailable = Query("selection", "AMRTasks", {"status":"available"})    # Looking for AMRTasks with the status available
        dateTimeArray = storeAttributeAsArray(AMRTasksWithTheStatusAvailable, dateTime)             # Stores attribute into array allowin us to use min
        resultingAMRTask = AMRTasksWithTheStatusAvailable[][dateTime] == min(dateTimeArray)         # FIXME: this will most likely need a for loop to work
        
        for i = 0 : length(dateTimeArray)
            if checkIfTargetAssetIsAvailable(resultingAMRTask['toLocation']) == False:
                dateTimeArray.remove(min(dateTimeArray))    # to be improved
                resultingAMRTask = AMRTasksWithTheStatusAvailable[][dateTime] == min(dateTimeArray)
            
            else :
                queryStatementSearch = {"AMRTaskId":resultingAMRTask.AMRTaskId}
                queryStatementUpdate = {"$set":{"status":"inProcess"}}
                Query("updation", "AMRTask", queryStatementSearch, queryStatementUpdate)  #Update AMR task status to taken

                queryStatementSearch = {"assetId":resultingAMRTask.tolocation}
                queryStatementUpdate = {"$set":{"status_conveyorIN":"Unavaliable"}}
                Query("updation", "Asset",queryStatementSearch, queryStatementUpdate)  #Update asset conveyor as taken

                return resultingAMRTask['fromLocation'], resultingAMRTask['toLocation'], resultingAMRTask['workpieceId'
    except:
        print("There are no AMRTasks that are available at the moment")
        # send ARMTask commanding the AMR to wait

# Checks the status of the converyorIN for a given statusLocation
def checkIfTargetAssetIsAvailable(assetLocation):
    queryStatement = {"assetId":assetLocation}
    targetAsset = Query("selection", "Asset",queryStatement)
    if targetAsset['status_conveyorIN'] == "Available"
        return True
    else:
        return False
        
