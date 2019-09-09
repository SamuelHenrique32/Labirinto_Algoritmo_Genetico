from .Util import Util
from .Genetic import Genetic

class Individual :
    # Cria um novo indivíduo
    def __init__(self,DNA):
        self.DNA = []
        self.Score = 0
        self.walked = []

        if DNA is None:
            self.generateDna()
            #print(self.Score)
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
        #self.generateScore()
        self.newScore()
        
    
    # Calcula o score do DNA
    def generateScore(self):

        self.Score = 0
        #self.newScore()
        max = len(self.DNA)
        for i in range(0,max):
            if self.DNA[i] == Genetic.Goal[i] :
                self.Score += 1
        #self.isEquals()
    
    #generate new score 
    def newScore(self):
        self.walked = []
        #print("new score")
        self.Score = 0
        Genetic.Position = [9,0]
        max = len(self.DNA)
        #print(self.DNA)
        for i in range(0,max):
            if self.DNA[i] == "01":
                #print("up")
                val = self.up()
                #print (val)
                self.Score = self.Score + val
                #print(self.Score)
            elif self.DNA[i] == "11":
                #print("down")
                val = self.down()
                #print (val)
                self.Score = self.Score + val 
                #print(self.Score)
            elif self.DNA[i] == "00":
                #print("rigth")
                val = self.right()
                #print(val)
                self.Score = self.Score + val
                #print(self.Score)
            elif self.DNA[i] == "10": 
                #print("left")
                val = self.left()
                #print(val)
                self.Score = self.Score + val
                #print(self.Score)

    def up(self):
        #print("up")
        Genetic.Position = [Genetic.Position[0] -1 ,Genetic.Position[1]]
        val = self.returnVal(0,Genetic.Position)
        self.walked.append([Genetic.Position[0] -1 ,Genetic.Position[1]])
        #print(val)
        return val

    def down(self):
        #print("down")
        Genetic.Position = [Genetic.Position[0] +1 ,Genetic.Position[1]]
        val = self.returnVal(1,Genetic.Position)
        self.walked.append([Genetic.Position[0] +1 ,Genetic.Position[1]])
        #print(val)
        return val 
    
    def right(self):
        #print("right")
        Genetic.Position = [Genetic.Position[0] ,Genetic.Position[1] +1]
        val = self.returnVal(3,Genetic.Position)
        self.walked.append([Genetic.Position[0] ,Genetic.Position[1] +1])
        return val
    
    def left(self):
        #print("left")
        Genetic.Position = [Genetic.Position[0] ,Genetic.Position[1]-1]
        val = self.returnVal(2,Genetic.Position)
        self.walked.append([Genetic.Position[0] ,Genetic.Position[1]-1])
        #print(val)
        return val

    def exists(self,arr):
        e = False
        
        #print("Arr")
        #print(arr)

        for i in range(0,len(self.walked)):
            #print("walked")
            #print(self.walked[i])
            if self.walked[i] == arr:
                e = True
        
        return e;
    def returnVal(self,position,arr):
        if Genetic.Position[0] >= 0 and Genetic.Position[0] <= 9 and Genetic.Position[1] >= 0 and Genetic.Position[1]<=9:

            val = Genetic.Board[Genetic.Position[0]][Genetic.Position[1]]
            #print(val)
            #print(val[position])
            if Genetic.Position == Genetic.Stop1 or Genetic.Position == Genetic.Stop2: 
                #print("500")
                return Genetic.GoalPoint
            if val[position] == 1:
                #print("-20")
                return Genetic.WallPoint
            if val[position] == 0:
                if self.exists(arr):
                    return -10
                else:
                   return  Genetic.WalkPoint
        else:
            #print("-100")
            return Genetic.OffPoint
                            

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
        #self.generateScore()
        self.newScore()
        
    
    # Verifica se esse gene é a solução
    def isEquals(self):
        #print(self.DNA)
        #print(Genetic.Goal)
        #print(self.DNA == Genetic.Goal)
        if self.DNA == Genetic.Goal:
            Genetic.IsFound = True