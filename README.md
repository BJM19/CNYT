

# Calculadora de números complejos
Se realizo una calculadora para números complejos con las operaciones algebraicas mas conocidas y unas trasnformaciones.


# Como se instala?
Para instalar esta libreria se realizan los iguientes pasos:

Entrar a la carpeta del ordenador donde deseamos descargar la libreria.
Utilizar el comando git clone, junto con el link de nuestra libreria (git clone https://github.com/BJM19/CNYT.git)
Una vez clonada la libreria, procedemos a abrir un editor de código.
Finalmente hacemos uso de la libreria.

En la primera version se manejan las siguientes operaciones
# Version 1
Las operaciones son:
1. **Suma**

Se realiza la suma de dos numeros complejos (a+b**i**)+(c+d**i**)

```
def suma(a,b):
    ar=a[0]+b[0]
    br=a[1]+b[1]
    return (ar,br)
```

2. **Resta**

Se realiza la resta de dos numeros complejos (a+b**i**)-(c+d**i**)
```
def resta(a,b):
    ar=a[0]-b[0]
    br=a[1]-b[1]
    return (ar,br)
```

3. **Producto**

Se realiza el producto de dos numeros complejos (a+b**i**)`*`(c+d**i**)

```
def producto(a,b):
    ar=((a[0]*b[0])+((a[1]*b[1])*-1))
    br=((a[0]*b[1])+(a[1]*b[0]))
    return (ar,br)
```

4.  **División**

Se realiza el division de dos numeros complejos (a+b**i**)/(c+d**i**)

```
def division(a,b):
    aux=((a[1]**2)+(b[1]**2))
    ar=((a[0]*a[1])+(b[0]*b[1]))/aux
    br=((a[1]*b[0])-(a[0]*b[1]))/aux
    return (ar,br)
```

5. **Conjugado**

Se realiza el conjugado de un número complejo conjugado(a+b**i**)

```
def conjugado(a):
    ar=a[0]
    br=a[1]*-1
    return (ar,br)
```

6. **Opuesto**


Se realiza el opuesto de un número complejo opuesto(a+b**i**)

```
def opuesto(a):
    ar=a[0]*-1
    br=a[1]*-1
    return (ar,br)
```

7. **Modulo**

Se realiza el modulo de un número complejo modulo(a+b**i**)

```
def modulo(a):
    r=((a[0]**2)+(a[1]**2))**0.5
    return r
```

8. **Cartesianas a polares**

Se realiza la coversion de cartesianas a polares

```
def cartesianasAPolares(a):
    alpha=math.atan(a[1]/a[0])
    ar=(a[0]**2+a[1]**2)**5
    br=alpha*(180/math.pi)
    return(ar,br)
```

9. **Polares a Cartesianas**

Se realiza la coversion de polares a cartesianas

```
def polaresACartesianas(a):
    h=a[0]
    alpha=a[1]*(math.pi/180)
    ar=h*math.cos(alpha)
    br=h*math.sin(alpha)
    return (ar,br)
```

10. **Retornar fase**

Se encuentra la fase

```
def fase(a):
    ar=math.atan2(a[1],a[0])
    return (ar)
```

# Version 2

1. **Adición de vectores complejos.**

Se realiza la suma de dos vectores complejos

```
def adicionDeVectoresComplejos(a,b):
    res=[]
    if len(a)==len(b):
        for i in range(len(b)):
            res.append(suma(a[i],b[i]))
        return res
    else:
        raise "dimensiones invalidas"
```

2. **Inverso (aditivo) de un vector complejo.**

Se realiza el inverso de un vector

```
def inverso(a):
    res=[]
    for i in range(len(a)):
        res.append(opuesto(a[i]))
    return res
```

3. **Multiplicación de un escalar por un vector complejo.**

Se realiza la multiplicacion de un escalar por un vector

```
def productoEscalar(a,b):
    ar=a[0]*b
    br=a[1]*b
    return (ar,br)
```

4. **Adición de matrices complejas.**

Se realizo la suma de dos matrices

```
def sumaDeMatrices(a,b):
    for i in range(len(a)):
        res=[]
        for j in range(len(b)):
            res.append(suma(a[i][j],b[i][j]))
    return res
```

5. **Inversa (aditiva) de una matriz compleja.**

Se realiza la inversa de una matriz 

```
def inversaMatriz(a):
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(opuesto(a[i][j]))
    return [res]
```

6. **Multiplicación de un escalar por una matriz compleja.**

Se realiza la multiplicacion de un escalar por un vector 

```
def multiplicacionEscalarMatrices(a,b):
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(producto(b,a[i][j]))
    return [res]
```

7. **Transpuesta de una matriz**

Se realiza la transpuesta de una matriz 

```
def traspuesta(a):
    m=[[0]*len(a[0])]*len(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            m[i][j]=a[j][i]
    return m
```

8. **Conjugada de una matriz**

Se realiza la conjugada de una matriz

```
def conjugadaMatriz(a):
    for i in range(len(a)):
        res=[]
        for j in range(len(a)):
            res.append(conjugado(a[i][j]))
    return [res]
```

9. **Adjunta (daga) de una matriz**

Se realza la adjunta de una matriz

```
def adjunta(a):
    return (conjugadaMatriz(traspuesta(a)))
```

10. **Producto de dos matrices (de tamaños compatibles)**

Se realiza la multiplicacion entre dos matrices

```
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
```

11. **Función para calcular la "acción" de una matriz sobre un vector.**

Se calcula la accion de una matriz sobre un vector

12. **Producto interno de dos vectores**

Se realiza el producto interno entre dos vectores

```
def productoInternoEntreVectores(a,b):
    res = []
    if len(a)==len(b):
        cont = 0
        for i in range(len(a)):
            res = multiplicar(a[i],b[i])
    return (res)
```

13. **Norma de un vector**

Se encuentra la norma entre dos vectores 

```
def normaDeVector(a):
    sol = [0,0]
    for i in range(len(a)):
        sol = suma(sol,potenciaCuadrada(a[i]))
    sol[0]=sol[0]**0.5
    return(sol)
```

14. **Distancia entre dos vectores**

Se encuentra la distancia entre dos vectores 

```
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
```

15. **Revisar si una matriz es unitaria**

Se comprueba si una matriz es unitaria 

```
def esUnaUnitaria(m):
    if len(m) != len(m[0]):  raise ("La matriz no es cuadrada")
    i = [[(float(0),float(0)) for w in range(len(m))]for j in range(len(m))]
    for k in range(len(i)):
        i[k][k] = (float(1),float(0))
    return multiplicacionEntreMatriz(m,adjunta(matriz)) == multiplicacionEntreMatriz(adjunta(matriz),matriz) == i
```

16. **Revisar si una matriz es Hermitiana**

Se comprueba si una matriz es hermitiana

```
def esUnaHermitiana(m):
    if len(m) != len(m[0]):  raise ("La matriz no es cuadrada")
    return m == adjunta(matriz)
```

17. **Producto tensor de dos matrices/vectores**

Se realiza producto tensor entre dos vectores o matrices 

```
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
```
# Licencia 

Todo el código incluido es código libre y puede ser usado por cualquier persona 

