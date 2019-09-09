from Model.Genetic import Genetic
from Model.Population import Population
from Model.Result import Result
import json
def main():
        # Define a solução
        Genetic.Goal = ["01","01","01","00","00","01","01","00","01","10","10","10","01","00","00","00","00","00","11","00","00","01","00","00","11","11"]
       
        # Define os caracteres existentes
        Genetic.Alphabet = ["00","01","10","11"]
        
        # taxa de crossover
        Genetic.PercentCrossover = 0.85

        #taxa de mutação
        Genetic.PercentMutation = 0.045
        
        #elitismo
        Genetic.Elitism = True

        #tamanho da população
        Genetic.MaxPopulation =  2

        #numero máximo de gerações
        Genetic.MaxGenerations = 3

        #número de corte no crossover
        Genetic.CrossoverPoints = 3

        #número de genes a serem mudades
        Genetic.MaxMutation = 4

        #número de filhos sortedos pelo torneio
        Genetic.NumberSelection = 20

        Genetic.WalkPoint = 10

        Genetic.GoalPoint = 20

        Genetic.WallPoint = -20

        print(str(Genetic.Goal) +  " | Aptidão: " + str(len(Genetic.Goal)))
        
        pop = Population()

       

        print("Geração " + str(pop.getGeneration()) + " | Aptidão: " + str(pop.getFirst().getScore()) + " | Melhor: " + str(pop.getFirst().getDna()))

        #print("Teste")
        #print(pop.getFirst().getScore())
        while Genetic.IsFound != True:

            pop.createNewGeneration()

            print("Geração " + str(pop.getGeneration()) + " | Aptidão: " + str(pop.getFirst().getScore()) + " | Melhor: " + str(pop.getFirst().getDna()))
        
        if Genetic.IsFound :
            print("Solução encontrada")

        if pop.getGeneration() == Genetic.MaxGenerations:
            print("Número máximo atingido")

if __name__ == "__main__":
    main()