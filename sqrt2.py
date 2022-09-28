#方法一：循环迭代，逐步逼近
def sqrt_1(num):
    times = 0
    g = 0
    for i in range(0, num + 1):
        if(i * i > num and g == 0):
            g = i - 1
    while(abs(g * g - num) > 0.0001):
        g += 0.00001
        times += 1
    print("times: %d   g = %.5f" % (times, g))

sqrt_1(2)

#方法二：二分法
def sqrt_2(num):
    times = 0
    max = num
    min = 0
    g = (max + min) / 2
    while(abs(g * g - num) > 0.00000000001):
        if(g * g < num):
            min = g
        else:
            max = g
        g = (max + min) / 2
        times += 1
    print("times: %d      g = %.13f" % (times, g))

sqrt_2(2) 

#方法三：曲线切线，线性逼近（牛顿法）如果（任意切点）切线与x轴的交点足够接近，即认为该点为f(x) = 0的根
#例：算根号2，num = 2，f(x) = x^2 - 2，f'(x) = 2x，设切点为(xk, yk)，yk = xk^2 - 2
#切线方程为y - yk = f'(x)(x - xk)，与x轴的交点(g, 0)满足yk + f'(x)(g - xk) = 0
#所以g = xk - yk / f'(x) = xk - (xk^2 - 2) / 2*xk = 1/2 * (xk + 2 / xk)
def sqrt_3(num):
    g = num / 2
    times = 0
    while(abs(g * g - num) > 0.00000000001):
        g = (g + num / g) / 2
        times += 1
    print("times: %d       g = %.13f" % (times, g))

sqrt_3(2)