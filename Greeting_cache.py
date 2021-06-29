import Greeting as gt

database = {}
def Greet_cache(str) :
    if str in database.keys() :
        print(database[str] + " from " + str)
    else :
        ret = gt.Greet(str)
        database[str] = ret

if __name__ == "__main__" :
    Greet_cache("Nick")   # 1s 
    Greet_cache("Nick")   # immediately 
    Greet_cache("Minsu")  # 3s
    Greet_cache("Minsu")  # immediately