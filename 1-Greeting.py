import time

# Function that not supports cache
def Greeting(str):
    timeCost = {"Nick" : 1, "Minsu": 3}
    if (str in timeCost.keys()):
        time.sleep(timeCost[str])
        print("Greeting of " + str)

Greeting("Nick")   # Hello!
Greeting("Minsu")  # 안녕하세요!
