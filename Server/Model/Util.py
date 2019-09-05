import random
import json
from Model.Genetic import Genetic

class Util:
    @staticmethod
    def getRandomInt(min,max):
        return random.randint(min,max)
    
    @staticmethod
    def getRandomFloat(min,max):
        return random.uniform(min,max)

    @staticmethod
    def concatStringList(list):
        result = ""
        for a in list:
            result += str(a)
        return result
    
    @staticmethod
    def setProps(props):
        # Define a solução
        Genetic.Goal = props.getGoal()
        
        # Define os caracteres existentes
        Genetic.Alphabet = props.getAlphabet()
        
        # taxa de crossover
        Genetic.PercentCrossover = props.getPercentCrossover()

        #taxa de mutação
        Genetic.PercentMutation = props.getPercentMutation()
        
        #elitismo
        Genetic.Elitism = props.getElitism()

        #tamanho da população
        Genetic.MaxPopulation =  props.getMaxPopulation()

        #numero máximo de gerações
        Genetic.MaxGenerations = props.getMaxGenerations()

        #número de corte no crossover
        Genetic.CrossoverPoints = props.getCrossoverPoints()

        #número de genes a serem mudades
        Genetic.MaxMutation = props.getMaxMutation()

        #número de filhos sortedos pelo torneio
        Genetic.NumberSelection = props.getNumberSelection()


