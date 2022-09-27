ji = []
sum = 1
for i in range(100):
    if i % 2 == 1:
        ji.append(i)
        if i < 50:
            sum *= i
for i in range(len(ji)):
    if i == len(ji) - 1:
        print(ji[i])
    else:
        print(ji[i], end = " ")
print(sum)