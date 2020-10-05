import time
import math

def zamanHesap(fonk):
    def icFonk(*args,**kwargs):
        begin = time.time()
        fonk(*args,**kwargs)
        end = time.time()
        print("bu işlem sırasında geçen zaman:",fonk.__name__,end-begin)

    return icFonk

@zamanHesap
def Faktoriyel(param):
    time.sleep(2)
    print(math.factorial(param))

@zamanHesap
def ConCat(*args):
    sonuc = ""
    for item in args:
        sonuc += ";" + item
    print(sonuc)

@zamanHesap
def JoinBir(*args):
    sonuc = ""
    sonuc = ";".join(args)
    print(sonuc)

JoinBir("ali","veli","ayşe")
ConCat("ali","veli","ayşe")