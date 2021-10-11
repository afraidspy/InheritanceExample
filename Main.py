# -*- coding: utf-8 -*-
from PoligonoPadre import Poligono
from TrianguloHijo import Triangulo
from CuadradoHijo  import Cuadrado
from RectanguloHijo import Rectangulo

poligono = Triangulo(12,14,23)
print('Perìmetro: ',poligono.calcular_perimetro())
print("Area: " ,poligono.area())
print(poligono)

poligono = Rectangulo(10,15)
print('Perìmetro: ',poligono.calcular_perimetro())
print("Area: " ,poligono.area())
print(poligono)



