from nodo import Nodo#Importamos la clase Nodo

class Arbol:
    #Funciones privadas
  def __init__(self,dato):
    self.raiz=Nodo(dato)
    #funcion recursiva que nos permite agregar datos al arbol
    def __agregar_recursivo(self,nodo,dato):#Metodo que recibe el nodo y el dato a agregar
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda=Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha,dato)
    #METODOS DE RECORRIDO
    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)#Visitamos toda la izquierda
            print(nodo.dato,end=",") #Imprimimos nodo actual   
            self.__inorden_recursivo(nodo.derecha)#Visitamos toda la derecha
    
    def __preorden_recurrsivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=",")#Imprimimos nodo actual 
            self.__preorden_recursivo(nodo.izquierda)#Visitamos toda laizquierda
            self.__preorden_recursivo(nodo.derecha)#Visitamos toda la derecha
    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)#Visitamos toda la izquierda
            self.__postorden_recursivo(nodo.derecha)#Visitamos toda la derecha
            print(nodo.dato, end=",")#Imprimimos nodo actual
    #Metodo para buscar dentro del arbol binario
    def __buscar(sel,nodo,busqueda):
        if nodo is None:#Si el nodo esta vacio
            return None #Retornamos None
        if nodo.dato == busqueda: #Si el dato en el nodo es igual a busqueda
            return nodo
        if busqueda< nodo.dato: #Si la busqueda es menor que el dato, buscamos la izquierda
            return self.__buscar(nodo.izquierda,busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
    #Funciones publicas para usarlas cuando creamos una instancia nueva
    def agregar(self,dato):
        self.__agregar_recursivo(self.raiz,dato)#La funcion publicaa invoca el metodo privado para agregar
    def inorden(self):
        print("Imprimiendo arbol inorden:")
        self.__inorden_recursivo(self.raiz)#La funcion publica invoca el metodo privado para recorrer  inorden
        print("")
    def preorden(self):
        print("Imprimiendo arbol preorden:")
        self.__preorden_recursivo(self.raiz)#La funcion publica invoca el metodo privado para recorrer  preorden
        print("")
    def posorden(self):
        print("Imprimiendo arbol preorden:")
        self.__posorden_recursivo(self.raiz)#La funcion publica invoca el metodo privado para recorrer  posorden
        print("")
    def buscar(sel,busqueda):
        return self.__buacar(self.raiz,busqueda)#La  función publica invoca el metodo privado para buscar
               