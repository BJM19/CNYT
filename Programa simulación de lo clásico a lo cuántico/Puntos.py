#Ejercicio1
def producto(v1,v2):
    real=(v1[0]*v2[0])-(v1[0]*v2[0])
    ima=(v1[0]*v1[0])+(v2[0]*v1[0])
    return (real,ima)

def tensorMatrices(m1,m2):
    for x in range (len(m2)):
        for y in range(len(m2[0])):
            new=[]
            for z in range(len(m2)):
                for j in range(len(m2[0])):
                    new.append(producto(m1[x][y],m2[x][y]))
                m1[x][y]=new
    return m1
def vectorMatriz(a,b):
    if len(b)==len(a[0]):
        nueva=[[(0, 0)] * len(b[0]) for x in range(len(a))]
        for x in range(len(a)):
            for y in range(len(b[0])):
                for z in range(len(b)):
                    multi=producto(a[x][z],b[z][y])
                    nu=nueva[x][y]
                    nueva[x][y]=(multi[0]+nu[0],multi[1]+nu[1])
        return nueva
    else:
        return False
def productoMatriz(m1,m2):
    rows2=len(m2)
    columns1=len(m1[0])
    if rows2==columns1:
        nueva=[[(0, 0)] * len(m2[0]) for x in range(len(m1))]
        for x in range(len(m1)):
            for y in range(len(m2[0])):
                for z in range(len(m2)):
                    multi=multiplicacion(m1[x][z],m2[z][y])
                    nu=matriz[x][y]
                    nueva[x][y]=(multi[0]+nu[0],multi[1]+nu[1])                    
        return nueva 
    else:
        raise "Las dimensiones de las matrices son incorrectas"    
def modulo(a):
    return (int(a[0])**2+int(a[1])**2)**0.5
def multiply(tupla1,tupla2):
    return (float((tupla1[0]*tupla2[0])-(tupla1[1]*tupla2[1])),float((tupla1[0]*tupla2[1])+(tupla2[0]*tupla1[1])))
def multiplicacionMatrices(a,b):
    if len(b) == len(a[0]):
        m = [[(0, 0)] * len(b[0]) for x in range(len(a))]
        for i in range(0, len(a)):
            for j in range(0, len(b[0])):
                for k in range(0, len(b)):
                    multi = multiplicacion(a[i][k], b[k][j])
                    nu = m[i][j]
                    m[i][j] = (multi[0]+nu[0], multi[1]+nu[1])
        return m
    else:        
        raise 'Las longitudes de las matriz son diferentes'
    
def accionMatrizVector(m, v):    
    if len(m[0]) != len(m) != len(v):
        raise 'Operacion no definida'
    else:
        a = []
        for f in m:
            a.append(productoPunto(f, v))
        return a
    
def matrizTranspuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
            
def canicas(a,b,c):
    aux=a
    while b!=0:
        f=multiplicacionMatrices(aux,a)
        aux=f
        b=b-1
    return multiplicacionMatrices(aux,matrizTranspuesta(c))

def balas(a,b,c):
    aux=a
    while b!=0:
        f=multiplicacionMatrices(aux,a)
        aux=f
        b=b-1
    return multiplicacionMatrices(aux,matrizTranspuesta(c))

def dinamica(sis,ini,c):
    for x in range(c):
        ini=accionMatrizVector(sis,ini)
    return ini

def dobleRendija(a,c):
    for x in range(len(a)):
        for y in range(len(a[0])):
            for k in range(c):
                a[x][y] = multiply(a[x][y],a[x][y])
            a[x][y] = modulo(a[x][y])
    return a

def flash(a,b):
    aux=a
    while b!=0:
        sol=multiplicacionMatrices(aux,a)
        aux=sol
        b=b-1
    f=a
    for x in range(len(a)):
        for y in range(len(a[0])):
            mu=((a[x][y][0]**2)+(a[x][y][1]**2))**0.5
            f[x][y]=mu
    return f
def multiplesRendijas(r, b, v):
    #r rendija
    #b blancos
    #v vector probabilidad
    p = r + 1
    nds = 2 * r + p * b + 1
    b = len(v)
    sistema = [[(0, 0) for j in range(nds)]for i in range(nds)]
    posicion = 0
    for i in range(1, r + 1):
        sistema[i][0][0] = 1/(r**(1/2))
        posicion = i
    for i in range(1, r + 1):
        for j in range(posicion, posicion + b + 1):
            sistema[j][i] = v[i-1]                
    return sistema
#Ejercicio 2
def egval(e):
    return complex(e[0],e[1])
def prube(e):
    a=e[0]-0.1
    b=e[1]
    if b>0:
        b=b-0.1
    return (a,b)

def vectorComplex(v):
    tempo=0
    for i in range(len(v)):
        tempo=tempo+(v[i][0]**2+v[i][1]**2)

    return round((tempo**0.5),3)
def conjugado(a):
    for x in range(len(a)):
        for y in range(len(a[0])):
            b=a[i][j]
            c=b[0]
            d=b[1]*-1
            e=(c,d)
            a[x][y]=e
    return a
def simplifity(a, b):
    sol = [[(0, 0)] * len(a) for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            sol[i][j] = (a[i][j][0] - b[i][j][0], a[i][j][1] - b[i][j][1])
    return sol

def hermitiana(m):
    if len(a)==len(a[0]):
        trans=matrizTranspuesta(m)
        conju=conjugado(trans)
        if trans==m:
            return True
        else:
            return False
    else:
        return False

def particle(v):
    j = 1
    normal= vectorComplex(v)
    probabilidad = (j/(normal**2))
    return round(probabilidad, 4)


def normalize(v):
    j = 1
    norm = vectorComplex(v)
    new = [[]]
    for i in range(len(v)):
        op1 = (1/norm) * v[j][0]
        op2 = (1/norm) * v[j][1]
        new[0].append((round(op1, 3), round(op2, 3)))
    return new


def spin(v):
    return (round(( v[0][0]**2 + v[0][1]**2/vectorComplex(v)**2), 2),round((v[1][0]**2 + v[1][1]**2/vectorComplex(v)**2), 2))


def ident(c, m):
    sol = [[(0, 0)] * len(m) for x in range(len(m))]
    for x in range(len(m)):
        for y in range(len(m)):
            if x == y:
                sol[x][y] = (c, 0)
    return sol

#3 Ejercicio

def innerProduct(v1, v2):
    if len(v1) == len(v2):
        cont = (0, 0)
        for i in range(len(v1)):
            multi = producto(v1[i], v2[i])
            nu= (cont[0]+multi[0], cont[1]+multi[1])
            cont = nu
        return cont
    else:
        return False
def amplitudKet(nu1, nu2, k1, k2):
    k3 = k2
    return innerProduct(innerProduct(nu1, k1), innerProduct(nu2, k2))

def probabilidad(h, ket):
    r = vectorComplex(ket)
    x = ket[h]
    y = x
    proba = abs(producto(x, y)[0] + producto(x, y)[1])/(r ** 2)
    return proba
def varianza(M, v):
    if len(M) == len(v[0]):
        H = productoMatrices(M, matrizTranspuesta(v))
        w = [[]]
        for j in H:
            w[0].append(j[0])
        x = productoMatrices(matrizTranspuesta(w), v)
        E = x[0][0][0] + x[1][0][1]
        m1 = ident(E, M)
        N = simplifity(M, m1)
        Delta = productoMatrices(N, N)
        r = v
        for i in range(len(v)):
            for j in range(len(v[0])):
                x = v[i][j]
                c = x[0] ** 2
                t = x[1] ** 2
                r[i][j] = (c, t)
        Rf = productoMatrices(r, Delta)
        x = prube(Rf[0][0])
        return round(x[0], 2)
    else:
        return False
