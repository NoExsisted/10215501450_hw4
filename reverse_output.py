import numpy as np
#给定列表l = [1,2,3,4,5]
#for循环
l = [1, 2, 3, 4, 5]
l_reverse1 = []
print('for循环:', end = " ")
for i in range(len(l)):
    l_reverse1.append(l[len(l) - 1 - i])
print(l_reverse1)

#while循环
l_reverse2 = []
i = 0
print('while循环:', end = " ")
while(i < len(l)):
    l_reverse2.append(l[len(l) - 1 - i])
    i += 1
print(l_reverse2)

#数组切片
print('数组切片:', end = " ")
l = np.array([1, 2, 3, 4, 5])
print(l[-1 :: -1])