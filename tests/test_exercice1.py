import sys
import pytest
from..exercice1 import *

def test_add():
    c = Calculator()
    assert c.add(1, 1) == 2
    assert c.add(-1, -1) == -2

def test_subtract():
    c = Calculator()
    assert c.subtract(1, 1) == 0
    assert c.subtract(-1, -1) == 0

def test_multiply():
    c = Calculator()
    assert c.multiply(8, 2) == 16

def test_divide():
    c = Calculator()
    assert c.divide(16, 2) == 8
    pytest.raises(ValueError, c.divide, *[16, 0])

def test_power():
    c = Calculator()
    assert c.power(8, 2) == 64

def test_sqrt():
    c = Calculator()
    assert c.sqrt(64) == 8
    pytest.raises(ValueError, c.sqrt, *[-64])

def test_clear_memory():
    c = Calculator()
    c.memory = 5
    c.clear_memory()
    assert c.memory == 0

def test_get_memory():
    c = Calculator()
    c.memory = 5
    assert c.get_memory() == 5
