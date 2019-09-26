from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_ID = (By.ID, 'enrique.appiumproject:id/email')
    PASSWORD_ID = (By.ID, 'enrique.appiumproject:id/password')
    SIGN_IN_ID = (By.ID, 'enrique.appiumproject:id/email_sign_in_button')

    def login_as(self, mail, password):
        self.__set__(self.EMAIL_ID, mail)
        self.__set__(self.PASSWORD_ID, password)
        self.click(self.SIGN_IN_ID)
