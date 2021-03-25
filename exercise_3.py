from math import sqrt

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return '({self.x},{self.y})'.format(self=self)
    def calculate(self, x_2, y_2):
        return sqrt((x_2 - self.x) + (y_2 - self.y))


cord_x1 = int(input('First dot cord X: '))
cord_y1 = int(input('First dot cord Y: '))
cord_x2 = int(input('Second dot cord X: '))
cord_y2 = int(input('Second dot cord Y: '))


test = Point(cord_x1,cord_y1)
print(test.calculate(cord_x2,cord_y2))