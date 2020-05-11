import os
from datetime import datetime
from time import sleep

from webdriver_docker import *

from src.service.util import load_input_from_xlsx


class Test:

    def test_01(self):
        wd = loadWebDriver_chrome()  # wd aka webdriver

        HOME = os.path.abspath(__file__ + '/../../'); testcase_excel = f'{HOME}/tests/fixture/test_fixture.xlsx'
        test_case_all = load_input_from_xlsx(testcase_excel)

        r_all = []  # r_all aka all_results
        for test_case_id, keyword in test_case_all.items():
            wd.get('https://www.google.com/')
            search_input = wd.find_element_by_name('q')
            search_input.send_keys(keyword)
            search_input.send_keys(Keys.ENTER)

            sleep(3)  # wait for search result
            snapshot_name = datetime.now().strftime("%Y%m%d-%H%M%S%f")
            snapshot = wd.save_screenshot(f'{HOME}/snapshot/{snapshot_name}.png')  # take snapshot search result

            r = {  # r aka testcase result
                'test_case_id': test_case_id,
                'keyword'     : keyword,
                'snapshot'    : snapshot_name,
            }; r_all.append(r)

        #NOTE quit() must put outside the loop
        wd.quit()  # nothing here for now
