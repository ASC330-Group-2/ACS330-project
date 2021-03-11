class Process:

    def __init__(self, assetId, testType):
        self.assetId = assetId
        self.testType = testType

    @property
    def assetId(self):
        return self.__assetId


    @assetId.setter
    def set_assetId(self, value):
        self.assetId = value
        
    @property
    def testType(self):
        return self.__testType


    @testType.setter
    def set_testType(self, value):
        self.testType = value
