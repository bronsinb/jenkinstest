import json
import pytest
import unittest
import requests
from selenium import webdriver


class Math:

    def add(x, y):
        return x + y


@pytest.fixture
def num_input():
    return 4

@pytest.mark.subtract
def test_subtract(num_input):
    assert Math.add(num_input, -2) == 2

@pytest.mark.param
@pytest.mark.parametrize("test_input,expected", [(6, 9), (4, 6), (40, 42)])
def test_add_twice(test_input, expected):
    assert Math.add(test_input, 2) == expected

class Test(unittest.TestCase):

    @pytest.mark.math
    @pytest.mark.add
    def test_add(self):
        assert Math.add(1, 2) == 3

    @pytest.mark.math
    @pytest.mark.zero
    def test_divid_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0

    @pytest.mark.costco
    def test_costco(self):
        print("Step 1: Set Up Browser")
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome('/Users/bronsinb/Downloads/chromedriver', options=options)

        print("Step 2: Go to Costco")
        assert "signin" in "https://signin.costco.com", "Costco.com did not load"

        print("Step 3: Log In")
        print("Input credentials")
        assert "Auto Mation" in "Welcome Auto Mation!", "Sign in failed"

        print("Step 4: Finalize")
        driver.close()
        
    @pytest.mark.requests
    def test_get_spiderman_wikipedia(self):
        session = requests.Session()
        url = "https://en.wikipedia.org/wiki/Spider-Man:_Homecoming"

        print("Step 1: Get Wikipedia page")
        spiderman = session.get(url)
        assert spiderman.status_code == 200, "Wikipedia page did not load properly"
        
        print("Step 2: Verify if correct page loaded")
        assert "Spider-Man: Homecoming" in str(spiderman.content), "Wrong page"