import unittest
from webdriver_docker import *

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = loadWebDriver_chrome()
        self.driver.get('https://www.google.com/')

    def tearDown(self): self.driver.quit()  # nothing here for now

    def test_01(self):
        search_input = self.driver.find_element_by_name('q')
        search_input.send_keys('selenium')
