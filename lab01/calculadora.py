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
    aux=((a[1]**2)+(b[1]**2))
    ar=((a[0]*a[1])+(b[0]*b[1]))/aux
    br=((a[1]*b[0])-(a[0]*b[1]))/aux
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
    alpha=math.atan2(a[1]/a[0])
    ar=(a[0]**2+a[1]**2)**5
    br=alpha*(180/math.pi)
    return(ar,br)
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
def escalarVector(a,b):
    res=[]
    for i in range(len(a)):
        res.append(producto(b,a[i]))
    return res
def sumaDeMatrices(a,b):
    for i in range(len(a)):
        res=[]
        for j in range(len(b)):
            res.append(suma(a[i][j],b[i][j]))
    return [res]
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
           


