#Scropt: Number race

'''
Description:
randint: let you generate integer numbers
uniform: let you generate integer numbers 
'''
#fuctions:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#Dentro de las funciones no deben ir salidas
import os
from random import randint
#Functions:::::::::::::::::::::::::::::
def dices () :
    d1 = randint(1,6)
    d2 = randint(1,6)
    tot = d1 + d2
    sumat = 0
    return [d1, d2, tot]


#Main::::::::::::::::::::::::::::::::::

suma_t=[]
contador_pares= 0
contador_impares= 0

os.system("cls")
numero=int(input("***Ingresar el numero de veces a lanzar: "))
if (numero>=1):
    D = 1
    while D <= numero :
        print("Tiro Numero: ", D)
        
        dd = dices()
        suma_t.append(dd[2])
        print("Dado1: ", dd[0])        
        print("Dado2: ", dd[1])
        print("Total: ",dd[2])
        D = D + 1
        if dd[2]%2==0:
            contador_pares+=1
        else:
            contador_impares+=1
        if dd[0] &dd[1]==6:
            break
            
        key = input("==Lanzar nuevamente ==")
        if(dd[0]==6 and dd[1]==6):
           print("Dados iguales")
           break
        

    print("*********************************************")
    print("*** Valor total de lanzamientos: ",sum(suma_t))
    print("*** Total de pares: ",contador_pares)
    print("*** Total de impares: ", contador_impares)
    print("*********************************************")
else:
    print("El numero ingresado debe de ser mayor o igual a 1")


