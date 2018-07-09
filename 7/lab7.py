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

def print_t(IT):
    print("-"*85)
    s = "|    x    |    y    |                             y'(x)                             |"
    print(s) 
    s = "|         |         | Одност. | Центр. | Повыш. точн. | Ф-ла Рунге | Выравн. перем. |"
    print(s)
    print("-"*85)
    for i in range(len(IT)):
        s = "|{:^9.3f}|{:^9.3f}|"
        
        if IT[i][2] == "-":
            s += "{:^9}|"
        else:
            s += "{:^9.3f}|"

        if IT[i][3] == "-":
            s += "{:^8}|"
        else:
            s += "{:^8.3f}|"

        if IT[i][4] == "-":
            s += "{:^14}|"
        else:
            s += "{:^14.3f}|"

        if IT[i][5] == "-":
            s += "{:^12}|"
        else:
            s += "{:^12.3f}|"

        if IT[i][6] == "-":
            s += "{:^16}|"
        else:
            s += "{:^16.3f}|"
        
        s = s.format(IT[i][0], IT[i][1], IT[i][2], IT[i][3], IT[i][4], IT[i][5], IT[i][6])
        print(s)
    print("-"*85)

def prav_st(IT):
    h = IT[1][0] - IT[0][0]
    for i in range(len(IT)-1):
        IT[i].append((IT[i+1][1] - IT[i][1])/h)
    i += 1
    IT[i].append("-")
    return IT

def centr(IT):
    i = 0
    h = IT[1][0] - IT[0][0]
    IT[i].append("-")
    for i in range(1, len(IT)-1):
        IT[i].append((IT[i+1][1] - IT[i-1][1])/(2*h))
    i += 1
    IT[i].append("-")
    return IT

def kray(IT):
    h = IT[1][0] - IT[0][0]
    lk = (-3*IT[0][1] + 4*IT[1][1] - IT[2][1])/(2*h)
    IT[0].append(lk)
    for i in range(1, len(IT)-1):
        IT[i].append("-")
    i += 1
    pk = (3*IT[i][1] - 4*IT[i-1][1] + IT[i-2][1])/(2*h)
    IT[i].append(pk)
    return IT

def runge(IT):
    h = IT[1][0] - IT[0][0]
    r = 2
    p = 1
    for i in range(len(IT) - r):
        """
        for i in range(r):
            IT[i].append("-")
        """
    #for i in range(r, len(IT)):
        j = 1
        r1 = (IT[i+j][1] - IT[i][1])/(IT[i+j][0] - IT[i][0])
        j += (r-1)
        r2 = (IT[i+j][1] - IT[i][1])/(IT[i+j][0] - IT[i][0])
        """
        r1 = (IT[i][1] - IT[i-j][1])/(IT[i][0] - IT[i-j][0])
        j += (r-1)
        r2 = (IT[i][1] - IT[i-j][1])/(IT[i][0] - IT[i-j][0])
        """
        ans = r1 + (r1-r2)/(r**p - 1)
        IT[i].append(ans)
    
    for i in range(len(IT) - r, len(IT)):
        IT[i].append("-")
    
    return IT
#кси
def ξ(x):
    y = x
    return y
#эта
def η(x):
    if(x <= 0):
        y = "-"
    else:
        y = log(x)
    return y

def ξp(x):
    y = 1
    return y

def ηp(x):
    if(x <= 0):
        y = "-"
    else:
        y = 1/x
    return y

def viravn(IT):
    T = []
    for i in range(len(IT)):
        e = ξ(IT[i][0])
        n = η(IT[i][1])
        if e == "-" or n == "-":
            IT[i].append("-")
        else:
            T.append([e, n])
    T = centr(T)
    IT[0].append("-")
    for i in range(1, len(IT)-1):
        ans = T[i][2]*(ξp(IT[i][0])/ηp(IT[i][1]))
        IT[i].append(ans)
    i += 1
    IT[i].append("-")
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
    return RR

def findx(XY, x):
    ans = -1
    for i in range(len(XY)):
        if XY[i][0] == x:
            ans = i
            return ans
    return ans

def zpol(M, A):
    for i in range(len(M)):
        for j in range(len(A)):
            if i != j:
                A[j] *= M[i]
    answ = 0
    for i in range(len(A)):
        answ += A[i]
    return answ

def pr(x, n, XY):
    inach = opr(XY, x, n)
    RR = RazdR(XY,  x, n)
    ans = 0
    for i in range(inach, inach+n-1):
        M = []
        A = []  
        for j in range(inach, i+1):
            M.append(x - XY[j][0])
            A.append(1)
        zm = zpol(M, A)
        ans += zm*RR[i-inach+2][0]
        #print(M)
        #print(RR)
        #print("zm = ", zm, ", RR[i-inach+2][0] = ", RR[i-inach+2][0])
    #print("ans = ", ans)
    return ans

"""
xn = 0
xk = 3
kol = 7
fname = "3.txt"
write_f(xn, xk, kol, fname)
"""


fname = "4.txt"
IT = read_t(fname)
XY = copyXY(IT)
#print(IT)
IT = prav_st(IT)
IT = centr(IT)
IT = kray(IT)
IT = runge(IT)
IT = viravn(IT)
if IT == -1:
    print("Функция не определена на всех данных значениях")
else:
    print_t(IT)



n = int(input("Введите количество узлов полинома: "))
if n < 2 or n > len(XY):
    print("Количество узлов полинома не может быть меньше 2 или больше размера таблицы!")
else:
    x = float(input("Введите x: "))
    f = 0
    if f == -1:
        print("Введеный х не найден в таблице!")
    else:
        yp = pr(x, n, XY)
        print("Производная - {:5.3f}".format(yp))
   
    
