from math import sin, cos, exp
from numpy import linspace
def f1(x, y):
    #r =  x**3+y+1
    r =  x - y -0.33
    return r

def f2(x, y):
    #r =  exp(x) - 2*y + 1
    #print("x, exp(x)", x, exp(x))
    r =  x + y + 0.23
    return r

def poldel(a,b,eps, y, f):
    xp = a
    xs = b
    xt = (xs+xp)/2
    #xt = 1
    if abs(f(y, a)) < eps:
        return a
    if abs(f(y, b)) < eps:
        return b
    while(abs(xs-xp) > abs(xt)*eps + eps):
        xt = (xs+xp)/2
        if f(y, xs)*f(y, xt) < 0:
            xp = xt
        else :
            xs = xt
    return(xt)        

def tabl(xn, xk, sh_x, yn1, yn2, yk1, yk2, eps):
    XY = []
    xt = xn
    yt1 = yn1
    yt2 = yn2
    while(xt < xk):
        yt1 = poldel(yn1, yk1, eps, xt, f1)
        yt2 = poldel(yn2, yk2, eps, xt, f2)
        XY.append([xt, yt1, yt2, yt1 - yt2])
        #XY.append([xt, yt1, yt2, yt2 - yt1])
        xt = xt+sh_x
    return XY

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
            
def poly(RR, n, x):
    p = RR[1][0];
    for i in range(1, n):
        tek = 1
        for j in range(i):
            #print("(",x," - ", RR[0][j],")*",RR[i+1][0]) 
            tek = tek*(x-RR[0][j])
        p = p +tek*RR[i+1][0];
    return p;

def opr(XY, x, n):
    for i in range(len(XY)):
        if x == XY[i][0]:
            it = i+1
            break
        
        if x < XY[i][0]:
            it = i
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

xn = -2;
#xk = 0;
xk = 1
sh_x = 0.2
#yn1 = -2
#yn2 = 0
#yk1 = 8
#yk2 = 2
yn1 = -2
yn2 = 2
yk1 = 2
yk2 = -2
eps = 0.001

XY = tabl(xn, xk, sh_x, yn1, yn2, yk1, yk2, eps)
print("   x   ", " y1  ", " y2  ", " dy  ")
for i in range(len(XY)):
    if(i%1 == 0):
        print("{:5.3f}".format(XY[i][0]), "{:5.3f}".format(XY[i][1]), "{:5.3f}".format(XY[i][2]), "{:5.3f}".format(XY[i][3]))

TAB = []
for i in range(len(XY)):
    TAB.append([XY[i][3], XY[i][0]])
t = 1
kol = len(XY)
while(t == 1):
    n = int(input("Введите степень полинома: "))
    n = n+1;
    if(n < 0):
        print("Степень полинома не может быть меньшей нуля!")
    elif(n > kol):
       print("Степень полинома слишком высока!")
    else:
        t = 0
x = 0

inach = opr(TAB, x, n)
#print(inach)
#for i in range(len(TAB)):
    #print(TAB[i])
RR = razd_razn(TAB, n, inach)
#print(RR)
p = poly(RR, n, x)

TAB = []
for i in range(len(XY)):
    TAB.append([XY[i][0], XY[i][1]])
x = p
inach = opr(TAB, x, n)
RR = razd_razn(TAB, n, inach)
py = poly(RR, n, x)

print("Вычисленное значение x: {:6.4f}".format(p))
print("Вычисленное значение y: {:6.4f}".format(py))






