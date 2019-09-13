import math
import sys
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image


# https://www.varsitytutors.com/hotmath/hotmath_help/topics/translations
# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
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
    def __init__(self):
        self.a = Point()
        self.b = Point()
        self.c = Point()

    def _classifyTriangle(self, p1, p2, p3):
        a = self._euclidDistSquare(p1, p2)
        b = self._euclidDistSquare(p1, p3)
        c = self._euclidDistSquare(p2, p3)

        print(f"O Triângulo é {self._getAngleClassification(a, b, c)} e {self._getSideClassification(a, b, c)}\n")

    def showTriangle(self):
        points = ((self.a.pointX, self.a.pointY),
                  (self.b.pointX, self.b.pointY),
                  (self.c.pointX, self.c.pointY))
        self.designerConfig(points)

    def designerConfig(self, *args):
        image = Image.new("RGB", (400, 400))

        draw = ImageDraw.Draw(image)

        for value in args:
            if args[0] == value:
                draw.polygon(value, fill=200)
            else:
                draw.polygon(value, outline='green')

        image.show()

    def _euclidDistSquare(self, p1, p2):
        return int(math.pow(p1.pointX - p2.pointX, 2)) + int(math.pow(p1.pointY - p2.pointY, 2))

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
            self.a.pointX = int(input("Vetor A1: "))
            self.a.pointY = int(input("Vetor A2: "))

            print("\nInforme os vetores da BASE (B) do Triângulo:\n")
            self.b.pointX = int(input("Vetor B1: "))
            self.b.pointY = int(input("Vetor B2: "))

            print("\nInforme os vetores do lado ESQUERDO (C) do Triângulo:\n")
            self.c.pointX = int(input("Vetor C1: "))
            self.c.pointY = int(input("Vetor C2: "))

            self._classifyTriangle(self.a, self.b, self.c)
        except ValueError:
            print('Insira apenas números!')

    def translation(self, triangle):
        print("Valores para Movimentar o Triângulo")
        t_x = int(input("Valor 1: "))
        t_y = int(input("Valor 2: "))

        triangleT = triangle

        after_point = ((triangle.a.pointX, triangle.b.pointY),
                       (triangle.b.pointX, triangle.b.pointY),
                       (triangle.c.pointX, triangle.c.pointY))
        points = ((triangleT.a.pointX + t_x, triangleT.b.pointY - t_y),
                  (triangleT.b.pointX + t_x, triangleT.b.pointY - t_y),
                  (triangleT.c.pointX + t_x, triangleT.c.pointY - t_y))

        self.designerConfig(points, after_point)


def main():
    triangle = Triangle()
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
            triangle.translation(triangle)
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
