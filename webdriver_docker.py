from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def loadWebDriver_chrome():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME,
    )
    driver.implicitly_wait(10)
    return driver
