from math import exp
from math import log
def f(x):
    #y = exp(x)
    #y = 2*x
    y = 3*x**3 - 4*x**2 + 10*x - 5
    return y

def write_f(xn, xk, kol, fname):
    sh = (xk-xn)/(kol-1)
    xt = xn
    fl = open(fname, "w")
    #fl.write("   x       y       p   \n")
    for i in range(kol):
         s = "{:7.4f} {:7.4f}        \n".format(xt, f(xt))
         fl.write(s)
         
         xt = xt+sh
    fl.close()
    
def read_t(fname):
    fl = open(fname, "r")
    IT = []
    #line = fl.readline()
    for line in fl:
        l = line.split()
        if len(l) < 2:
            print("Неверный формат файла")
            fl.close()
        #print(l[0], " ", l[1], " ", l[2], "\n")
        T = [float(l[0]), float(l[1])]
        IT.append(T)
    return IT

def fact(a):
    s = 1
    if a != 0:
        s = a*fact(a-1)
    return s

def copyXY(IT):
    XY = []
    for i in range(len(IT)):
        XY.append([IT[i][0], IT[i][1]])
    return XY

def opr(XY, x, n):
    for i in range(len(XY)):
        if x == XY[i][0]:
            it = i+1
            break

    r_range = round(n/2)
    l_range = n - r_range
    #print("it - ", it)
    #print("ilr - ", l_range)
    #print("irr - ", r_range)

    if it-l_range < 0:
        inach = 0
    elif it+r_range > len(XY):
        inach = len(XY)-n
    else:
        inach = it - l_range
    #print("inach - ", inach)
    return inach

def razd_razn(XY, n, inach):
    RR = []
    T = []
    for i in range(n):
        T.append(XY[inach+i][0])
    RR.append(T)
    T = []
    for i in range(n):
        T.append(XY[inach+i][1])
    RR.append(T)
    T = []
    for i in range(n-1):
        T = []
        for j in range(n-i-1):
            #print(RR[i+1][j], " - ", RR[i+1][j+1]," / ", RR[0][j], " - ", RR[0][i+j+1])
            #print((RR[i+1][j]-RR[i+1][j+1])/(RR[0][j] - RR[0][i+j+1]))
            T.append((RR[i+1][j]-RR[i+1][j+1])/(RR[0][j] - RR[0][i+j+1]))
        RR.append(T)
    return RR

def RazdR(XY, x, n):
    inach = opr(XY, x, n)
    RR = razd_razn(XY, n, inach)
    #print(RR)
    return RR[n][0]

def findx(XY, x):
    ans = -1
    for i in range(len(XY)):
        if XY[i][0] == x:
            ans = i
            return ans
    return ans

def pr(x, n, XY):
    yp = fact(n-1)*RazdR(XY, x, n)
    return yp

"""
xn = 1
xk = 6
kol = 6
fname = "2.txt"
write_f(xn, xk, kol, fname)
"""


fname = "3.txt"
IT = read_t(fname)
XY = copyXY(IT)
n = int(input("Введите количество узлов полинома: "))
if n < 2 or n > len(XY):
    print("Количество узлов полинома не может быть меньше 2 или больше размера таблицы!")
else:
    x = float(input("Введите x: "))
    f = findx(XY, x)
    if f == -1:
        print("Введеный х не найден в таблице!")
    else:
        yp = pr(x, n, XY)
        print("Производная - {:5.3f}".format(yp))
    
    
