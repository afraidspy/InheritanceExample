# -*- coding: utf-8 -*-

from PoligonoPadre import Poligono

class Rectangulo(Poligono):
    
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho
        super().__init__([largo, ancho, largo, ancho]);
        

    def area(self):
        return (self.__largo *  self.__ancho)
        
    def tipoPoligono(self):
        return "Rectangulo";
    
    def __str__(self):
        return "Rectangulo: " + super().__str__()