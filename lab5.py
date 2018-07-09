#сплайны

def f(x):
    return x**2 + 2*x - 2
    #return x**3 - 3*x + 2

def tabl(xn, xk, kol):
    XY = []
    sh = (xk-xn)/(kol-1)
    xt = xn
    while(xt <= xk):
        XY.append([xt, f(xt)])
        xt = xt+sh
    return XY

def print_t(XY, kazd):
    print("   x   ", " y   ")
    for i in range(len(XY)):
        if(i % kazd == 0):
            print("{:5.3f}".format(XY[i][0]), "{:5.3f}".format(XY[i][1]))

def opr(XY, x):
    for i in range(1, len(XY)):
        if XY[i-1][0] <= x < XY[i][0]:
            return i-1
    return len(XY)-1

def spline(XY, x, inach):

    hi = [0]
    #Шаг между x в табл.
    for i in range(1, len(XY)):
        hi.append(XY[i][0] - XY[i-1][0])

    #нахождение коэф. методом прогонки

    #начальные кси и эта из c1 = 0 и K = 1, M = 0, P = 0
    ksi = [0, 0, 0]
    eta = [0, 0, 0]

    #нахождение кси и эты
    for i in range(2, len(XY)):
        A = hi[i-1]
        B = -2*(hi[i-1]+hi[i])
        D = hi[i]
        F = -3*((XY[i][1]-XY[i-1][1])/hi[i] - (XY[i-1][1]-XY[i-2][1])/hi[i-1])
        ksi.append(D/(B - A*ksi[i]))
        eta.append((A*eta[i]+F)/(B - A*ksi[i]))
    """
    for i in range(len(XY)):
        print(A[i], " ", B[i], " ", D[i], " ", F[i])
    """

    """
    for i in range(len(eta)):
        print(eta[i], " ", end = "")
    print()
    """


    ci = []
    for i in range(len(XY)+1):
        ci.append(0)

    ci[1] = 0#eta и ci не оч., исправить
    ci[len(XY)] = 0 #т.к. eta[n] охожа на 2 гранич. условие на границах y'' = 0
    for i in range(len(XY)-1, 1, -1):
        #print(ksi[i+1], " ", ci[i+1], " ", eta[i+1]," ", end = "")
        ci[i] = ksi[i+1]*ci[i+1]+eta[i+1]
        #print(ci[i])

    ai = [0]
    bi = [0]
    di = [0]
    #Находим a, b, d
    for i in range(1, len(XY)):
        ai.append(XY[i-1][1])
        bi.append(  ( (XY[i][1] - XY[i-1][1]) / hi[i]) - (hi[i] / 3* (ci[i+1]+2*ci[i]) )  )
        di.append((ci[i+1]-ci[i])/(3*hi[i]))


    """
    print()    
    for i in range(len(ai)):
        print(ai[i])
    print()
    for i in range(len(bi)):
        print(bi[i])
    print()
    for i in range(len(ci)):
        print(ci[i])
    print()
    for i in range(len(di)):
        print(di[i])
    print()
    """
    IT = [ai, bi, ci, di]
    return IT
        

xn = -5
xk = 5
kol = 2

XY = tabl(xn, xk, kol)

print_t(XY, 1)
x = float(input("Введите х: "))
if(x <= xn or x >= xk):
    print("Х не входит в область определения таблицы")
else:
    inach = opr(XY, x)
    inach += 1
    IT = spline(XY, x, inach)
    p1 = x-XY[inach-1][0]
    res = IT[0][inach] + IT[1][inach]*p1 + IT[2][inach]*p1**2 + IT[3][inach]*p1**3
    print("Вычисленное значение f(x): {:6.4f}".format(res))
    print("Точное значение f(x): {:6.4f}".format(f(x)))
