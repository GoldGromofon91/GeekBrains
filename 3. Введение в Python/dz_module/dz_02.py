import random

def chekout(set):
        if set:
            result = random.choice(set)
            return result
if __name__=="__main__":
    print(chekout([1,2,3,7,9,10]))
    print(chekout([]))