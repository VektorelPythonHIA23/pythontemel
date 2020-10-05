import math
def GeneratorFonk(a):
    i = 0
    while i<=a:
        yield (i,math.factorial(i))
        i+=1

for j in GeneratorFonk(10):
    print(j)

x = GeneratorFonk(8)
print("1",x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

import random as rnd
def SayiAl():
    liste = [i for i in range(1,50)]
    sonuc = rnd.sample(liste,6)
    for i in sonuc:
        yield i

def LotoOyna(KolonSay=1):
    for i in range(KolonSay):
        liste = []
        for j in SayiAl():
            liste.append(j)
        liste.sort()
        yield liste

for kolon in LotoOyna(5):
    print(kolon)


class SayiUret:
    def __init__(self):
        import random as rnd
        self.sayilar = [i for i in range(1,50)]
        self.liste = rnd.sample(self.sayilar,6)
        self.a = 0
    def __iter__(self):
        self.liste = rnd.sample(self.sayilar,6)
        self.a = 0
    def __next__(self):
        try:
            return self.liste[self.a]
        except:
            raise StopIteration
        finally:
            self.a += 1
iterimiz = SayiUret()
while True:
    try:
        print(next(iterimiz))
    except StopIteration:
        break