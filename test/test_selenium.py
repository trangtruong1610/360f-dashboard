import os
import unittest
from webdriver_docker import *
from main.main import load_input_from_xlsx

file_path = os.path.abspath(os.pardir)

def setUpModule():    pass  # nothing here for now
def tearDownModule(): pass  # nothing here for now


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = loadWebDriver_chrome()
        self.driver.get('https://www.google.com/')

    def tearDown(self): self.driver.quit()  # nothing here for now

    def test_01(self):
        excel = f'{file_path}/fixture/test_fixture.xlsx'
        test_case = load_input_from_xlsx(excel)
        search_input = self.driver.find_element_by_name('q')
        search_input.send_keys(test_case[1])
