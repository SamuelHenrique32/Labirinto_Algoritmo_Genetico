from .Individual import Individual
from .Genetic import Genetic
from .Util import Util


class Population :

    def __init__(self) :
        self.population = []
        self.numberGenerations = 1

        self.generateInitialPopulation()
    
    #Retora a geração
    def getGeneration(self):
        return self.numberGenerations

    #Retorna o primeiro da população
    def getFirst(self):
        return self.population[0]

    #Gera a população inicial
    def generateInitialPopulation(self):
        for i in range(0,Genetic.MaxPopulation):
            ind = Individual(None)
        #    print(ind.getScore())
            self.population.append(ind)
        #for i in range(0,Genetic.MaxPopulation):
        #    print(self.population[i].getScore())
        
        self.sortPopulation()
    
    #Ordena a população por score
    def sortPopulation(self):
        #for i in range(0,Genetic.MaxPopulation):
        #    print(self.population[i].getDna())
        
        self.population = sorted(self.population, key=lambda x: x.Score,reverse=True)
        
        #for i in range(0,Genetic.MaxPopulation):
        #    print(self.population[i].getDna())

    #Criação da nova geração
    def createNewGeneration(self):
        newGeneration = []
        if Genetic.Elitism:
            newGeneration.append(self.population[0])
        while len(newGeneration) <= Genetic.MaxPopulation:
            
            parents = self.selection()
            children=[]
            
            if Util.getRandomFloat(0,1) <= Genetic.PercentCrossover :
                DNA = self.crossver(parents)
                children.append(Individual(DNA[0]))
                children.append(Individual(DNA[1]))

            if len(children) == 0:
                newGeneration.append(parents[0])
                newGeneration.append(parents[1])
            else :
                newGeneration.append(children[0])
                newGeneration.append(children[1])
      
        self.population = newGeneration
        self.sortPopulation()

        self.numberGenerations = self.numberGenerations + 1

        self.isFinal()
    #Seleção por torneio
    def selection(self):
        selected = []
        for i in range(0,Genetic.NumberSelection):
            selected.append(self.population[Util.getRandomInt(0,Genetic.NumberSelection-1)])
        selected = sorted(selected, key=lambda x: x.Score, reverse=True)
        return [selected[0],selected[1]]
    
    #Verifica se chagou no numero de iteracoes maximas
    def isFinal(self):
        if self.numberGenerations >= Genetic.MaxGenerations:
            Genetic.IsFound = True
    
    #Crossver com n pontos
    def crossver(self,parents):
        child = []

        count = Genetic.CrossoverPoints+1
        first = 0
        last = int((len(Genetic.Goal)/count))

        DNA1 = []
        DNA2 = []
       
        for i in range(0,Genetic.CrossoverPoints+1):
            DNA1.append(parents[0].getDna()[first:last])
            DNA2.append(parents[1].getDna()[first:last])
            
            first = last
            last= last + int((len(Genetic.Goal)/count))

            if i == Genetic.CrossoverPoints-1:
                last = len(Genetic.Goal)
        status = True
        
        result1 = []
        result2 = []

        for i in range(0,len(DNA1)):
            if status :
                for j in DNA1[i]:
                    result1.append(j)
                for j in DNA2[i]:
                    result2.append(j)    
            else:
                for j in DNA1[i]:
                    result2.append(j)
                for j in DNA2[i]:
                    result1.append(j)
            status = not status

        #print("Pai 1")
        #print(parents[0].getDna())
        #print("Pai 2")
        #print(parents[1].getDna())

        #print("Result1")
        #print(result1)
        #print("Result2")
        #print(result2)

        return [result1,result2]