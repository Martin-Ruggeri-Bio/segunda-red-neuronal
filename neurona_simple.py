import math

class NeuronaSimple():
    def __init__(self, entrada_1, entrada_2, peso_0=None, peso_1=None, peso_2=None, peso_3=None, entrada_3=None, salida_esperada=None):
        self.entrada_0 = 1
        self.entrada_1 = entrada_1
        self.entrada_2 = entrada_2
        self.entrada_3 = entrada_3
        self.peso_0 = peso_0
        self.peso_1 = peso_1
        self.peso_2 = peso_2
        self.peso_3 = peso_3
        self.salida_esperada = salida_esperada
        self.salida_real = 1
        self.delta = 0
        self.x = 0
    
    def entrenamiento(self):
        if self.entrada_3:
            x = (self.entrada_0 * self.peso_0) + (self.entrada_1 * self.peso_1) + (self.entrada_2 * self.peso_2) + (self.entrada_3 * self.peso_3)
            self.x = x
            self.salida_real = 1/(1+math.exp(x*(-1)))
            variacion_abs = self.salida_esperada - self.salida_real
            self.delta = self.salida_real*(1-self.salida_real)*variacion_abs
            variacion_peso_0 = 0.1*self.entrada_0*self.delta
            variacion_peso_1 = 0.1*self.entrada_1*self.delta
            variacion_peso_2 = 0.1*self.entrada_2*self.delta
            variacion_peso_3 = 0.1*self.entrada_3*self.delta
            self.peso_0 = self.peso_0 + variacion_peso_0
            self.peso_1 = self.peso_1 + variacion_peso_1
            self.peso_2 = self.peso_2 + variacion_peso_2
            self.peso_3 = self.peso_3 + variacion_peso_3
            return self.delta
        else:
            x = (self.entrada_0 * self.peso_0) + (self.entrada_1 * self.peso_1) + (self.entrada_2 * self.peso_2)
            self.x = x
            self.salida_real = 1/(1+math.exp(x*(-1)))
        return self.salida_real

    def entrenamiento_back(self, delta):
        delta_oculto = self.salida_real*(1-self.salida_real)*delta
        variacion_peso_0 = 0.1*self.entrada_0*delta_oculto
        variacion_peso_1 = 0.1*self.entrada_1*delta_oculto
        variacion_peso_2 = 0.1*self.entrada_2*delta_oculto
        self.peso_0 = self.peso_0 + variacion_peso_0
        self.peso_1 = self.peso_1 + variacion_peso_1
        self.peso_2 = self.peso_2 + variacion_peso_2
        x = (self.entrada_0 * self.peso_0) + (self.entrada_1 * self.peso_1) + (self.entrada_2 * self.peso_2)
        self.x = x
        self.salida_real = 1/(1+math.exp(x*(-1)))
        return self.salida_real

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
            salida_esperada: {self.salida_esperada}
            delta: {self.delta}
            salida_real: {self.salida_real}
        """)