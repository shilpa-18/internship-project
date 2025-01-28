from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage(BasePage):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-name='Password']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")
    SECONDARY_TAB = (By.ID, "w-node-b528dfcf-d2ee-f936-302e-86e97f0796ec-7f66df20")
    # SECONDARY_TAB = (By.ID,"w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b")
    SECONDARY_PAGE = (By.CSS_SELECTOR, "[wized='listingsCounterMLS']")
    # SECONDARY_PAGE = (By.ID, "w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d4-7f66df43")
    MIN_PRICE_FIELD = (By.XPATH, "//div/div[1]//input[@id='field-5']")
    MAX_PRICE_FILED = (By.XPATH, "//div[2]/input[@id='field-5']")
    FILTER_BUTTON = (By.CSS_SELECTOR, "[wized='openFiltersWindow']")
    APPLY_FILTER_BUTTON = (By.CSS_SELECTOR, '[wized="applyFilterButtonMLS"]')


    def open_main_page(self):
        self.open_url('https://soft.reelly.io')

    def login_credentials(self, username, password):
        self.input_text(username, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BUTTON)

    def left_side_menu(self):
        self.click(*self.SECONDARY_TAB)

    def correct_page(self):
        self.click(*self.SECONDARY_PAGE)

    def filters(self):
        self.click(*self.FILTER_BUTTON)

    def filter_by_price(self, low_price, high_price):
        self.input_text(low_price, *self.MIN_PRICE_FIELD)
        self.input_text(high_price, *self.MAX_PRICE_FILED)
        self.click(*self.APPLY_FILTER_BUTTON)

    # def open_filters(self):
    #     self.click(*self.FILTER_BUTTON)
    #     self.click(*self.APPLY_FILTER_BUTTON)

    def verify_price_range(self, lower_price, higher_price):
        PRICE_CARD = (By.CSS_SELECTOR, '[wized="unitPriceMLS"]')
        prices = self.driver.find_elements(*PRICE_CARD)

        for price_card in prices:
            price_text = price_card.text.replace('AED', '').replace(' ', '').replace(',', '').strip()
            price = float(price_text)

            if not (lower_price <= price <= higher_price):
                raise AssertionError(f"Price {price} is not within the range {lower_price} - {higher_price}")

        print(f"All prices are within the range {lower_price} - {higher_price}")


