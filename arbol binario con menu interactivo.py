# Creamos una clase Tree
class Tree:
    # constructor para crear un nodo del arbol
    def __init__(self,data):
        self.data = data #raiz del arbol puede ser un numero
        self.derecha = None #Hoja
        self.izquierda = None # Hoja

    #Agregera nodos al arbol
    def add(self,data):
        if data < self.data:
            if self.izquierda is None:
                self.izquierda = Tree(data)
            else:
                self.izquierda.add(data)
        else:
            if self.derecha is None:
                self.derecha = Tree(data)
            else:
                self.derecha.add(data)
        
    def predecesor(self):
        if self.derecha is None:
            return self
        else:
            return self.derecha.predecesor()

    def sucesor(self):
        if self.izquierda is None:
            return self
        else:
            return self.izquierda.sucesor()

    def remove(self, data):
        nodo = self

        if data < self.data:
            self.izquierda = self.izquierda.remove(data)
        elif data > self.data:
            self.derecha = self.derecha.remove(data)
        else:
            if self.izquierda is not None and self.derecha is not None:
                nodotemporal = self
                nodoizquierda = self.izquierda.predecesor()
                self.data =  nodoizquierda.data
                nodotemporal.izquierda = nodotemporal.remove(nodoizquierda)
            elif self.izquierda is not None:
                nodo = self.izquierda
            elif self.derecha is not None:
                nodo = self.derecha
            else:
                nodo = None
        return nodo
# Funciones para cada recorrido del arbol
    def preorder(self, lista = list()):
        lista.append(self.data)

        if self.izquierda is not None:
            self.izquierda.preorder(lista)

        if self.derecha is not None:
            self.derecha.preorder(lista)

        return lista

    def inorder(self, lista = list()):

        if self.izquierda is not None:
            self.izquierda.inorder(lista)

        lista.append(self.data)

        if self.derecha is not None:
            self.derecha.inorder(lista)

        return lista
    
    def postorder(self, lista = list()):

        if self.izquierda is not None:
            self.izquierda.postorder(lista)

        if self.derecha is not None:
            self.derecha.postorder(lista)

        lista.append(self.data)
        return lista
#----------------------Bonus -----------------------------------
# arbol = Tree(75)

# arbol.add(50)
# arbol.add(26)
# arbol.add(47)
# arbol.add(30)
# arbol.add(28)
# arbol.add(100)
# arbol.add(80)
# arbol.add(150)
# arbol.add(89)
# arbol.add(85)
# arbol.add(98)

# preorder = arbol.preorder()
# print("Recorrido preorder", preorder)

# inorder = arbol. inorder()
# print("Recorrido inorden:",inorder)

# postorder= arbol.postorder()
# print("Recorrido postorden:",postorder)
#---------------------- Fin bonus ------------------- 


arbol = Tree(50)
import random

for i in range(0,100):
    arbol.add(random.randrange(1,100,1))
# Menu de opciones 
decidir = True
while (decidir):
    print("1- Realizaar barridos preorden - inorden - postorden \n 2- Buscar numero \n 3- Eliminar valores \n 4- Determinar la cantidad de veces que se repite un numero \n 5-Contar pares e impares \n 6- Salir del programa")
    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        print("Barridos")
        preorden = arbol.preorder()
        inorden = arbol.inorder()
        postorden = arbol.postorder()
        print(f"Barrido preorden: {preorden}")
        print(f"\nBarrido inorden: {inorden}")
        print(f"\nBarrido postorden: {postorden}")

    elif opcion == 2:
        print("Encontrar si un numero se encuentra en el arbol: ")
        buscar = int(input("Ingrese el numero: "))

        if buscar in preorden:
            print(f"{buscar} se encuentra en el arbol")
        else:
            print(f"{buscar} no se encuentra en el arbol")

    elif opcion == 3:# no funciona
        print("Ingresa el numero que desea eliminar")
        remove = int(input("Ingrese el numero: "))
        arbol.remove(remove)

    elif opcion == 4:
        print("Ingrese el numero que desea saber su numero de ocurrencias")
        ocurrencia = int(input("Ingrese el numero: "))
        print(F"El {ocurrencia} se repite {preorden.count(ocurrencia)} vez")

    elif opcion == 5:
        pares = 0
        impar = 0

        for valor in preorden:
            if valor %2 == 0:
                pares +=1
            else:
                impar +=1
        print(f"Hay {pares} numeros pares y {impar} numeros impares")

    elif opcion == 6:
        decidir =False
        print("El programa finalizo")
    
    else:
        print("Ingrese una opcion valida")





'''
#Borrador
carga de datos
for i in range(0,100):
    arbol.add(random.randrange(1,100,1))

print("Barridos")
preorden = arbol.preorder()
inorden = arbol.inorder()
postorden = arbol.postorder()

print(f"Barrido preorden: {preorden}")
print(f"\nBarrido inorden: {inorden}")
print(f"\nBarrido postorden: {postorden}")

arbol.remove(10)'''


'''arbol = Tree(60)
arbol.add(41)
arbol.add(16)
arbol.add(25)
arbol.add(53)
arbol.add(46)
arbol.add(55)
arbol.add(42)
arbol.add(74)
arbol.add(65)
arbol.add(63)
arbol.add(70)
arbol.add(62)
arbol.add(64)

preorder = arbol.preorder()
inorder = arbol.inorder()
postorder = arbol.postorder()

print("Recorrido en preorden: ", preorder)
print("Recorrido en inorden; ", inorder)
print("Recorrido en postorden: ", postorder)'''





                 

