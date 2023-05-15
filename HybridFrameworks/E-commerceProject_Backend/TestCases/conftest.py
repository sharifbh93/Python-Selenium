from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(3)
    return driver
#
# @pytest.fixture()
# def setup(browser):
#     if browser=='chrome':
#         driver=webdriver.Chrome()
#         print("Launching chrome browser.........")
#     elif browser=='firefox':
#         driver = webdriver.Firefox()
#         print("Launching firefox browser.........")
#
#     else:
#         driver=webdriver.Edge
#     return driver
#
# def pytest_addoption(parser):    # This will get the value from CLI /hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sharif'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)