import pytest
from hook_utils.hook_utils import HookUtils
from support.locators import locators

hook_utils = HookUtils()
def pytest_configure():
    hook_utils.pytest_global_configuration()


def pytest_sessionstart(session: "Session"):
    hook_utils.browser_setup()
    pytest.locators = locators()


def pytest_sessionfinish(session, exitstatus):
    hook_utils.teardown()



