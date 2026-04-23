from base.base_pages import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure




class LoggedInSuccessPage(BasePage):
    
    PAGE_URL = Links.CORRECT_USER
    
    LOGGED_FIELD = ('xpath' , "//h1[@class='post-title']")
    
    LOGOUT_FIELD = ('xpath', "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")
    
    
    @allure.step("Получение текста успешного входа")
    def text_is_correct(self):
        text_element = self.wait.until(EC.visibility_of_element_located(self.LOGGED_FIELD))
        return text_element.text
    
    @allure.step("Проверка отображения кнопки Log out")
    def button_is_logout(self):
        button = self.wait.until(EC.visibility_of_element_located(self.LOGOUT_FIELD))
        return button
    
