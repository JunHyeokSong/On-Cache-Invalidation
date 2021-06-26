import time

def notSupportCache(str):
    timeCost = {"Nick" : 1, "Minsu": 3}
    if (str in timeCost.keys()):
        time.sleep(timeCost[str])
        print("Greeting of " + str)

notSupportCache("Nick")   # Hello!
notSupportCache("Minsu")  # 안녕하세요!
