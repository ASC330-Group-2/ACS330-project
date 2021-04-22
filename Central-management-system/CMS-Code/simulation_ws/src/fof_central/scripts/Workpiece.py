class Workpiece:
    
    workpieceId = ""
    workpiecePreset = ""
    stepIndex = 0
    actionList = [] = presetmongodb
    AMRTaskList = []
    moreSteps = True
    error = 0
    
    # in the following example of a action list the files have been replace with single variables for the purpose of the demonstrator
    chairlegInstruction = [["EM1001", "FILE1"], ["EM1002", "FILE2"], ["EM1001", "FILE3"]]
    
    def __init__(self, workpieceId, workpiecePreset): 
        self.workpieceId = workpieceId
        self.stepIndex = 0
        self.moreSteps = True
        self.error = 0  

        workpiece.getpreset(workpiecePreset)
        workpiece.createActionList(actionList)
        uploadNewWorkpieceToDatabase(workpieceId, workpiecePreset)




        

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
    
    def createAMRTaskList(actionList): #To create an AMR task list we need to know the action list
        AMRTaskIdList = []
        for i in length(actionList) -1
	        startingAsset = Query(“selection”,”assets”, “location”, assetList[i+1][1])
	        endingAsset = Query(“selection”,”assets”, “location”, assetList[i+1][1])
	        newAMRTask = AMRTask()
            
            AMRTaskList.append(AMRTask(endingAsset.location, startingAsset.location, workpieceId, notAvailable, ))


    def uploadNewWorkpieceToDatabase(workpieceId, workpiecePreset):
        queryStatement = "INSERT into Workpieces, workpieceId = {}, workpiecePreset = {}, stepIndex = 0, moreSteps = True, error = 0".format(workpieceId, workpiecePreset)
        Query("Insertion", "Assets", queryStatement)      


    

    def gene
