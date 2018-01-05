from datamanagement import DataManagement

def main():

    populationData = DataManagement("data.json")
    populationData.enterData("Austin", 931830)
    populationData.outputData()
    
main()
