import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from allure_commons.types import AttachmentType
import allure 


@pytest.fixture(scope='function',autouse=True)
def driver(request):
    options = Options()
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver 
    yield driver
    driver.quit()
    
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver = item.cls.driver
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)