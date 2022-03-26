import pytest
import unittest
import time
from selenium import webdriver


class Math:

    def add(x, y):
        return x + y


browser = webdriver.Chrome('/Users/bronsinb/Downloads/chromedriver')
class Test(unittest.TestCase):

    def test_add(self):
        assert Math.add(1, 2) == 3

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