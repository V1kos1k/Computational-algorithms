from math import exp
from numpy import linspace
def f(x, y):
    #print(exp(x**3-y)-x**6+2*x**3*y+2*x**3-y**2-2*y-2)
    return exp(x**3-y)-x**6+2*x**3*y+2*x**3-y**2-2*y-2

def poldel(a,b,eps, y, sh_y):
    xp = a
    xs = b
    xt = (xs+xp)/2
    while(abs(xs-xp) > abs(xt)*eps + eps):
        xt = (xs+xp)/2
        if f(y, xp)*f(y, xt) < 0:
            xs = xt
        else :
            xp = xt
    return(xt)        
        

def tabl(xn, xk, sh_x, yn, sh_y, eps):
    XY = []
    XY.append([xn,yn])
    xt = xn+sh_x
    yt = yn
    rang = yn;
    while(xt <= xk+sh_x):
        yt = poldel(yt-rang, yt+rang, eps, xt, sh_y)
        rang = rang+sh_y
        XY.append([xt, yt])
        xt = xt+sh_x
    return XY

def trap(XY):
    s = 0
    s += (XY[0][1]+XY[len(XY)-1][1])/2
    for i in range(1, len(XY)-1):
        s += XY[i][1]
    s = s*sh_x
    return s

xn = 0;
xk = 2;
sh_x = 0.04
yn = -0.4
sh_y = 0.1
eps = 0.01

XY = tabl(xn, xk, sh_x, yn, sh_y, eps)
print("   x   ", " y   ")
for i in range(len(XY)):
    if(i%1 == 0):
        print("{:5.3f}".format(XY[i][0]), "{:5.3f}".format(XY[i][1]))
integr = trap(XY)
print("Integral - {:5.3f}".format(integr))


import matplotlib.pyplot as plt
    
plt.plot(XY)
plt.show()
