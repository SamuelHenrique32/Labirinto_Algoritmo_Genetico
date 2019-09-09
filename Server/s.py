from bottle import Bottle, request, run, response
from truckpad.bottle.cors import CorsPlugin, enable_cors
from Model.Genetic import Genetic
from Model.Result import Result
from Model.Params import Params
from Model.Population import Population
from Model.Util import Util
import json



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
Genetic.MaxPopulation =  1000

#numero máximo de gerações
Genetic.MaxGenerations = 100

#número de corte no crossover
Genetic.CrossoverPoints = 3

#número de genes a serem mudades
Genetic.MaxMutation = 4

#número de filhos sortedos pelo torneio
Genetic.NumberSelection = 20

Genetic.WalkPoint = 10

Genetic.GoalPoint = 20

Genetic.WallPoint = -20

Genetic.OffPoint = -15

pop = Population()

app = Bottle()


@enable_cors
@app.route('/init', method=['GET', 'POST', 'OPTIONS'])
def init():
    if request.method == 'OPTIONS':
        # do something here?
        pass
    else:
        response.content_type = 'application/json'
        pop = Population()
        r = Result(pop.getFirst().getScore(),pop.getFirst().getDna(),pop.getGeneration(),Genetic.IsFound)
        return json.dumps(r.__dict__)

@enable_cors
@app.route('/next', method=['GET', 'POST', 'OPTIONS'])
def next():
   
    if request.method == 'OPTIONS':
        # do something here?
        pass
    else:
        response.content_type = 'application/json'
        pop.createNewGeneration()
        r = Result(pop.getFirst().getScore(),pop.getFirst().getDna(),pop.getGeneration(),Genetic.IsFound)
        return json.dumps(r.__dict__)

@enable_cors
@app.route('/params', method=['GET', 'POST', 'OPTIONS'])
def next():
   
    if request.method == 'OPTIONS':
        # do something here?
        pass
    elif request.method == 'GET':
        response.content_type = 'application/json'
        p = Params()
        p.setPercentCrossover(Genetic.PercentCrossover)
        p.setPercentMutation(Genetic.PercentMutation)
        p.setMaxPopulation(Genetic.MaxPopulation)
        p.setMaxGenerations(Genetic.MaxGenerations)
        p.setCrossoverPoints(Genetic.CrossoverPoints)
        p.setMaxMutation(Genetic.MaxMutation)
        p.setNumberSelection(Genetic.NumberSelection)
        p.setWalkPoint(Genetic.WalkPoint)
        p.setWallPoint(Genetic.WallPoint)
        p.setOffPoint(Genetic.OffPoint)
        p.setGoalPoint(Genetic.GoalPoint)
        return json.dumps(p.__dict__)
    elif request.method == 'POST':
        Genetic.PercentCrossover = float(request.json['percentCrossover'])
        Genetic.PercentMutation = float(request.json['percentMutation'])
        Genetic.MaxPopulation = int(request.json['maxPopulation'])
        Genetic.MaxGenerations = int(request.json['maxGenerations'])
        Genetic.CrossoverPoints =  int(request.json['crossoverPoints'])
        Genetic.MaxMutation = int(request.json['maxMutation'])
        Genetic.NumberSelection = int(request.json['numberSelection'])
        Genetic.GoalPoint = int(request.json['goalPoint'])
        Genetic.WalkPoint = int(request.json['walkPoint'])
        Genetic.OffPoint = int(request.json['offPoint'])
        Genetic.WallPoint = int(request.json['wallPoint'])
app.install(CorsPlugin())

run(app)