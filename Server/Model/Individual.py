from .Util import Util
from .Genetic import Genetic
import math
class Individual :
    # Cria um novo indivíduo
    def __init__(self,DNA):
        self.DNA = []
        self.Score = 0
        self.last = []

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
    
    def check_blockage(self,row_pos,col_pos):
            return (Genetic.Board[row_pos + 1][col_pos] == 1 or      # Return True if any move leads to a block
            Genetic.Board[row_pos - 1][col_pos] == 1 or      # If True, blocked is incremented by 1 and thus overall fitness score falls
            Genetic.Board[row_pos][col_pos + 1] == 1 or
            Genetic.Board[row_pos][col_pos - 1] == 1)

    def edge_maze(self,row_pos,col_pos,move):
            return((row_pos != len(Genetic.Board) -1 and move == "01") or     # To check if on edge.
           (row_pos != 0 and move == "11") or                # Used in combination with 'check_blockage()'
           (col_pos != len(Genetic.Board) -1 and move == "00") or  # As to not get indexing error
           (col_pos != 0 and move == "10"))

    def newScore2(self):
        Genetic.Position = [9,0]
        blocked = 0
        open_space = 0      
        no_back_forth = 0   
        cheese_distance = 0
        dist = 0
        index = 0

        for move in range(len(self.DNA) -1):
            if move == "01":
                index = 0
            elif move == "11":
                index = 1
            elif move == "01":
                index = 2
            elif move == "10":
                index = 3

            if Genetic.Position[0] >= 0 and Genetic.Position[0] <=9:
                if Genetic.Position[1] >= 0 and Genetic.Position[1] <=9:
                    p = Genetic.Board[Genetic.Position[0]] [Genetic.Position[1]]
                    if p[index] == 1:
                        blocked +=1
            
            if self.DNA[move + 1] != self.DNA[move]:
                if (self.DNA[move] in Genetic.Alphabet[0:2] and self.DNA[move + 1] in Genetic.Alphabet[2:4]):
                    no_back_forth +=1
            
            if Genetic.Position[0] != len(Genetic.Board) -1:  
                if self.DNA[move] == "01":  
                    Genetic.Position[0] += 1   
                    open_space += 1

            if Genetic.Position[0] != 0:
                if self.DNA[move] == "11":
                    Genetic.Position[0] -= 1
                    open_space += 1

            if Genetic.Position[1] != len(Genetic.Board[0]) - 1:
                if self.DNA[move] == "00":       # If the col_pos is end of row, going Right ('R') would lead to error
                    Genetic.Position[1] +=1               # Otherwise, move col_pos by 1
                    open_space +=1

            if Genetic.Position[1] != 0:
                if self.DNA[move] == "10":
                    Genetic.Position[1] -= 1
                    open_space += 1

        
        self.Score = open_space  + no_back_forth - blocked
        dist = abs(Genetic.Stop1[1] - Genetic.Position[1]) + abs(Genetic.Stop1[0] - Genetic.Position[0])

        #print(self.DNA)
        #print("Blocked: " + str(blocked))
        #print("No return: " + str(no_back_forth))
        #print("Open: " + str(open_space ))
        #print("Dist: " + str(dist))
        for point in range(len(Genetic.Goal), dist, -1):
            self.Score += 1

        if self.Score < 0:
            self.Score = -1

        if Genetic.Position == Genetic.Stop1:
                self.Score += len(self.DNA)

        #print("Score: "+ str(self.Score))      
        
    
   

    def newScore(self):
        Genetic.Position = [9,0]
        self.Score = 0

        #lista de pontos passados
        self.last = [[9,0]]
        
        #numero de vezes volta
        repited = 0

        #numero de paredes atravessadas
        wall = 0

        #numero de saidas do tabuleiro
        out = 0

        #Numero de blocos ocupados no eixo x
        sizex = 0

        #Numero de blocos ocupados no eixo x
        sizey = 0

        for i in range(0,len(self.DNA)):
            #realiza o movimento
            mov = self.newPosition(self.DNA[i])
            #print(str(i) + " - "+ str(self.DNA[i]) + " - " + str(Genetic.Position) + " -> " + str(mov))

            #verifica se está dentro do tabuleiro
            if mov[0] >= 0 and mov[0] <= 9 and mov[1] >= 0 and mov[1] <= 9:
                #verifica se a casa já foi percorrida
                if self.rep(mov):
                    #movimento válido
                    self.last.append(mov)
                    Genetic.Position = mov

                    if self.isWall(self.DNA[i]):
                        wall = wall + Genetic.WallPoint
                        #print("Movimento com parede")
                else:
                    repited = repited + Genetic.WalkPoint
                    #print("Movimento Repetido")

            else:
                #print("Movimento fora do tabuleiro")
                out = out + Genetic.OffPoint
            
        x = []
        y = []

        if len(self.last) > 0:
            for j in range (0,len(self.last)):
                x.append(self.last[j][0])
                y.append(self.last[j][1])
            
                sizex = max(x) - min(x)
                sizey = max(y) - min(y)

        #print("Casas repetidas - " + str(repited) + "/" + str(len(self.DNA)))
        #print("Passagens pelas paredes - " + str(wall)+ "/" + str(len(self.DNA)))
        #print("Saidas do Tabuleiro - " + str(out)+ "/" + str(len(self.DNA)))
        #print("Linhas ocupadas - " + str(sizex))
        #print("Colunas ocupadas - " + str(sizey))
        #print("Casas visitadas - " +str(len(self.last))+ "/" + str(len(self.DNA)))
        soma  = repited + wall + out
        self.Score  = self.Score  - soma 
        self.Score  = self.Score + sizex + sizey


        if Genetic.Position == Genetic.Stop1:
                #print("Position - " + str(Genetic.Position))
                #print("Stop - " + str(Genetic.Stop1))
                self.Score = self.Score + Genetic.GoalPoint
        #print(self.Score)
    def rep(self,mov):
        out = True
        for i in range(0,len(self.last)-1):
            if self.last[i] == mov:
                out = False
        return out

    def isWall (self,move):
        wall = False
        if move == "01":
            if Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][0] == 1:
                wall = True
                #print(Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][0])
        elif move == "11":
            if Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][1] == 1:
                wall = True
                #print(Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][1])
        elif move == "00":
           if Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][3] == 1:
                #print(Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][3])
                wall = True
        elif move == "10": 
          if Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][2] == 1:
                #print(Genetic.Board[Genetic.Position[0]][Genetic.Position[0]][2])
                wall = True

        return wall
    def newPosition(self,move):
        mov = [0,0]
        if move == "01":
            mov[0] = Genetic.Position[0] - 1
            mov[1] = Genetic.Position[1] 
        elif move == "11":
            mov[0] = Genetic.Position[0] + 1
            mov[1] = Genetic.Position[1] 
        elif move == "00":
            mov[0] = Genetic.Position[0] 
            mov[1] = Genetic.Position[1] + 1
        elif move == "10": 
            mov[0] = Genetic.Position[0] 
            mov[1] = Genetic.Position[1] - 1
        
        return mov
    
    
    #generate new score 
    def newScore3(self):
        self.last = []
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
            
            #print("Anterior")
            #print(self.last)
            a = True
            #print("Atual")
            #print(Genetic.Position)
            #print("Lista")
            for i in range(0,len(self.last)-1):
                #print(self.last[i])
                if self.last[i] == Genetic.Position:
                    a = False

            if a:
                #print("Não existe na lista")
                self.last.append(Genetic.Position)
            #else:
                #print("Já existe na lista")
        self.Score = self.Score + (-10 * (27 - len(self.last)))
        
        if(Genetic.Position == Genetic.Stop1):
            self.Score = self.Score + Genetic.GoalPoint
             
        dist = abs(Genetic.Stop1[1] - Genetic.Position[1]) + abs(Genetic.Stop1[0] - Genetic.Position[0])
        self.Score = self.Score + (27 - dist)
        #self.Score = self.Score + abs((Genetic.Stop2[0] - Genetic.Position[0])) + abs((Genetic.Stop2[1] - Genetic.Position[1]))
        #diff = 27 - len(self.walked)
        #print(self.Score)
        #self.Score = self.Score + (-100 * diff) 
        #print (len(self.walked))
        #print(diff)
        #print(diff)
    def up(self):
        #print("up")
        Genetic.Position = [Genetic.Position[0] -1 ,Genetic.Position[1]]
        val = self.returnVal(0,Genetic.Position)
        #self.walked.append([Genetic.Position[0] -1 ,Genetic.Position[1]])
        #print(val)
        return val

    def down(self):
        #print("down")
        Genetic.Position = [Genetic.Position[0] +1 ,Genetic.Position[1]]
        val = self.returnVal(1,Genetic.Position)
        #self.walked.append([Genetic.Position[0] +1 ,Genetic.Position[1]])
        #print(val)
        return val 
    
    def right(self):
        #print("right")
        Genetic.Position = [Genetic.Position[0] ,Genetic.Position[1] +1]
        val = self.returnVal(3,Genetic.Position)
        #self.walked.append([Genetic.Position[0] ,Genetic.Position[1] +1])
        return val
    
    def left(self):
        #print("left")
        Genetic.Position = [Genetic.Position[0] ,Genetic.Position[1]-1]
        val = self.returnVal(2,Genetic.Position)
        #self.walked.append([Genetic.Position[0] ,Genetic.Position[1]-1])
        #print(val)
        return val

    def exists(self,arr):
        #print("Position")
        #print(arr)
        #print("Table")
        e = False    
        for i in range(0,len(self.walked)):
            if self.walked[i] == arr:
                e = True
        
        if e :
            self.walked.append(arr)
        
    def returnVal(self,position,arr):
        if Genetic.Position[0] >= 0 and Genetic.Position[0] <= 9 and Genetic.Position[1] >= 0 and Genetic.Position[1]<=9:

            val = Genetic.Board[Genetic.Position[0]][Genetic.Position[1]]
            #print(val)
            #print(val[position])
            #if Genetic.Position == Genetic.Stop1 or Genetic.Position == Genetic.Stop2: 
                #print("500")
                #return Genetic.GoalPoint
            if val[position] == 1:
                #print("-20")
                return Genetic.WallPoint
            if val[position] == 0:
                #self.exists(arr)
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

                while  self.DNA[position] == Genetic.Alphabet[position2]:
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