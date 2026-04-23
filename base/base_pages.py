from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType



class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10 , poll_frequency=1)
        
    
    def open(self):
        with allure.step(f'Open page {self.PAGE_URL}'):
            self.driver.get(self.PAGE_URL)
        
    def is_open(self):
        with allure.step(f'Check open page {self.PAGE_URL}'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))
        
