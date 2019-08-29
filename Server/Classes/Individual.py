from .Util import Util
from .Genetic import Genetic

class Individual :
    # Cria um novo indivíduo
    def __init__(self,DNA):
        self.DNA = []
        self.Score = 0

        if DNA is None:
            self.generateDna()
        else :
            self.DNA = DNA
            self.mutation()
            
    
    #Retorna o score
    def getScore(self):
        return self.Score

    #Retorna o DNA
    def getDna(self):
        return self.DNA

    # Gera DNA aleatório
    def generateDna(self):
        for i in range(0,len(Genetic.Goal)):
            #print(self.DNA)
            #print(Genetic.Alphabet[Util.getRandomInt(0,len(Genetic.Alphabet)-1)])
            
            random = Util.getRandomInt(0,len(Genetic.Alphabet)-1)
            #print(random)
            alfabet = Genetic.Alphabet[random]
            #print(alfabet)
            self.DNA.append(alfabet)
        self.generateScore()
        
    
    # Calcula o score do DNA
    def generateScore(self):
        self.Score = 0
        max = len(self.DNA)
        for i in range(0,max):
            if self.DNA[i] == Genetic.Goal[i] :
                self.Score += 1
        self.isEquals()

    # Realiza a mutação do gene
    def mutation(self):
        for i in range(0,Genetic.MaxMutation):
            
            if Util.getRandomFloat(0,1) <= Genetic.PercentMutation:
                position = Util.getRandomInt(0,len(Genetic.Goal)-1)
                position2 = Util.getRandomInt(0,len(Genetic.Alphabet)-1)

                #print(self.DNA)
                #print("Pos1 - " + str(position))
                #print(self.DNA[position])
                #print("Pos2 - " + str(position2))
                #print(Genetic.Alphabet[position2])
                self.DNA[position] = Genetic.Alphabet[position2]
        self.generateScore()
        
    
    # Verifica se esse gene é a solução
    def isEquals(self):
        #print(self.DNA)
        #print(Genetic.Goal)
        #print(self.DNA == Genetic.Goal)
        if self.DNA == Genetic.Goal:
            Genetic.IsFound = True