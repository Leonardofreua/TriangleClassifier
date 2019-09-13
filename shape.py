import math
import sys
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image


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

        print(f"The triangle is {self._getAngleClassification(a, b, c)} and {self._getSideClassification(a, b, c)}\n")

    def showTriangle(self):
        points = ((self.a.pointX, self.a.pointY),
                  (self.b.pointX, self.b.pointY),
                  (self.c.pointX, self.c.pointY))
        self.designerConfig(points)

    def setPoints(self, shape):
        return ((shape.a.pointX, shape.b.pointY),
                (shape.b.pointX, shape.b.pointY),
                (shape.c.pointX, shape.c.pointY))

    def designerConfig(self, dimension=(400, 400), *args):
        image = Image.new("RGB", dimension)

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
            return "Equilateral"
        elif a == b or b == c:
            return "Isosceles"
        else:
            return "Scalene"

    def _getAngleClassification(self, a, b, c):
        if a + b > c:
            return "Acute"
        elif a + b == c:
            return "Rectangle"
        else:
            return "Obtuse"

    def classify(self):
        try:
            print("\nCoordinates of vector A:\n")
            self.a.pointX = int(input("X: "))
            self.a.pointY = int(input("Y: "))

            print("\nCoordinates of vector B:\n")
            self.b.pointX = int(input("X: "))
            self.b.pointY = int(input("Y: "))

            print("\nCoordinates of vector C:\n")
            self.c.pointX = int(input("X: "))
            self.c.pointY = int(input("Y: "))

            self._classifyTriangle(self.a, self.b, self.c)
        except ValueError:
            print('Insert numbers only!')

    def translation(self, triangle):
        print("Values to Translate the Triangle")
        t_x = int(input("Value 1: "))
        t_y = int(input("Value 2: "))

        T_triangle = triangle

        previous_points = self.setPoints(triangle)
        points = ((T_triangle.a.pointX + t_x, T_triangle.b.pointY - t_y),
                  (T_triangle.b.pointX + t_x, T_triangle.b.pointY - t_y),
                  (T_triangle.c.pointX + t_x, T_triangle.c.pointY - t_y))

        self.designerConfig(points, previous_points)

    def scaling(self, triangle):
        s_x = int(input("Value 1: "))
        s_y = int(input("Value 2: "))

        S_triangle = triangle

        previous_points = self.setPoints(triangle)
        points = ((s_x * S_triangle.a.pointX, s_y * S_triangle.b.pointY),
                  (s_x * S_triangle.b.pointX, s_y * S_triangle.b.pointY),
                  (s_x * S_triangle.c.pointX, s_y * S_triangle.c.pointY))

        self.designerConfig((800, 800), points, previous_points)


def main():
    triangle = Triangle()
    option = 0
    while option != 6:
        print('''           [ 1 ] Classiy Triangle
           [ 2 ] Show original Triangle
           [ 3 ] Translation
           [ 4 ] Scaling
           [ 5 ] Rotation
           [ 6 ] Exit''')

        option = int(input('>>> Option: '))

        if option == 1:
            triangle.classify()
        elif option == 2:
            triangle.showTriangle()
        elif option == 3:
            triangle.translation(triangle)
        elif option == 4:
            triangle.scaling(triangle)
        elif option == 6:
            sys.exit()
        else:
            print('Invalid option!')


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
