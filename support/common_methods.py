import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta



class CommonMethods:

    def navigate_to_webpage(self,pstr_url):
        try:
            pytest.driver.get(pstr_url)
        except Exception as e:
            raise Exception(e)

    def get_clickable_web_element(self,locator,explicit_wait=0):
        try:
            element = WebDriverWait(pytest.driver,explicit_wait).until(EC.element_to_be_clickable((By.XPATH, locator)))
            return element
        except  Exception as e:
            raise Exception(e)



    def wait_for_element_invisiblity(self,locator,explicit_wait):
        try:
            WebDriverWait(pytest.driver, explicit_wait).until(EC.invisibility_of_element_located((By.XPATH, locator)))
        except  Exception as e:
            raise Exception(e)

    def dismiss_sign_in_notification_if_exists(self):
        try:
            self.get_clickable_web_element(pytest.locators.str_dismiss_sign_in, 10).click()
        except Exception as e:
            pass

    def get_future_date(self):
        try:
            future_date = datetime.now() + timedelta(days=5)
            formatted_date = future_date.strftime("%_d %B %Y")
            return formatted_date
        except  Exception as e:
            raise Exception(e)

