import random

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