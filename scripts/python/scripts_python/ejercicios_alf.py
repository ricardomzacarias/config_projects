#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:34:41 2023

@author: ricardo_parrot
"""

# =============================================================================
#                         Ejercicios de alf BUCLES                             
# =============================================================================

#%% 1. muestra tu nombre por pantalla 10 veces 
# WHILE
nombre='Ricardo'
# inicializamos la variable a=0, mientras la variable 'a' sea menor que 10 se mantenga en un bucle, ademas creamos una variable que permita el incremento de la variable 'a' para que podamos parar el bucle en cuestion e imprima el nombre
a=0
while a < 10:
    print(nombre)
    # print(a)
    a+=1
    # print(a)

#%% 1. muestra tu nombre por pantalla 10 veces 
# FOR
# mantenemos el bucle en un rango de 10 e imprimimos
for i in range(10):
    print('Ricardo Marin')

#%% 2. Escribe un programa que pregunte al usuario su edad y que lo muestre por pantalla desde que cumplio un año hasta su edad actual 
# FOR

# preguntamos la edad y mantenemos el bucle en el rango de la edad, de 0 a 30 y aunmentamos el valor de la iteracion para que empieze desde el numero 1, tambien podemos inicializar el for con 1 y no necesitariamos incrementar la interacion 'i+1'
# edad=int(input('indicame tu edad: '))
edad=30
for i in range(0,edad):
    print(i+1, end=' ')
print("\n")

#%% 2. Escribe un programa que pregunte al usuario su edad y que lo muestre por pantalla desde que cumplio un año hasta su edad actual 
# FOR

# mantenemos un rango indicado por el usuario y despues convertimos la iteracion en string para que poder concatenarla, tambien podemos usar ',' para concatenar sin el problema de concatenar diferentes tipos
edad=int(input('Dime tu edad: '))
for i in range(edad):
    print('Tu edad es ' + str(i))

#%% 2. Escribe un programa que pregunte al usuario su edad y que lo muestre por pantalla desde que cumplio un año hasta su edad actual
# WHILE

edad2=int(input('indicame tu edad: \n'))
# edad2=24
a=0
print('Tu edad es: \n')
while a < edad2:
    a+=1
    print(a,end=' ')

#%% 2. Escribe un programa que pregunte al usuario su edad y que lo muestre por pantalla desde que cumplio un año hasta su edad actual
# WHILE
edad3=int(input('indicame tu edad: \n'))
a=0
while a < edad3:
    a+=1
    print('Tu edad es:',a,'años')

#%% 3. Escribe un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares desde el 1 hasta ese numero, separados por comas

# FOR
# numero=int(input('indicame tu edad: \n'))
numero=20
for i in range(1,numero+1):
    i2=i%2
    if i2 == 1:
        print(i, end=',')

#%% 3. Escribe un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares desde el 1 hasta ese numero, separados por comas

# FOR

# n=int(input('dame un numero'))
n=20
# for i in range(0,n,2):
#     print(i+1, end=', ')

for i in range(1,n+1,2):
    print(i, end=', ')

# for i in range(n, -1, -1):
#     print(i, end=', ')
#%% 3. Escribe un programa que pida al usuario un numero entero positivo y muestre por pantalla todos los numeros impares desde el 1 hasta ese numero, separados por comas

# WHILE
a=-1
# numero=20-1
numero=int(input('numero: '))-1
while a < numero:
    a+=2
    print(a, end=', ')

#%% 4. Escribe un numero entero positivo y muestra la cuenta hacia atras de ese numero. 

# FOR
# numero=int(input('numero: '))
numero=20
# invertimos nuestro bucle comenzamos desde el numero entregado por el usuario hasta el '-1' y como no se cuenta el ultimo numero nos entregaria el '0'
for i in range(numero,-1,-1):
    a=i
    print(i, end=', ')
#%% 4. Escribe un numero entero positivo y muestra la cuenta hacia atras de ese numero.

# WHILE

numero=int(input('numero: '))+1
# numero=25+1
a=0
# condicion del bucle es mientras numero sea mayor que 
while numero > a:
    numero-=+1
    print(numero, end=', ')
#%% 5. Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual, y el numero de años y muestre por pantalla el capital obtenido en la inversion cada año que dura la inversion.

# FOR

# cantidad_invertir=float(input('cantidad_invertir: '))
# interes=float(input('interes: '))
# años=int(input('años: '))

cantidad_invertir=1000
interes=10
años=5

for i in range(años):
    # cantidad_invertir *=1 + interes / 100
    # es lo mismo que 
    cantidad_invertir = cantidad_invertir * (1 + interes / 100)
    print('Capital tras '+ str(i+1) + ' años: ' + str(round(cantidad_invertir,2)))

#%% 5. Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual, y el numero de años y muestre por pantalla el capital obtenido en la inversion cada año que dura la inversion.

# WHILE

#%% 6. escribe un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo, de altura el numero introducido

# FOR
# numero=int(input('numero: '))
n = 15
print('')
for i in range(1, n, 1):
    print(i*"*")

#%% 6. escribe un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo, de altura el numero introducido

# WHILE

# numero=int(input('numero: '))
a = 0
numero = 15
print()
while numero > a:
    # recordando que si queremos que vaya de atras hacia adelante, agregamos un - a nuestra variable 'numero', es lo mismo que 
    # numero = numero - 1 
    # numero = -52+1
    numero-=+1
    print(numero*'*')

#%% 7. escribe un programa que muestre por pantalla la tabla de multiplica de 1 al 10

# FOR
for i in range(1,11):
    for j in range(1,11):
        # investigar \t y print('')
        print(i*j, end='\t')
    print('')

#%% 7. escribe un programa que muestre por pantalla la tabla de multiplica de 1 al 10

# WHILE

#%% 8. Escribir un programa que pida al usuario un numero entero y muestre por pantalla un triangulo rectangulo como el de mas abajo

# FOR
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

for i in range(1,10,2):
    # print(i)
    for j in range(i,0,-2):
        print(j,end=' ')
    print('')
for x in range(10,1,-2):
    for z in range(0,x,2):
        print(x,end=' ')
    print('')
#%% 9. Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# WHILE
password=input('password: ')
key='holama'

while key not in password:
    password=''
    password=input('password: ')
#%%

# FOR

# for x in range(1,x):

#%% 10. Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero=int(input('dame un numero: '))
a= True
while a:
    if numero%2 == 0:
        print('Tu numero es primo')
        a = False 
    else:
        print('Tu numero no es primo')
        a = False
    