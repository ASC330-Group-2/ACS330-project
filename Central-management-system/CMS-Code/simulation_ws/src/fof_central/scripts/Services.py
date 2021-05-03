#VSCode plugin for highlighting TODOs and FIXMEs within code
#
#TODO:
# - change next_amr_task to hadle instance of multiple workpieces with the status available
# - complete the exception clause

from datetime import datetime

def next_amr_task(assetId):
    nextAMRTaskFound = 0
    TasksWithTheStatusAvailable = 0 

    while (nextAMRTaskFound == 0) ^ (TasksWithTheStatusAvailable =! NULL)
        minDate = "00/00/0000" #Min date acts as lower range of date that can be selected. 
        #When AMR task cannot be served as the 'tolocation' is not avaliable then this variable
        #is incremented to the equal the selected AMR task. 
        queryStatement = "SEARCH FOR AMR TASKS WITH status == avaliable AND priority == min BUT ALSO > {}".format(minDate)
        AMRTasksWithTheStatusAvaliable = Query("selection", "AMRTasks", queryStatement)
        if AMRTasksWithTheStatusAvaliable == NULL
            
        else 
            nextAMRTask = AMRTask(AMRTasksWithTheStatusAvaliable)
            queryStatement = "SEARCH Assets FOR status_conveyorOUT with assetId == {}".format(nextAMRTask.assetId)
            if status_conveyorOUT == "avaliable":
                #Serves Object nextAMRTask to AMR with ID assetId.
                nextAMRTaskFound == 1
            else if status_conveyorOUT == "occupied":
                minDate == nextAMRTask.priority
    

    if nextAMRTaskFound ==1: and AMRTasksWithTheStatusAvaliable =! NULL:
        #serve nextAMRTask to requesting AMR
        return nextAMRTask.fromlocation, nextAMRTask.tolocation, nextAMRTask.workpieceId
    else if AMRTasksWithTheStatusAvaliable == NULL and nextAMRTaskFound == 0:
        #No outstanding AMR tasks are avaliable. Notify AMR or give AMR specfic task

    
    #Search for task with lowest date, status==valiable and tolocation Status_ConveyorOOUT = avaliable DOESN'T WORK
    queryStatement = ("SELECT AMRTask.AMRTaskId, MIN(status.Status_ConveyorOUT)FROM AMRTask INNER JOIN status ON AMRTask.toLocation = status.assetId WHERE AMRTask.status = 'avaliable'")
    queryStatement = ("db.AMRTaskINNER JOIN status ON AMRTask.toLocation = status.assetId .find({ "AMRTask.status " :  'avaliable'},{"AMRTask.AMRTaskId": 1,"MIN(status.Status_ConveyorOUT)": 1});")
    
    # earliestAMRTaskdate = min(AMRTasksWithTheStatusAvailable.priority)
    # #*note to self* in the case you cant use min on an attribute of a class uncomment the following code
    # #------------------
    # # listOfDates = AMRTasksWithTheStatus
    # #-------------------
    # for i in AMRTasksWithTheStatusAvailable
    #     if AMRTasksWithTheStatusAvailable.priority == earliestAMRTaskdate:
    #         return AMRTasksWithTheStatusAvailable
    

def wp_info(workpieceId, stepIndex): #Don't think we need stepIndex here
    queryStatement = "SEARCH FOR WORKPIECE WITH ID == {}".format(workpieceId) #I think a more complex search could make things easier here.
    infoWorkpiece = workpiece(Query("1", "workpieces", queryStatement ))

    actionfile =  infoWorkpiece.actionList(2, infoWorkpiece.stepIndex)
    #send the action file to the requested asset. (Do we need a asset_ID?)

def ndt_result(assetId,workpieceId,result, failTestIndex):
    

def wp_moved(assetId, workpieceId, moveType)
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
#   querystatement = "FIND Asset with assetId == {}".format(assetId)
#   newValuesStatement = "set status_main, status_conveyorIN, status_conveyorOUT ==[{},{},{}]".format(status_main, status_conveyorIN, status_conveyorOUT)
#   query("assets","updation",querystatement,newValuesStatement)

#   Act on status chnages if they need action i.e. error...


def next_amr_task(assetId):
    try:
        AMRTasksWithTheStatusAvailable = Query("selection", "AMRTasks", "{"satus":"available"}")    # Looking for AMRTasks with the status available
        dateTimeArray = storeAttributeAsArray(AMRTasksWithTheStatusAvailable, dateTime)             # Stores attribute into array allowin us to use min
        resultingAMRTask = AMRTasksWithTheStatusAvailable[][dateTime] == min(dateTimeArray)         # FIXME: this will most likely need a for loop to work
        if checkIfTargetAssetIsAvailable(resultingAMRTask['toLocation']) == False:
            dateTimeArray.remove(min(dateTimeArray))
        else:
            Query("updation", "AMRTask", "status", "inProcess")    
            return resultingAMRTask['fromLocation'], resultingAMRTask['toLocation'], resultingAMRTask['workpieceId']
    except:
        print("There are no AMRTasks that are available at the moment")
        # send ARMTask commanding the AMR to wait

# Checks the status of the converyorIN for a given statusLocation
def checkIfTargetAssetIsAvailable(assetLocation):
    targetAsset = Query("selection", "Asset", "location", assetLocation)
    if targetAsset['status_conveyorIN'] == "Available"
        return True
    else:
        return False
        
