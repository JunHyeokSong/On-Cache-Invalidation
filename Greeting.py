import time

# Function that not supports cache
def Greet(str):
    ret = ""
    if str == "Nick" :
        time.sleep(1)
        ret = "Hello!"
    elif str == "Minsu" :
        time.sleep(3)
        ret = "안녕하세요!"
    print(ret + " from " + str)
    return ret

if __name__ == "__main__" :
    Greet("Nick")   # Hello!
    Greet("Minsu")  # 안녕하세요!
