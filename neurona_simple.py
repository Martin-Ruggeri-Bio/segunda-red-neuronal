import math

class NeuronaSimple():
    def __init__(self, entrada_1, entrada_2, peso_0, peso_1, peso_2, peso_3=None, entrada_3=None,):
        self.entrada_0 = 1
        self.entrada_1 = entrada_1
        self.entrada_2 = entrada_2
        self.entrada_3 = entrada_3
        self.peso_0 = peso_0
        self.peso_1 = peso_1
        self.peso_2 = peso_2
        self.peso_3 = peso_3
        self.salida_real = 1
        self.x = 0
    
    def entrenamiento(self):
        if self.entrada_3 and self.peso_3:
            x = (self.entrada_0 * self.peso_0) + (self.entrada_1 * self.peso_1) + (self.entrada_2 * self.peso_2) + (self.entrada_3 * self.peso_3)
            self.x = x
            self.salida_real = 1/(1+math.exp(x*(-1)))
        else:
            x = (self.entrada_0 * self.peso_0) + (self.entrada_1 * self.peso_1) + (self.entrada_2 * self.peso_2)
            self.x = x
            self.salida_real = 1/(1+math.exp(x*(-1)))
        return 1/(1+math.exp(x*(-1)))

    def __str__(self):
        return (f"""
            entrada 0: {self.entrada_0}
            entrada_1: {self.entrada_1}
            entrada_2: {self.entrada_2}
            entrada_3: {self.entrada_3}
            peso_0: {self.peso_0}
            peso_1: {self.peso_1}
            peso_2: {self.peso_2}
            peso_3: {self.peso_3}
            x: {self.x}
            salida_real: {self.salida_real}
        """)