class Params(object):
    def __init__(self):
        self.percentCrossover = 0
        self.percentMutation = 0
        self.maxPopulation = 0
        self.maxGenerations = 0
        self.crossoverPoints = 0
        self.maxMutation = 0
        self.numberSelection = 0,
        self.wallPoint = 0
        self.offPoint = 0
        self.walkPoint = 0
        self.goalPoint = 0

   
    def getWalkPoint(self):
        return self.walkPoint

    def getOffPoint(self):
        return self.offPoint

    def getWallPoint(self):
        return self.wallPoint

    def getPercentCrossover(self):
       return self.percentCrossover

    def getPercentMutation(self):
        return self.percentMutation
        
    def getMaxPopulation(self):
        return self.maxPopulation
        
    def getMaxGenerations(self):
        return self.maxGenerations

    def getCrossoverPoints(self):
        return self.crossoverPoints

    def getMaxMutation(self):
        return self.maxMutation

    def getNumberSelection(self):
        return self.numberSelection

    def setPercentCrossover(self,percentCrossover):
        self.percentCrossover = percentCrossover

    def setPercentMutation(self,percentMutation):
        self.percentMutation =percentMutation
        
    def setMaxPopulation(self,maxPopulation):
        self.maxPopulation = maxPopulation
        
    def setMaxGenerations(self,maxGenerations):
        self.maxGenerations = maxGenerations

    def setCrossoverPoints(self,crossoverPoints):
        self.crossoverPoints = crossoverPoints

    def setMaxMutation(self,maxMutation):
        self.maxMutation = maxMutation

    def setNumberSelection(self,numberSelection):
        self.numberSelection = numberSelection

    def setGoalPoint(self,goalPoint):
        self.goalPoint = goalPoint

    def setWalkPoint(self,walkPoint):
        self.walkPoint = walkPoint
    
    def setOffPoint(self,offPoint):
        self.offPoint = offPoint

    def setWallPoint(self,wallPoint):
        self.wallPoint = wallPoint