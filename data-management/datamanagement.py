import json

class DataManagement:

    def __init__(self, jsonFile):
        self.jsonFile = jsonFile
        self.dataFileR = open(self.jsonFile, "r")
        self.dataDict = json.load(self.dataFileR)
        self.dataFileR.close()

    def outputData(self):
        dataList = []
        
        for entry in self.dataDict:
            dataList.append((entry, self.dataDict[entry]))

        dataList = sorted(dataList, key=lambda tup: int(tup[1]), reverse=True)
        
        for entry in dataList:
            print(entry[0] + ": " + str(entry[1]))

    def enterData(self, key, value):
        dataFileW = open(self.jsonFile, "w")
        self.dataDict[key] = value
        json.dump(self.dataDict, dataFileW, indent=4)
        dataFileW.close()
