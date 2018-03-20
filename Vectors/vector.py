import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __add__(self,v):
        if self.dimension!=v.dimension:
            raise ValueError('The dimensions of two vectors should be equal')
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self,v):
        if(self.dimension!=v.dimension):
            raise ValueError('The dimensions of two vectors should be equal')
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self,scalar):
        new_coordinates = [x*Decimal(scalar) for x in self.coordinates]
        return Vector(new_coordinates)

    def get_magnitude(self):
        return math.sqrt(sum([x*x for x in self.coordinates]))

    def normalize(self):
        magnitude = self.get_magnitude()
        try:
            return self.times_scalar((Decimal('1.0')/Decimal(magnitude)))
        except ZeroDivisionError:
            raise Exception("Cannnot normalize a zero vector")

    def dotProduct(self,v):
        if (self.dimension != v.dimension):
            raise ValueError('The dimensions of two vectors should be equal')
        return sum([x1*x2 for x1,x2 in zip(self.coordinates,v.coordinates)])

    def angleWith(self,v, inDegrees = False):
        try:
            unit_vector1 = self.normalize()
            unit_vector2 = v.normalize()
            angleRadians = math.acos(unit_vector1.dotProduct(unit_vector2))
            if inDegrees:
                return math.degrees(angleRadians)
            else:
                return angleRadians
        except Exception as e:
            if str(e) == "Cannnot normalize a zero vector":
                raise Exception("Cannot calculate angle between a vector and zero vector")
            else:
                raise e

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

v = Vector([8.218,9.314])
w = Vector([-1.129,2.111])
print(v+w)

v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print(v-w)

v = Vector([1.671,-1.012,-0.318])
c= 7.41
print(v.times_scalar(c))

v = Vector([-0.221,7.437])
print(v.get_magnitude())

v = Vector([8.813,-1.331,-6.247])
print(v.get_magnitude())

v = Vector([5.581, -2.136])
print(v.normalize())

v = Vector([1.996,3.108,-4.554])
print(v.normalize())

v = Vector([7.887,4.138])
w = Vector([-8.802,6.776])
print(v.dotProduct(w))

v = Vector([-5.955,-4.904,-1.874])
w = Vector([-4.496,-8.755,7.103])
print(v.dotProduct(w))

v = Vector([3.183,-7.627])
w = Vector([-2.668,5.319])
print(v.angleWith(w,False))

v = Vector([7.35,0.221,5.188])
w = Vector([2.751,8.259,3.985])
print(v.angleWith(w,True))