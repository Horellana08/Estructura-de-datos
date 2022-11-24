class Nodo:
    def __init__(self,dato):
        #El dato puede ser cualquier tipo , incluso un objeto si se sobreescriben los operadores de comparación
        self.dato=dato
        self.izquierda=None
        self.derecha=None