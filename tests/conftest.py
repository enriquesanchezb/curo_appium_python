import pytest
import os
from driver import driver

@pytest.fixture(scope="class")
def config_driver():
    abs_file_path = os.path.join(os.path.dirname(__file__), "../config/android.yml")
    appium_driver = driver.Driver(abs_file_path)
    yield appium_driver
    appium_driver.instance.quit()

