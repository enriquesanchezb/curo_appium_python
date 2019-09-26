import pytest
from pages.login_page import LoginPage
from pages.button_page import ButtonPage

@pytest.mark.usefixtures("config_driver")
class TestLogin:
    def test_valid_login(self, config_driver):
        login_page = LoginPage(config_driver)
        login_page.login_as("a@foo.com", "123456")
        button_page = ButtonPage(config_driver)
        assert button_page.is_button_displayed
