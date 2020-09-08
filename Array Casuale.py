import random

i=0
arr = []
num = 0
for i in range(1000):
    num = random.randint(0, 100)
    arr.append(num)
print("Array di 1000 elementi disordinati", arr)
arr.sort()
print("Array di 1000 elementi ordinato", arr)