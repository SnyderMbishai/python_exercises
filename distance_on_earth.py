"""The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))"""

from math import sin, cos

# a = float(input("point A: \nY1: "))
# b = float(input("point A: \nX1: "))
# c = float(input("point B: \nY2: "))
# d = float(input("point B: \nX2: "))

def distance_btn_two_places_on_earth():
    a = float(input("point A: \nY1: "))
    b = float(input("point A: \nX1: "))
    c = float(input("point B: \nY2: "))
    d = float(input("point B: \nX2: "))
    distance = 6371.01 * cos(sin(a) * sin(c) + cos(a) * cos(b) * cos(b-d))
    print(distance)

distance_btn_two_places_on_earth()

#to be solved

