import random
n = 10000000
s = 1.0 * 2
sum = 0
for i in range(n):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 2.0)
    if(x**3 + x**2 >= y):
        sum += 1
result = sum * 1.0 / n * s
print(result)