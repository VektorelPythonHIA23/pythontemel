import os
print(os.getcwd())
liste = ["star"]
for item in liste:
    print(item)
    os.mkdir(item)