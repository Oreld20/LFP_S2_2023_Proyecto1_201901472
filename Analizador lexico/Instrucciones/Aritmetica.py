from Abstract.Abstract  import Expression
import math

class Aritmetica(Expression):

    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        operacion = self.tipo.operar(arbol)
        if self.left != None:
            valor1 = self.left.operar(arbol)
        if self.right != None:
            valor2 = self.right.operar(arbol)
        
        if isinstance(valor1, list):
            valor1 = self.operar(valor1[0])
        if isinstance(valor2, list):
            valor2 = self.operar(valor2[0])
        resultado = self.realizar_operacion(operacion, valor1, valor2)
        return resultado


    def realizar_operacion(self, operacion, valor1, valor2):
        if operacion == "suma":
            return valor1 + valor2
        elif operacion == "resta":
            return valor1 - valor2
        elif operacion == "multiplicacion":
            return valor1 * valor2
        elif operacion == "division":
            if valor2 == 0:
                return "Error: División por cero"
            return valor1 / valor2
        elif operacion == "seno":
            return math.sin(math.radians(valor1))
        elif operacion == "coseno":
            return math.cos(math.radians(valor1))
        elif operacion == "tangente":
            return math.tan(math.radians(valor1))
        elif operacion == "inverso":
            if valor1 == 0:
                return "Error: División por cero"
            return 1 / valor1
        elif operacion == "raiz":
            if valor2 == 0:
                return "Error: División por cero"
            return math.sqrt(valor1) ** (1 / valor2)
        elif operacion == "potencia":
            return valor1 ** valor2
        elif operacion == "mod":
            return valor1 % valor2
        else:
            return "Error: Operación no válida"

    

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
