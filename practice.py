import pytest
import unittest


class Math:

    def add(x, y):
        return x + y


class Test(unittest.TestCase):

    @pytest.mark.add
    def test_add(self):
        assert Math.add(1, 2) == 3, "Incorrect adding" 

    @pytest.mark.addtwice
    def test_add_twice(self):
        assert Math.add(2, Math.add(1, 2)) == 5, "Not Correct"