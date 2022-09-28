#方法一：格雷戈里-莱布尼茨级数
#pi / 4 = 1 - 1/3 + 1/5 -1/7 + ……
import math
import random
def Leibniz():
    n = 1
    pi = 0.0
    k = 1.0
    temp = 1.0
    while(abs(temp) > 1e-8):
        pi += temp
        k = -k
        n += 2
        temp = k / n
    pi *= 4
    #print("Leibniz: times: %d  pi = %.7f" % (n, pi))
    print("Leibniz: times: %d  pi =" % n, end = " ")
    print(str(pi).split(".")[0] + "." + str(pi).split(".")[1][:7])

Leibniz()

#方法二：圆周法
def cirle():
    m = 0
    pi = 0
    n = 0
    while(abs(pi - math.pi) > 1e-9):
        x = random.uniform(0.0, 1.0) #先算第一象限1/4个圆
        y = random.uniform(0.0, 1.0)
        if x**2 + y**2 <= 1:
            m += 1
        n += 1
        if m != 0:
            pi = 4 * m / n
    print("cirle: times: %d  pi =" % n, end = " ")
    print(str(pi).split(".")[0] + "." + str(pi).split(".")[1][:8])

cirle()

#方法三：投针法(与方法二同为蒙特卡洛法)
def needle():
    m = 0 #相交次数
    n = 0 #总次数
    l = 0.6 #针的长度
    a = 1.0 #两条线间距
    pi = 0.0
    while (abs(pi - math.pi) > 1e-7):
        dis = random.uniform(0.0, a / 2)
        deg = random.uniform(0.0, math.pi)
        if (l / 2) * math.sin(deg) >= dis:
            m += 1
        n += 1
        if m != 0:
            pi = (2 * n * l) / (m * a)
    #pi = (2 * n * l) / (m * a)
    #print("needle: times: %d  pi = %.7f" % (n, pi))
    print("Needle: times: %d  pi =" % n, end = " ")
    print(str(pi).split(".")[0] + "." + str(pi).split(".")[1][:8])

needle()

#方法四：BBP公式
def bbp():
    n = 7
    pi = 0
    for i in range(n):
        pi += 1/pow(16, i) * (4/(8*i + 1) - 2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6)) 
    #print("BBP: times: %d  pi = %.10f" % (n, pi))
    print("BBP: times: %d  pi =" % n, end = " ")
    print(str(pi).split(".")[0] + "." + str(pi).split(".")[1][:10])

bbp()

#方法五：梅钦级数法
def Machin():
    pi = 16 * math.atan(1 / 5) - 4 * math.atan(1 / 239)
    #print("Machin: times: %d  pi = %.10f" % (1, pi))
    print("Machin: times: 1  pi =", end = " ")
    print(str(pi).split(".")[0] + "." + str(pi).split(".")[1][:10])

Machin()