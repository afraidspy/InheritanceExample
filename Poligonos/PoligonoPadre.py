# -*- coding: utf-8 -*-
"""
Implementación de una clase abstracta
"""
from abc import ABC, abstractmethod

class Poligono(ABC): 
    
    def __init__(self, lados):
        self._lados = lados
        self._num_lados = len(self._lados)
   
    def calcular_perimetro(self):
       sum = 0
       for valor in self._lados:
           sum += valor
       return sum
   
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def tipoPoligono(self):
        pass
    
    def __str__(self):
        estado=""
        for valor in self._lados:
            estado+= "Lado: " + str(valor)
        return estado