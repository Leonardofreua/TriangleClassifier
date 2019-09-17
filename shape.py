import math
import sys
import matplotlib.pyplot as plt


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
        self.img_names = {'original': 'original_triangle.jpg',
                          'translated': 'translated_triangle.jpg',
                          'scaled': 'scaled_triangle.jpg',
                          'rotated': 'rotated_triangle.jpg'}

    def _classifyTriangle(self, p1, p2, p3):
        a = self._euclidDistSquare(p1, p2)
        b = self._euclidDistSquare(p1, p3)
        c = self._euclidDistSquare(p2, p3)

        print(f"The triangle is {self._getAngleClassification(a, b, c)} and {self._getSideClassification(a, b, c)}\n")

    def _setPoints(self, shape):
        return ((shape.a.pointX, shape.a.pointY),
                (shape.b.pointX, shape.b.pointY),
                (shape.c.pointX, shape.c.pointY))

    def _designerConfig(self, points, file_name):
        points.append(points[0])

        xs, ys = zip(*points)

        plt.figure()
        plt.grid()
        plt.autoscale()
        plt.title(file_name.replace('.jpg', ''))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.plot(xs, ys, '-o')
        plt.savefig(file_name)
        plt.show()

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

    def showTriangle(self):
        points = [[self.a.pointX, self.a.pointY],
                  [self.b.pointX, self.b.pointY],
                  [self.c.pointX, self.c.pointY]]

        self._designerConfig(points, self.img_names['original'])

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

    def translation(self, polygon):
        print("Values to Translate the Triangle")
        t_x = int(input("Value 1: "))
        t_y = int(input("Value 2: "))

        translated_polygon = []
        T_triangle = polygon
        points = self._setPoints(T_triangle)

        for corner in points:
            translated_polygon.append((corner[0] - t_x, corner[1] - t_y))

        self._designerConfig(translated_polygon, self.img_names['translated'])

    def scaling(self, polygon):
        s_x = int(input("Value 1: "))
        s_y = int(input("Value 2: "))

        scaled_polygon = []
        S_triangle = polygon
        points = self._setPoints(S_triangle)

        for corner in points:
            scaled_polygon.append((s_x * corner[0], s_y * corner[1]))

        self._designerConfig(scaled_polygon, self.img_names['scaled'])

    def rotation(self, polygon):
        theta = int(input("Enter the angle: "))
        theta = math.radians(theta)
        rotated_polygon = []

        points = self._setPoints(polygon)

        for corner in points:
            rotated_polygon.append((int(round(corner[0] * math.cos(theta) - corner[1] * math.sin(theta), 0)),
                                    int(round(corner[0] * math.sin(theta) + corner[1] * math.cos(theta), 0))
                                    ))

        self._designerConfig(rotated_polygon, self.img_names['rotated'])


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
        elif option == 5:
            triangle.rotation(triangle)
        elif option == 6:
            sys.exit()
        else:
            print('Invalid option!')


if __name__ == '__main__':
    main()

# Vectpr A1: 100
# Vector A2: 150
#
# Vector B1: 200
# Vector B2: 150
#
# Vector C1: 200
# Vector C2: 100

#
# X: 20
# Y: 10
#
# X: 30
# Y: 20
#
# X: 10
# Y: 20
