import sys
import pytest
from..exercice2 import *

def test_init():
    input_string = "hello world"
    s = StringAnalyzer(input_string=input_string)
    assert s.input_string == "hello world"

def test_count_vowels():
    s = StringAnalyzer("hello world")
    count = s.count_vowels()
    assert count == 3

def test_count_consonants():
    s = StringAnalyzer("hello world")
    count = s.count_consonants()
    assert count == 7

def test_count_digits():
    s = StringAnalyzer("hello world1234")
    count = s.count_digits()
    assert count == 4

def test_count_words():
    s = StringAnalyzer("hello world !")
    count = s.count_words()
    assert count == 3

def test_count_lines():
    s = StringAnalyzer("hello\nworld\n!")
    count = s.count_lines()
    assert count == 3
