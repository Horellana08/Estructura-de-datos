class Pila:
    #iniclizamos una lista que represeta la Pila
    def __init__(self):
        self.elementos = list()
    
    #agrega elemento al final de la Pila
    def apilar(self, elemento):
        self.elementos.append(elemento)
        
    #borra elemento al final de la Pila
    def desapilar(self):
        try:
            return self.elementos.pop()
        except:
            raise ValueError("La Pila esta vacia")

    #verifica si la Pila esta vacia 
    def estaVacia(self):
        return len(self.elementos) == 0

    def tope(self):
        try:
            return self.elementos[len(self.elementos)-1]
        except:
            raise ValueError("La Pila esta vacia")


class Evaluador:
    # evaluamos expresion 1
    def evaluarExpresionUno(self, expresion):
        expresionDos = self.convertirExpresionDos(expresion)
        return self.evaluarExpresionDos(expresionDos)

    # evaluamos si la expresion dos es nuevo o simbolo
    def evaluarExpresionDos(self, expresion):
        pila = Pila()

        for caracter in expresion:
            if not self.operador(caracter):
                numero = float(caracter)
                pila.apilar(numero)
            else:
                numero2 = float(pila.desapilar())
                numero1 = float(pila.desapilar())
                resultado = self.operacion(caracter, numero1, numero2)
                pila.apilar(resultado)
                
        return pila.tope()

    #apilamos y desapilamos elementos segun su prioridad
    def convertirExpresionDos(self, expresion):
        pila = Pila()
        expresionDos = ""

        for caracter in expresion:
            if self.operador(caracter):
                if pila.estaVacia():
                    pila.apilar(caracter)
                else:
                    if self.prioridadEnExpresion(caracter) > self.prioridadEnPila(pila.tope()):
                        pila.apilar(caracter)
                    else:
                        expresionDos += pila.desapilar()
                        pila.apilar(caracter)
            else:
                expresionDos +=caracter

        
        while not pila.estaVacia():
            expresionDos += pila.desapilar()

        return expresionDos

    #prioridad de simbolo en expresion
    def prioridadEnExpresion(self, caracter):
        if caracter == '^': return 4
        if caracter == '*' or caracter == '/': return 2
        if caracter == '+' or caracter == '-': return 1
        return 0

    #prioridad de simbolo en pila
    def prioridadEnPila(self, caracter):
        if caracter == '^': return 3
        if caracter == '*' or caracter == '/': return 2
        if caracter == '+' or caracter == '-': return 1
        return 0

    #verificar si se trata de un operador
    def operador(self, caracter):
        if caracter == '+': return True
        if caracter == '-': return True
        if caracter == '*': return True
        if caracter == '/': return True
        if caracter == '^': return True
        return False

    #procesar operacion
    def operacion(self, simbolo, numero1, numero2):
        if simbolo == '+': return numero1 + numero2
        if simbolo == '-': return numero1 - numero2
        if simbolo == '*': return numero1 * numero2
        if simbolo == '/': return numero1 / numero2
        if simbolo == '^': return numero1 ** numero2
        return 0


evaluador = Evaluador()
expresion = input("Ingresa una expresion: ")
resultado = evaluador.evaluarExpresionUno(expresion)
print(resultado)