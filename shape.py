import math
import numpy as np
import cv2
import sys


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def pointX(self):
        return self.x

    @pointX.setter
    def pointX(self, x):
        self.x = x

    @property
    def pointY(self):
        return self.y

    @pointY.setter
    def pointY(self, y):
        self.y = y


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def _classifyTriangle(self, p1, p2, p3):
        a = self._euclidDistSquare(p1, p2)
        b = self._euclidDistSquare(p1, p3)
        c = self._euclidDistSquare(p2, p3)

        print(f"O Triângulo é {self._getAngleClassification(a, b, c)} e {self._getSideClassification(a, b, c)}\n")

    def showTriangle(self):
        image = np.ones((300, 300, 3), np.uint8) * 255

        a = (self.c.x, self.c.y)  # L and top
        b = (self.a.x, self.a.y)  # L and left base
        c = (self.b.x, self.b.y)  # R and right base

        triangle_cnt = np.array([a, b, c])

        cv2.drawContours(image, [triangle_cnt], 0, (0, 255, 0), -1)

        cv2.imshow("image", image)
        cv2.waitKey()

    def _euclidDistSquare(self, p1, p2):
        return int(math.pow(p1.x - p2.x, 2)) + int(math.pow(p1.y - p2.y, 2))

    def _getSideClassification(self, a, b, c):
        if a == b and b == c:
            return "Equilátero"
        elif a == b or b == c:
            return "Isósceles"
        else:
            return "Escaleno"

    def _getAngleClassification(self, a, b, c):
        if a + b > c:
            return "Acutângulo"
        elif a + b == c:
            return "Retângulo"
        else:
            return "Obtuso"

    def classify(self):
        try:
            print("\nInforme os vetores do lado DIREITO (A) do Triângulo:\n")
            self.a.x = int(input("Vetor A1: "))
            self.a.y = int(input("Vetor A2: "))

            print("\nInforme os vetores da BASE (B) do Triângulo:\n")
            self.b.x = int(input("Vetor B1: "))
            self.b.y = int(input("Vetor B2: "))

            print("\nInforme os vetores do lado ESQUERDO (C) do Triângulo:\n")
            self.c.x = int(input("Vetor C1: "))
            self.c.y = int(input("Vetor C2: "))

            self._classifyTriangle(self.a, self.b, self.c)
        except ValueError:
            print('Insira apenas números!')

    def translation(self):
        print("Valores para Movimentar o Triângulo")
        t_x = int(input("Valor 1: "))
        t_y = int(input("Valor 2: "))

        triangleTranslated = Triangle(self.a, self.b, self.c)


def main():
    p1 = Point()
    p2 = Point()
    p3 = Point()
    triangle = Triangle(p1, p2, p3)
    option = 0
    while option != 6:
        print('''           [ 1 ] Classificar Triângulo
           [ 2 ] Exibir
           [ 3 ] Translação
           [ 4 ] Escala
           [ 5 ] Rotação
           [ 6 ] Sair''')

        option = int(input('>>> Opção: '))

        if option == 1:
            triangle.classify()
        elif option == 2:
            triangle.showTriangle()
        elif option == 3:
            triangle.translation()
        elif option == 6:
            sys.exit()
        else:
            print('Opção inválida!')


if __name__ == '__main__':
    main()


# Vetor A1: 100
# Vetor A2: 150
#
# Vetor B1: 200
# Vetor B2: 150
#
# Vetor C1: 200
# Vetor C2: 100
