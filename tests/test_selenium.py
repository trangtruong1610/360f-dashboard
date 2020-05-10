import os
from webdriver_docker import *

from src.service.util import load_input_from_xlsx


class Test:

    def test_01(self):
        wd = loadWebDriver_chrome()  # wd aka webdriver

        TEST_HOME = os.path.abspath(__file__ + '/..'); testcase_excel = f'{TEST_HOME}/fixture/test_fixture.xlsx'
        test_case_all = load_input_from_xlsx(testcase_excel)

        r_all = []  # r_all aka all_results
        for test_case_id, keyword in test_case_all.enumerate():
            wd.get('https://www.google.com/')
            search_input = wd.find_element_by_name('q')
            search_input.send_keys(keyword)

            #TODO Trang take snapshot of the search result here and save to snapshot/YYYYmmDD-HHMMSSz.png aka :snapshot_f

            r = {  # r aka testcase result
                'test_case_id': test_case_id,
                'keyword'     : keyword,
                'snapshot'    : 'TODO snapshot_f',
            }; r_all.append(r)

        #TODO study to know quit() once or quit at every :tc end is faster
        wd.quit()  # nothing here for now
