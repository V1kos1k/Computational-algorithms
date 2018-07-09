#Методом Ньютона
#создание таблицы интерполированных значений по х
#интерполяция этих значений по у
#сложновато представить надо обрисовать
#но в принципе та же прошлая программа

def f(x,y):
    z = (x**3+y**2 - 6)
    return z

def tabl(xn, xk, yn, yk, kolx, koly):
    XY = []
    shx = (xk-xn)/(kolx-1)
    shy = (yk-yn)/(koly-1)
    xt = xn
    yt = yn
    i = 0
    XY.append(["   x/y"])
    while(yt <= yk):
        XY[i].append(yt)
        yt = yt+shy
    while(xt <= xk):
        yt = yn
        XY.append([xt])
        i = i+1
        while(yt <= yk):
            XY[i].append(f(xt,yt))
            yt = yt+shy
        xt = xt+shx
    
    return XY

def print_t(XY):
    for i in range(len(XY)):
        for j in range(len(XY[i])):
            if(i == 0 and j == 0):
                print("{:^8s} ".format(XY[i][j]), end = "")
            else:
                print("{:8.3f} ".format(XY[i][j]), end = "")
        print("")


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


def opr_x(XY, x, n):
    for i in range(1, len(XY)):
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

    if it-l_range < 1:
        inach = 1
    elif it+r_range > len(XY):
        inach = len(XY)-n
    else:
        inach = it - l_range
    #print("inach - ", inach)
    return inach

def opr_y(XY, x, n):
    for i in range(1, len(XY[0])):
        if x == XY[0][i]:
            it = i+1
            break
        
        if x < XY[0][i]:
            it = i
            break

    r_range = round(n/2)
    l_range = n - r_range
    #print("it - ", it)
    #print("ilr - ", l_range)
    #print("irr - ", r_range)

    if it-l_range < 1:
        inach = 1
    elif it+r_range > len(XY):
        inach = len(XY)-n
    else:
        inach = it - l_range
    #print("inach - ", inach)
    return inach

def poly_2(XY, x, y, nx, ny):
    xnach = opr_x(XY, x, nx)
    ynach = opr_y(XY, y, ny)
    #print(xnach," ", ynach)
    XY_pol = []
    for i in range(ynach, ynach+ny):
        XY_obr = []
        for j in range(xnach, xnach+nx):
            XY_obr.append([XY[j][0], XY[j][i]])
        #print(XY_obr)
        RR = razd_razn(XY_obr, nx,0)
        p = poly(RR, nx, x)
        XY_pol.append([XY[0][i], p])
    #print(XY_pol)
    RR = razd_razn(XY_pol, ny, 0)
    p = poly(RR, ny, y)
    return p
    


xn = -5
xk = 5
yn = 5
yk = 10
kolx = 11
koly = 6
XY = tabl(xn ,xk, yn, yk, kolx, koly)
print_t(XY)
t = 1
while(t == 1):
    nx = int(input("Введите степень полинома x: "))
    nx = nx+1;
    if(nx < 0):
        print("Степень полинома не может быть меньшей нуля!")
    elif(nx > kolx):
        print("Степень полинома слишком высока!")
    else:
        t = 0
t = 1
while(t == 1):
    ny = int(input("Введите степень полинома y: "))
    ny = ny+1;
    if(ny < 0):
        print("Степень полинома не может быть меньшей нуля!")
    elif(ny > koly):
        print("Степень полинома слишком высока!")
    else:
        t = 0

x = float(input("Введите х: "))
if(x < xn or x > xk):
    print("Х не входит в область определения таблицы")
else:

    y = float(input("Введите y: "))
    if(y < yn or y > yk):
        print("Y не входит в область определения таблицы")
    else:

        p = poly_2(XY, x, y, nx, ny)
        pt = f(x,y)
        print("Вычисленное значение - {:6.3f}".format(p))
        print("Точное значение - {:6.3f}".format(pt))
        print("Погрешность - {:6.3f}".format(abs(pt-p)))

