class Workpiece:
    
    workpieceId = ""
    workpiecePreset = ""
    stepIndex = 0
    AMRTaskList = []
    moreSteps = True
    error = 0
    
    # in the following example of a action list the files have been replace with single variables for the purpose of the demonstrator
    chairlegInstruction = [["EM1001", "FILE1"], ["EM1002", "FILE2"], ["EM1001", "FILE3"]]
    
    def __init__(self, workpiecePreset, orderId): 
        self.stepIndex = 0
        self.moreSteps = True
        self.error = 0  
        self.workpiecePreset = workpiecePreset
        self.orderId = orderId
        self.workpieceId = generateNewID("WP", "Workpiece")

        workpiece.getpreset(workpiecePreset)
        self.actionList = workpiece.getActionList(workpiecePreset)
        workpiece.createAMRTasks(actionList)
        uploadNewWorkpieceToDatabase(workpieceId, workpiecePreset, orderId)

    #def definePreset(CheckNewPreset, presetID, file) 
    #CheckNewPreset ==1 If new workpiece defined. ==0 if not.
    #   name
    #   

    #   if CheckNewPreset == 1:PresetID would be left blank in this case
            #function to define new presetID and store preset
            #
            #

    #   else if CheckNewPreset == 0: #
    #       #search for Preset and return action list
    #       querystatement = "FIND preset with PresetId = {} RETURN actionList".format(presetId)
    #       workpiece.actionlist = Query("presets", "selection", querystatement)
    
    #-----------------------------------------------------------------------------------------------------
    # # this is the code that would be used if we had our presets in our cloud database
    # def createActionList(workpiecePreset): #Created up creation of workpiece.
    #     query = queryQuery(“selection”, workpiecePreset)
    #-----------------------------------------------------------------------------------------------------
    
    def getActionList(workpiecePreset)
        querystatement = {"workpiecePreset":workpiecePreset}
        actionList = Query("selection","WorkpiecePreset",querystatement)
        return actionList

    def createAMRTaskList(actionList): #To create an AMR task list we need to know the action list
        AMRTaskIdList = []
        for i in length(actionList) -1
	        startingAsset = Query(“selection”,”assets”, {“location”: actionList[i][1]})
	        endingAsset = Query(“selection”,”assets”, “location”, actionList[i+1][1])
	        newAMRTask = AMRTask(workpiece.generateNewID(), startingAsset.location, endingAsset.location, workpieceId)# TODO: make sure the id creation is fixed
            AMRTaskList.append(AMRTask(endingAsset.location, startingAsset.location, workpieceId, notAvailable, ))


    def uploadNewWorkpieceToDatabase(workpieceId, workpiecePreset,orderId:
        queryStatement = {"workpieceId":workpieceId,"workpiecePreset":workpiecePreset,"stepIndex":0,"moreSteps":False,"error":0,"AMRTaskList":{},"orderId":orderId}
        Query("insertion", "Workpiece", queryStatement)      


    

    def gene
