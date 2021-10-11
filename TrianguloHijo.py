# -*- coding: utf-8 -*-
from PoligonoPadre import Poligono
import math

class Triangulo(Poligono): 
    
    def __init__(self,lado1, lado2, lado3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3        
        super().__init__([lado1,lado2,lado3]);
    
    def area(self):
        s = super().calcular_perimetro() / 2
        resta1 = s-self.__lado1
        resta2 = s-self.__lado2
        resta3 = s-self.__lado3
        
        return math.sqrt(s*resta1*resta2*resta3)
    
    def tipoPoligono(self):
        return "Triangulo"
    
    def __str__(self):
        return "Triangulo: " + super().__str__()
    

