from base.base_pages import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure




class LoginPage(BasePage):
    PAGE_URL = Links.HOST
    
    
    USERNAME_FIELD = ('xpath' , "//input[@id='username']")
    PASSWORD_FIELD = ('xpath' , "//input[@id='password']")
    SUBMIT_BUTTON = ('xpath' , "//button[@id='submit']")
    ERROR_NAME_FIELD = ('xpath' , "//div[text()='Your username is invalid!']")
    ERROR_PASSWORD_FIELD = ('xpath', "//div[text()='Your password is invalid!']")
    
    @allure.step("Ввод username: {username}")  
    def enter_username(self,username):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(username)
    
    @allure.step("Ввод password: {password}")
    def enter_password(self,password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)
    
    @allure.step("Нажатие кнопки Submit")
    def submit(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
       
    @allure.step("Получение сообщения об ошибке username")    
    def get_error_username(self):
        error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_NAME_FIELD))
        return error_element.text
    
    @allure.step("Получение сообщения об ошибке password")
    def get_error_password(self):
        error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_PASSWORD_FIELD))
        return error_element.text