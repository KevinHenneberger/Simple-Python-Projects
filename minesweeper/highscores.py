import json

class HighScores:

    def __init__(self):
        self.scoresFile = "scores.json"
        self.scoresFileR = open(self.scoresFile, "r")
        self.scoresDict = json.load(self.scoresFileR)
        self.scoresFileR.close()

    def outputData(self):
        """
        - returns a sorted array of tuples (name, score)
        """
        scoreList = []
        
        for score in self.scoresDict:
            scoreList.append((score, self.scoresDict[score]))

        scoreList = sorted(scoreList, key=lambda tup: int(tup[1]))

        return scoreList

    def addData(self, name, score):
        """
        - adds new data to the JSON file
        """
        scoreFileW = open(self.scoresFile, "w")
        self.scoresDict[name] = score
        json.dump(self.scoresDict, scoreFileW, indent=4)
        scoreFileW.close()
