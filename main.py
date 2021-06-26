import time

def notSupportCache(str):
    timeCost = {"Nick" : 3, "Minsu": 5}
    if (str in timeCost.keys()):
        sleep(timeCost[str])