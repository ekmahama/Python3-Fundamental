accronyms = {
    'lol': "Laugh out Loud",
    'idk': "I don't know",
    "tbh": "To be honest"
}


def CallAccronyms(key):
    try:
        accronyms[key]
    except:
        raise Exception("Specified key does not exist")



def divisor_remainder(a, b):
    if a == 0:
        raise ZeroDivisionError
    q = a//b
    r = a% b
    print(f"{a}/{b} is {q} remainder {r}")


if __name__ == "__main__":
    CallAccronyms("lol")
    #CallAccronyms("lop")
    divisor_remainder(3,2)
    #divisor_remainder(3,0)






