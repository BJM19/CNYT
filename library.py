from sys import stdin
import math
def suma(a,b):
    ar=a[0]+b[0]
    br=a[1]+b[1]
    return ar,br
def resta(a,b):
    ar=a[0]-b[0]
    br=a[1]-b[1]
    return ar,br
def imprimir(a,b):
    if b>0:
        return (str(a)+"+"+str(b)+"i")
    else:
        return (str(a)+"-"+str(abs(b))+"i")
def producto(a,b):
    ar=((a[0]*b[0])+((a[1]*b[1])*-1))
    br=((a[0]*b[1])+(a[1]*b[0]))
    print((a[0]*b[0]))
    print(((a[1]*b[1])*-1))
    return ar,br
def division(a,b):
    aux=((a[1]**2)+(b[1]**2))
    ar=((a[0]*a[1])+(b[0]*b[1]))/aux
    br=((a[1]*b[0])-(a[0]*b[1]))/aux
    return ar,br

def modulo(a):
    r=((a[0]**2)+(a[1]**2))**0.5
    return r
def conjugado(a,b):
    op=int(input("Conjugado de el 1 o 2 :"))
    if op==1:
        ar=a[0]
        br=a[1]*-1
    elif op==2:
        ar=b[0]
        br=b[1]*-1
    return ar,br
def opuesto(a,b):
    op=int(input("Opuesto de el 1 o 2 :"))
    if op==1:
        ar=a[0]*-1
        br=a[1]*-1
    elif op==2:
        ar=b[0]*-1
        br=b[1]*-1
    return r
def CartesianasAPolares(a,b):
    op=int(input("Conjugado de el 1 o 2 :"))
    if op==1:
       p=modulo(a)
       t=math.degrees(math.atan(a[0]/a[1]))
       ar=p*math.cos(t)
       br=p*math.sin(t)
    elif op==2:
       p=modulo(b)
       t=math.degrees(math.atan(b[0]/b[1]))
       ar=p*math.cos(t)
       br=p*math.sin(t)
    return p,t
def menu():
    print("1.Sumar")
    print("2.Resta")
    print("3.Producto")
    print("4.Division")
    print("5.Conjugado")
    print("6.opuesto")
    print("7.Modulo")
    print("8.Cartesianas a polares")
    print("9.Retornar Fase")
    print("10.Salir")
    op=int(input("Que opcion desea: "))
    return op
def main():
    n1=[int(i) for i in input("numero 1: ").strip().split()]
    n2=[int(i) for i in input("numero 2: ").strip().split()]
    op=-1
    while op!=10:
        op=menu()
        if op==1:
            r,i=suma(n1,n2)
            print(imprimir(r,i))
        elif op==2:
            r,i=resta(n1,n2)
            print(imprimir(r,i))
        elif op==3:
            r,i=producto(n1,n2)
            print(imprimir(r,i))
        elif op==4:
            r,i=division(n1,n2)
            print(imprimir(r,i))
        elif op==5:
            r,i=conjugado(n1,n2)
            print(imprimir(r,i))
        elif op==6:
            r,i=opuesto(n1,n2)
            print(imprimir(r,i))
        elif op==7:
            op=int(input("Modulo de el 1 o 2 :"))
            if op==1:
                r=modulo(n1)
            elif op==2:
                 r=modulo(n2)
            print(r)
        elif op==8:
            r,i=CartesianasAPolares(n1,n2)
            print(imprimir(r,i))
        elif op==9:
            r,i=RetornarFase(n1,n2)
            print(imprimir(r,i))
        elif op==10:
            break
        n1=[int(i) for i in input("numero 1: ").strip().split()]
        n2=[int(i) for i in input("numero 2: ").strip().split()]
    
main()
