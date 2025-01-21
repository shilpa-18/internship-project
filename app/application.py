from pages.base_page import BasePage
from pages.left_side_menu import Left
from pages.main_page import MainPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.left_side_menu = Left(driver)
        self.main_page = MainPage (driver)