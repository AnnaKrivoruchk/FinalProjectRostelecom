from urllib.parse import urlparse
from params import LOGIN_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = LOGIN_URL
        self.driver.implicitly_wait(timeout)

    def get_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message = f'Not find {locator}')

    def find_elements(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message = f'Not find {locator}')

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def fimd_element_to_be_clickable(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message = f'Element not clickable')
