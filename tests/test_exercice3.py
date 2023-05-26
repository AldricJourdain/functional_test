import sys
import pytest
from..exercice3 import *

def test_init():
    width = 7
    height = 4
    radius = 8
    side = 7
    r = Rectangle(width=width, height=height)
    assert r.width == 7
    assert r.height == 4
    c = Circle(radius=radius)
    assert c.radius == 8
    s = Square(side=side)
    assert s.width == side
    assert s.height == side

def test_area():
    width = 7
    height = 4
    radius = 8
    side = 7
    r = Rectangle(width=width, height=height)
    assert r.area() == width * height
    c = Circle(radius=radius)
    assert c.area() == (pi * radius ** 2)
    s = Square(side=side)
    assert s.area() == side * side

def test_perimeter():
    width = 7
    height = 4
    radius = 8
    side = 7
    r = Rectangle(width=width, height=height)
    assert r.perimeter() == 2 * (width + height)
    c = Circle(radius=radius)
    assert c.perimeter() == (2 * pi * radius)
    s = Square(side=side)
    assert s.perimeter() == 2 * (side + side)

def test_shape():
    s = Shape()
    s.area()
    s.perimeter()
