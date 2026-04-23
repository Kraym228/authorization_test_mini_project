from base.base_test import BaseTest
import pytest
import random
from pages.login_is_correct import LoggedInSuccessPage
import time
import allure


@allure.feature("Авторизация")
class TestLogin(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_login(self):
        self.login_page.open()
        self.login_page.enter_username('student')
        self.login_page.enter_password('Password123')
        self.login_page.submit()
        success_page = LoggedInSuccessPage(self.driver)
        success_page.is_open()
        assert self.driver.current_url == LoggedInSuccessPage.PAGE_URL
        assert 'Logged In Successfully' in success_page.text_is_correct()
        assert success_page.button_is_logout().is_displayed()
        
    @allure.severity(allure.severity_level.NORMAL)
    def test_negative_username(self): 
        self.login_page.open()
        self.login_page.enter_username('incorrectUser')
        self.login_page.enter_password('Password123')
        self.login_page.submit()
        error_name = self.login_page.get_error_username()
        assert "Your username is invalid!" in error_name
        
    @allure.severity(allure.severity_level.NORMAL)    
    def test_negative_password(self): 
        self.login_page.open()
        self.login_page.enter_username('student')
        self.login_page.enter_password('incorrectPassword')
        self.login_page.submit()
        password_name = self.login_page.get_error_password()
        assert "Your password is invalid!" in password_name