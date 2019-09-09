from Model.bottle import route,run,get,post,request,response,app,Bottle
from Model.Genetic import Genetic
from Model.Result import Result
from Model.Params import Params
from Model.Population import Population
from Model.Util import Util
import json

app = Bottle()

p = Params( ["01","01","01","00","00","01","01","00","01","10","10","10","01","00","00","00","00","00","11","00","00","01","00","00","11","11"],
                ["00","01","10","11"],
                0.85,
                0.045,
                True,
                20000,
                70,
                3,
                4,
                30,
                0,
                0,
                10,
                0)


@get('/init')
def init():
    response.content_type = 'application/json'
    Genetic.IsFound = False
    Genetic.Population = []
    Util.setProps(p)
    Genetic.Population = Population()
    r = Result(Genetic.Population.getFirst().getScore(),Genetic.Population.getFirst().getDna(),Genetic.Population.getGeneration(),Genetic.IsFound)
    return json.dumps(r.__dict__)

@get('/next')
def nextPopulation():
    response.content_type = 'application/json'
    Genetic.Population.createNewGeneration()
    r = Result(Genetic.Population.getFirst().getScore(),Genetic.Population.getFirst().getDna(),Genetic.Population.getGeneration(),Genetic.IsFound)
    return json.dumps(r.__dict__)
    
run(host='localhost', port=8080, debug=True)