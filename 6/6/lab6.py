def f(x):
    y = x**3 - 2*x**2 + x/2 - 4
    return y

def phi(x, k):
    y = x**k
    return y

def write_f(xn, xk, kol, fname):
    sh = (xk-xn)/kol
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
        if len(l) < 3:
            print("Неверный формат файла")
            fl.close()
        #print(l[0], " ", l[1], " ", l[2], "\n")
        T = [float(l[0]), float(l[1]), float(l[2])]
        IT.append(T)
    return IT

def matr_c(IT, n):
    M = []
    for i in range(n):
        M.append([])
        for j in range(n):
            M[i].append(0)
            
    for i in range(n):
        for j in range(n):
            for k in range(len(IT)):
                M[i][j] += IT[k][2]*phi(IT[k][0], i+j)
                #print(i," ", j, " ", k," \n")
                #print(M[i][j])
    return M

def vect_c(IT, n):
    V = []
    for i in range(n):
        V.append(0)
    
    for i in range(n):
        for k in range(len(IT)):
            V[i] += IT[k][2]*phi(IT[k][0],i)*IT[k][1]
    return V

def upt(M, V, n):
    for i in range(n-1):
        max_n = i
        max_z = abs(M[i][i])
        for j in range(i+1, n):
            znach = M[j][i]
            if znach > max_z:
                max_n = j
                max_z = znach


        if max_n > i:
            t = M[i]
            M[i] = M[max_n]
            M[max_n] = t

            t = V[i]
            V[i] = V[max_n]
            V[max_n] = t
        else:
            if(abs(max_z) <= 1e-20):
                #print(M)
                return [[-1]]


        znach = M[i][i]
        for j in range(i+1, n):
            koef = M[j][i]/znach
            for k in range(n):
                M[j][k] -= M[i][k]*koef
            V[j] -= V[i]*koef
        #print("i: ",i, M)

    if abs(M[n-1][n-1]) <= 1e-20:
        #print(M)
        return [[-1]]
    return M

def gauss(M, V, n):
    M = upt(M, V, n)
    #print(M)
    #print(V)
    if M[0][0] == -1:
        return [[[-1]], [-1]]

    for i in range(n-1, -1, -1):
        if i != n-1:
            for j in range(i+1, n):
                V[i] -= M[i][j]*V[j]
        V[i] /= M[i][i]
    return [M, V]

def umn(A, B):
    C = []
    #print("A ", A)
    #print("B ", B)
    n1 = len(A)
    m1 = len(B)
    for i in range(n1):
        for j in range(1):
            s = 0
            for k in range(m1):
                s = s+(A[i][k]*B[k])
            C.append(s)
    return C

def slozh(A, B):
    C = []
    for i in range(len(A)):
         C.append(A[i]+B[i])
    return C

def psi(b, a, x):
    ax = umn(a,x)
    #print("ax ", ax)
    #print("b ", b)
    ps = []
    for i in range(len(ax)):
        ps.append(b[i] - ax[i])
    return ps

def itera(MB, VB, V):
    #pss = 10;
    #eps = 1e-20
    #print("V - vx",V)
    #while abs(pss) > eps:
    for i in range(4):
        ps = psi(VB, MB, V)
        print("ps - ", ps)
        MB1 = copy_m(MB)
        VB1 = copy_v(VB)
        T = gauss(MB1, ps, len(MB1))
        VT = T[1]
        V = slozh(VT, V)
        print("V - ", V)
        #pss = 0
        #for i in range(len(ps)):
        #    pss += ps[i]
        #print("pss - ",pss)
    return V

def copy_m(M):
    MC = []
    for i in range(len(M)):
        MC.append([])
        for j in range(len(M)):
            MC[i].append(M[i][j])
    return MC

def copy_v(V):
    VC = []
    for i in range(len(V)):
        VC.append(V[i])
    return VC
        


    

"""
xn = 0
xk = 10
kol = 11
fname = "4.txt"
write_f(0, 1, 5, fname)
"""


fname = "4.txt"
IT = read_t(fname)
#print(IT)

print("Введите степень полинома: ")
n = int(input())
if n < 0:
    print("Степень полинома не может быть меньшей нуля")
else:
    n = n+1
    M = matr_c(IT, n)
    V = vect_c(IT, n)
    MB = copy_m(M)
    VB = copy_v(V)
    #print(M)
    #print(V)
    T = gauss(M, V, n)
    M = T[0]
    V = T[1]
    V = itera(MB, VB, V)
    #print(M)
    #print(V)
    if V[0] == -1:
        print("Система не имеет решения")
    else:
        T = []
        for i in range(len(IT)):
            y = 0
            for j in range(n):
                y = y+(IT[i][0]**j)*V[j]
            T.append([IT[i][0], y, IT[i][2]])
        s = "f(x) = "
        for i in range(n):
            if i != 0:
                if V[i] >= 0:
                    s  = s+ " + "
            s = s+ "{:7.4f}*x**{} ".format(V[i], i)
        print(s)

        X1 = []
        Y1 = []
        Y2 = []
        for i in range(len(IT)):
            X1.append(IT[i][0])
            Y1.append(IT[i][1])

            Y2.append(T[i][1])
        import matplotlib.pyplot as plt
        plt.plot(X1, Y1, "r", label = "Исходная")
        plt.plot(X1, Y2, "b", label = "Найденная")
        plt.show()
        
    
    



