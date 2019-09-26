from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ButtonPage(BasePage):
    BUTTON_ID = (By.ID, 'enrique.appiumproject:id/button')

    def is_button_displayed(self):
        return self.__get__(self.BUTTON_ID) == "Push me"
