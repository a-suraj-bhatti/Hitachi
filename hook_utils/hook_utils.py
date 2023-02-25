import time
from collections import defaultdict
import pytest
import webdriver_manager.chrome
from selenium import webdriver
import yaml
import os
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from hook_utils.config_utils import ConfigUtils


class HookUtils:
    def __init__(self):
        self.config_utils = ConfigUtils(os.getcwd())

    def pytest_global_configuration(self):
        try:
            pytest.driver = None
        except Exception as e:
            raise Exception(e)

    def browser_setup(self):
        try:
            str_browser_name = self.config_utils.get_browser_name()
            print('++++++++++++++++++EXECUTION STARTED++++++++++++++++++++')
            if str_browser_name == "Chrome":
                options = webdriver.ChromeOptions()
                options.add_argument('--incognito')
                pytest.driver = webdriver.Chrome()
            elif str_browser_name == "Firefox":
                pytest.driver = webdriver.Firefox()
            elif str_browser_name == "Edge":
                pytest.driver - webdriver.Edge()
            else:
                raise Exception("Browser not supported")
            pytest.driver.implicitly_wait(20)
            pytest.driver.maximize_window()
        except Exception as e:
            raise Exception(e)

    def teardown(self):
        try:
            pytest.driver.quit()
        except Exception as e:
            raise Exception(e)

    # def send_email(self):
    #
