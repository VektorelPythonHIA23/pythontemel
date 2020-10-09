










class A:

    def __init__(self,limit):
        self.limit = limit


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