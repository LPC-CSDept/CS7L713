import main
import io
import sys
import re

# global rsum


def test_main_1():
    numbers = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
               [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]
    result = main.countCross(numbers)
    print('Your result', result)
    assert result == 5


def test_main_2():
    numbers = [[0, 1, 0, 1, 1],
               [1, 1, 1, 1, 1],
               [1, 1, 0, 1, 0],
               [1, 1, 1, 0, 1],
               [1, 1, 0, 1, 0]]
    result = main.countCross(numbers)
    print('Your result', result)
    assert result == 3
