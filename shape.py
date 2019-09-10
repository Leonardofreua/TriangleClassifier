import math
import numpy as np
import cv2
import sys


class Triangle:
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

    def showTriangle(self, p1, p2, p3):
        image = np.ones((300, 300, 3), np.uint8) * 255

        pt1 = (p3.x, p3.y)  # L and top
        pt2 = (p1.x, p1.y)  # L and left base
        pt3 = (p2.x, p2.y)  # R and right base

        triangle_cnt = np.array([pt1, pt2, pt3])

        cv2.drawContours(image, [triangle_cnt], 0, (0, 255, 0), -1)

        cv2.imshow("image", image)
        cv2.waitKey()

    def classifyTriangle(self, p1, p2, p3):
        a = self.euclidDistSquare(p1, p2)
        b = self.euclidDistSquare(p1, p3)
        c = self.euclidDistSquare(p2, p3)

        print(f"O Triângulo é {self.getAngleClassification(a, b, c)} e {self.getSideClassification(a, b, c)}")

    def euclidDistSquare(self, p1, p2):
        return math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2)

    def getSideClassification(self, a, b, c):
        if a == b and b == c:
            return "Equilátero"
        elif a == b or b == c:
            return "Isósceles"
        else:
            return "Escaleno"

    def getAngleClassification(self, a, b, c):
        if a + b > c:
            return "Acutângulo"
        elif a + b == c:
            return "Retângulo"
        else:
            return "Obtuso"

    def classify(self, P1, P2, P3):
        print("\nInforme os vetores do lado DIREITO (A) do Triângulo:\n")
        P1.x = int(input("Vetor A1: "))
        P1.y = int(input("Vetor A2: "))

        print("\nInforme os vetores da BASE (B) do Triângulo:\n")
        P2.x = int(input("Vetor B1: "))
        P2.y = int(input("Vetor B2: "))

        print("\nInforme os vetores do lado ESQUERDO (C) do Triângulo:\n")
        P3.x = int(input("Vetor C1: "))
        P3.y = int(input("Vetor C2: "))

        self.classifyTriangle(P1, P2, P3)

    def menu(self):
        P1 = Triangle()
        P2 = Triangle()
        P3 = Triangle()
        option = 0
        while option != 6:
            print('''            [ 1 ] Classificar Triângulo
            [ 2 ] Exibir
            [ 3 ] Translação
            [ 4 ] Escala
            [ 5 ] Rotação
            [ 6 ] Sair''')

            option = int(input('>>> Opção: '))

            if option == 1:
                self.classify(P1, P2, P3)
            elif option == 2:
                self.showTriangle(P1, P2, P3)
            elif option == 6:
                sys.exit()


def main():
    triangle = Triangle()
    triangle.menu()


if __name__ == '__main__':
    main()
