## CNYT

# Calculadora de números complejos
Se realizo una calculadora para números complejos con las operaciones algebraicas mas conocidas y unas trasnformaciones.\

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
