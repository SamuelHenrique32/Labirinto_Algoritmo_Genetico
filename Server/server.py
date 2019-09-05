from Model.bottle import route,run,get,post,request,response
from Model.Genetic import Genetic
from Model.Result import Result
from Model.Params import Params
from Model.Population import Population
from Model.Util import Util
import json

p = Params( ["01","01","01","00","00","01","01","00","01","10","10","10","01","00","00","00","00","00","11","00","00","01","00","00","11","11"],
                ["00","01","10","11"],
                0.85,
                0.045,
                True,
                100,
                100,
                1,
                4,
                4)

@get('/init')
def init():
    response.content_type = 'application/json'
    Util.setProps(p)
    Genetic.Population = Population()
    r = Result(Genetic.Population.getFirst().getScore(),Genetic.Population.getFirst().getDna(),Genetic.Population.getGeneration(),Genetic.IsFound)
    return json.dumps(r.__dict__)

@get('/params')
def getParams():
    response.content_type = 'application/json'
    return json.dumps(p.__dict__)

@get('/next')
def nextPopulation():
    response.content_type = 'application/json'
    Genetic.Population.createNewGeneration()
    r = Result(Genetic.Population.getFirst().getScore(),Genetic.Population.getFirst().getDna(),Genetic.Population.getGeneration(),Genetic.IsFound)
    return json.dumps(r.__dict__)

@post('/params')
def setParams():
    p.setPercentCrossover(request.json['percentCrossover'])
    p.setPercentMutation(request.json['percentMutation'])
    p.setElitism(request.json['elitism'])
    p.setMaxPopulation(request.json['maxPopulation'])
    p.setMaxGenerations(request.json['maxGenerations'])
    p.setCrossoverPoints(request.json['crossoverPoints'])
    p.setMaxMutation(request.json['maxMutation'])
    p.setNumberSelection(request.json['numberSelection'])
    Util.setProps(p)

run(host='localhost', port=8080, debug=True)