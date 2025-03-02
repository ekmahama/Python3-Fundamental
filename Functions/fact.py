def factatorail(n):
    store = {0:1}
    if n in store:
        return store[n]
    store[n] = factatorail(n-1) * n
    return store[n]

def add(a,b):
    return a+b

def roll_dice():
    import random
    return random.randint(1,6)

# Positional Arguments
# Eg: test(1,2,3,4,5)
def test(*args):
    return args

# Keyword Arguments
# Eg: test(a=1,b=2,c=3,d=4,e=5)
def tsts(**kwargs):
    return kwargs

if __name__ == "__main__":
    print("5! :", factatorail(5),sep="")
    print("Add 5 and 6:", add(5,6),sep="")
    print("Roll Dice:", roll_dice(),sep="")
    print("Test:", test(1,2,3,4,5),sep="")
    print("Test:", tsts(a=1,b=2,c=3,d=4,e=5),sep="")