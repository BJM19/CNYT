import math
def suma(a,b):
    ar=a[0]+b[0]
    br=a[1]+b[1]
    return (ar,br)
def resta(a,b):
    ar=a[0]-b[0]
    br=a[1]-b[1]
    return (ar,br)
def producto(a,b):
    ar=((a[0]*b[0])+((a[1]*b[1])*-1))
    br=((a[0]*b[1])+(a[1]*b[0]))
    return (ar,br)
def division(a,b):
    ar=((a[0]*b[0]+a[1]*b[1])/(b[0]**2+b[1]**2))
    br=((b[0]*a[1]-a[0]*b[1])/(b[0]**2+b[1]**2))
    return (ar,br)
def modulo(a):
    r=((a[0]**2)+(a[1]**2))**0.5
    return r
def conjugado(a):
    ar=a[0]
    br=a[1]*-1
    return (ar,br)
def opuesto(a):
    ar=a[0]*-1
    br=a[1]*-1
    return (ar,br)
def cartesianasAPolares(a):
    h=((a[0]**2)+(a[1]**2))**0.5
    an=math.atan2(a[1],a[0])
    return an,(an*(180/math.pi))
def polaresACartesianas(a):
    h=a[0]
    alpha=a[1]*(math.pi/180)
    ar=h*math.cos(alpha)
    br=h*math.sin(alpha)
    return (ar,br)
def fase(a):
    ar=math.atan2(a[1],a[0])
    return (ar)
def adicionDeVectoresComplejos(a,b):
    res=[]
    if len(a)==len(b):
        for i in range(len(b)):
            res.append(suma(a[i],b[i]))
        return res
    else:
        raise "dimensiones invalidas"
def inverso(a):
    res=[]
    for i in range(len(a)):
        res.append(opuesto(a[i]))
    return res
def productoEscalar(a,b):
    ar=a[0]*b
    br=a[1]*b
    return (ar,br)
def escalarVector(a,b):
    res=[]
    for i in range(len(a)):
        res.append(productoEscalar(a[i],b))
    return res
def sumaDeMatrices(a,b):
    for i in range(len(a)):
        res=[]
        for j in range(len(b)):
            res.append(suma(a[i][j],b[i][j]))
    return res
def inversaMatriz(a):
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(opuesto(a[i][j]))
    return [res]
def multiplicacionEscalarMatrices(a,b):
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(producto(b,a[i][j]))
    return [res]
def productoInternoDeVectores(a,b):
    aux = []
    res = [0,0]
    if len(a)==len(b):
        for i in range(len(vec1)):
           aux.append(multiplicar(a[i],b[i]))
           resu = sumar(res,aux[i])
    return(res)
def traspuesta(a):
    m=[[0]*len(a[0])]*len(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            m[i][j]=a[j][i]
    return m
def conjugadaMatriz(a):
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(conjugado(a[i][j]))
    return [res]
def adjunta(a):
    return (conjugadaMatriz(traspuesta(a)))
def multiplicacionMatices(m1,m2):
    sol = []
    for i in range(len(m1)):
        l = []
        for j in range(len(m2[0])):
            aux = (0,0)
            for k in range(len(m2)):
                sumas= producto(m1[i][k],m2[k][j])
                aux= suma(sumas,aux) 
    
            l.append(aux)
        sol.append(l)
    return (sol)

def tensorVector(a,b):
    sol=[]
    for x in range(len(a)):
        for y in range(len(b)):
            sol.append(producto(a[x],b[y]))
    return sol

def tensorMatrices(a,b):
    sol=[]
    for i in range(len(a)):
        for j in range(len(b)):
             sol.append(tensorVector(a[i],b[j]))
    return sol
def potenciaCuadrada(num):
    return(producto(num,num))
def productoInternoEntreVectores(a,b):
    res = []
    if len(a)==len(b):
        cont = 0
        for i in range(len(a)):
            res = multiplicar(a[i],b[i])
    return (res)
def distanciaEntreDosVectores(a,b):
    res = []
    sol = [0,0]
    if len(a)==len(b):
        for i in range(len(vec1)):
            a.append(resta(a[i],b[i]))
        for j in range(len(resu)):
            solucion = suma(solucion,potenciaCuadrada(res[j]))
    sol[0]=sol[0]**0.5
    return (sol)
def normaDeVector(a):
    sol = [0,0]
    for i in range(len(a)):
        sol = suma(sol,potenciaCuadrada(a[i]))
    sol[0]=sol[0]**0.5
    return(sol)
def multiplicacionEntreMatriz(m1,m2):
    finnalMat = []
    for i in range(len(m1)):
        aux = []
        for j in range(len(m2[0])):
            cont = (0,0)
            for k in range(len(m2)):
                sums = multiplicar(m1[i][k],m2[k][j])
                cont = suma(sums,cont) 
            aux.append(cont)
        finnalMat.append(aux)
    return (finnalMat)
def esUnaHermitiana(m):
    if len(m) != len(m[0]):  raise ("La matriz no es cuadrada")
    return m == adjunta(matriz)
def esUnaUnitaria(m):
    if len(m) != len(m[0]):  raise ("La matriz no es cuadrada")
    i = [[(float(0),float(0)) for w in range(len(m))]for j in range(len(m))]
    for k in range(len(i)):
        i[k][k] = (float(1),float(0))
    return multiplicacionEntreMatriz(m,adjunta(matriz)) == multiplicacionEntreMatriz(adjunta(matriz),matriz) == i
def productoInternoEntreMatrices(m1,m2):
    adj = matrizAdjunta(m1)
    aux = multiplicacionEntreMatriz(adj,m2)
    res = (0,0)
    for i in range(len (aux)):
        res = suma(res,aux[i][i])
    return modulo(res)
def normaMatriz (m):
    return round(m.sqrt(productoInternoEntreMatrices(m,m)),2)
