import os
from webdriver_docker import *

from main.main import load_input_from_xlsx


class Test:

    def test_01(self):
        self.driver = loadWebDriver_chrome()
        self.driver.get('https://www.google.com/')

        file_path = os.path.abspath(__file__ + '/../../')
        excel = f'{file_path}/fixture/test_fixture.xlsx'
        test_case = load_input_from_xlsx(excel)
        search_input = self.driver.find_element_by_name('q')
        search_input.send_keys(test_case[1])

        self.driver.quit()  # nothing here for now
