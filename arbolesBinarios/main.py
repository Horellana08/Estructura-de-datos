from arbol import Arbol  # Importamos

#ARBOL DE TIPO ENTERO
arbol_numeros = Arbol(5)
arbol_numeros.agregar(1984)
arbol_numeros.agregar(60)
arbol_numeros.agregar(10)
arbol_numeros.agregar(20)
arbol_numeros.agregar(10)
arbol_numeros.agregar(25)
arbol_numeros.agregar(59)
arbol_numeros.agregar(64)
arbol_numeros.agregar(10)
arbol_numeros.agregar(19)
arbol_numeros.agregar(23)
arbol_numeros.agregar(18)
arbol_numeros.agregar(1)
arbol_numeros.agregar(2013)
arbol_numeros.preorden()
arbol_numeros.inorden()
arbol_numeros.postorden()
busqueda = int(input("Ingresa un numero para buscar en el arbol:"))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"{busqueda}no existe")
else:
    print(f"{busqueda} si existe")