"""
Base class will contain all common functionality
"""


class BasePage:
    """Base page class that is initialized on every page object class."""

    def __init__(self, driver):
        self.driver = driver

    def __set__(self, locator, value):
        """Set the supplied text to the specified object"""
        element = self.driver.instance.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def __get__(self, locator):
        """Gets the text of the specified object"""
        element = self.driver.instance.find_element(*locator)
        return element.get_attribute("text")

    def click(self, locator):
        element = self.driver.instance.find_element(*locator)
        element.click()
