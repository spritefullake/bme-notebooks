from math import *
from enum import Enum
from helpers import sig

Shapes = Enum('CrystalShapes','FCC BCC HCP SimpleCubic')
# although r is unnecessary,
# this depicts the equation
# the atomic packing factor is also known as the filling factor
def apf(shape,r=1):
    # apf is the ratio of atoms to total space in a unit cell
    # a is the edge length
    if shape == Shapes.BCC:
        atoms = 2
        a = 4*r/sqrt(3)
    elif shape == Shapes.FCC:
        atoms = 4
        a = 4*r/sqrt(2)
    elif shape == Shapes.HCP:
        atoms = 2
        a = 2*r
    elif shape == Shapes.SimpleCubic:
        atoms = 1
        a = 2*r
    return atoms*4/3*pi*r**3/a**3