# Practica 14 -Recursividad
---------------------------------------------------------
#sumatoria
---------------------------------------------------------
 def sumatoria(num):
     if num==1:
         return 1
     else:
         return num + sumatoria(num-1)
 num= int(input("Numero de la sumatoria:"))
 print(sumatoria(num))
 ---------------------------------------------------------
 # #factorial
---------------------------------------------------------
def factorial(n):
     if n==1:
         return 1
     else:
         return n * factorial(n-1)
 n= int(input("numero de factorial:"))
 print(factorial(n))
 ----------------------------------------------------------
#palindroma
---------------------------------------------------------
 def es_Palindroma(palabra):
     if len(palabra)>1:
         return True
     else:
         if palabra[0] == palabra [-1]:# si el caracter 
           return  es_Palindroma(palabra[1:-1])#Aumenta el 
         else:
           return False
 print(es_Palindroma('oxxo'))

---------------------------------------------------------
# #Fibonacci
---------------------------------------------------------
def fibonacci_recursivo(n):
     if n==0:
         return 0
     elif n==1:
         return 1
     else:
         return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
 print(fibonacci_recursivo(12))
---------------------------------------------------------
# #ejercicio propuesto:Elabore un algoritmo que pueda calcular el promedio de una lista la cual se ingresará desde consola tanto su longitud como su contenido
---------------------------------------------------------
lista =[]
 def promedio(num):
     if num <1:
         return calculo()
     else:
         valor = int(input("Ingrese el valor:"))
         lista.append(valor)
         return promedio(num-1)
 def calculo():
     suma_valores = 0
     for valor in lista:
         suma_valores += valor
     print(suma_valores/ num)
 num = int(input("cuantos numeros ingresara:"))
 promedio(num)
---------------------------------------------------------
# Juego De Aciertos
---------------------------------------------------------
def jugar(intento=1):
     respuesta = input("¿De que color es una naranja?")
     if respuesta != "naranja":
         if intento <3:
             print("\n Fallaste intentalo de nuevo")
             intento +=1
             jugar(intento) #llamada recursiva
         else:
             print("\n Perdiste")
     else:
         print("\n Ganaste!!")
 jugar()

