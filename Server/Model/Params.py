class Params(object):
    def __init__(self,
                   goal,
               alphabet,
               percentCrossover,
               percentMutation,
               elitism,
               maxPopulation,
               maxGenerations,
               crossoverPoints,
               maxMutation,
               numberSelection):
        self.goal = goal
        self.alphabet = alphabet
        self.percentCrossover = percentCrossover
        self.percentMutation = percentMutation
        self.elitism = elitism
        self.maxPopulation = maxPopulation
        self.maxGenerations = maxGenerations
        self.crossoverPoints = crossoverPoints
        self.maxMutation = maxMutation
        self.numberSelection = numberSelection
    
    def getGoal(self):
        return self.goal
        
    def getAlphabet(self):
        return self.alphabet
        
    def getPercentCrossover(self):
       return self.percentCrossover

    def getPercentMutation(self):
        return self.percentMutation
        
    def getElitism(self):
        return self.elitism
        
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

    def setGoal(self,goal):
        self.goal = goal
        
    def setAlphabet(self,alphabet):
        self.alphabet = alphabet
        
    def setPercentCrossover(self,percentCrossover):
        self.percentCrossover = percentCrossover

    def setPercentMutation(self,percentMutation):
        self.percentMutation =percentMutation
        
    def setElitism(self,elitism):
        self.elitism = elitism
        
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
