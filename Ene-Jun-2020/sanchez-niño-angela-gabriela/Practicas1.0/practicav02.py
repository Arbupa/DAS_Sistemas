n=int(input('Ingrese un numero base:'))
m=int(input('Ingrese numero de potencia:'))
def potencia(n,m):
    resultado=1
    i=0
    if m!=0:
        print("1")
    while True:
        resultado=n*resultado
        print(resultado)
        i=i+1
        
        if i>= abs(m):
            if m<0:
                resultado=1/resultado
                
                print(resultado)
                break
potencia(n,m) 