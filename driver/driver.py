from appium import webdriver
import yaml


class Driver:
    def __init__(self, filename):
        with open(filename, 'r') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)
        self.instance = webdriver.Remote(cfg["appium_lib"]["server_url"], cfg["caps"])
