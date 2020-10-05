# liste = [1,2,3]
# benim_iter = iter(liste)


# while True:
#     try:
#         print(next(benim_iter))
#     except StopIteration:
#         break


class A:
    def __init__(self,limit):
        self.limit = limit
        self.a = 0

    def __iter__(self):
        self.a = 3
        return self
    def __next__(self):
        a = self.a 
        if a > self.limit:
            raise StopIteration
        self.a = a+1
        return a


for i in A(8):
    print(i)

# class A:
#     pass
# print(*dir(A),sep="\n")
benim_iter = iter(A(8))
while True:
    try:
        print(next(benim_iter))
    except StopIteration:
        break
