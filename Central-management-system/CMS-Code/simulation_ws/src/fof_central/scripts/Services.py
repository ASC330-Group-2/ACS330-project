()""

from datetime import datetime

def next_amr_task(assetId):
    nextAMRTaskFound = 0
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
