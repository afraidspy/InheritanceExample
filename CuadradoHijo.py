# -*- coding: utf-8 -*-

from PoligonoPadre import Poligono
import math
class Cuadrado(Poligono):
    
    def __init__(self, lado):
        self.__lado = lado
        super().__init__([lado,lado,lado,lado]);
        
    def area(self):
        return math.pow(self.__lado, 2)
    
    def tipoPoligono(self):
        return "Cuadrado";
    
    def __str__(self):
        return "Cuadrado: " + super().__str__()
    
    
    
    