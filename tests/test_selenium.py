import os
from webdriver_docker import *

from main.main import load_input_from_xlsx


class Test:

    def test_01(self):
        wd = loadWebDriver_chrome()
        wd.get('https://www.google.com/')  # wd aka webdriver

        file_path = os.path.abspath(__file__ + '/../../')
        excel = f'{file_path}/fixture/test_fixture.xlsx'
        test_case = load_input_from_xlsx(excel)
        search_input = wd.find_element_by_name('q')
        search_input.send_keys(test_case[1])

            #TODO Trang take snapshot of the search result here and save to snapshot/

        #TODO study to know quit() once or quit at every :tc end is faster
        wd.quit()  # nothing here for now
