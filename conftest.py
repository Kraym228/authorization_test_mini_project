import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 


@pytest.fixture(scope='function',autouse=True)
def driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver 
    yield driver
    driver.quit()
    
    